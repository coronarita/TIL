import torch

# torch.nn.Transformer
# TRANSFORMER > TransformerEncoder > TransformerEncoderLayer > MultiheadAttention > multi_head_attention_forward > _scaled_dot_product_attention
# 추적해서 코드변경 필요시 트래킹 ! 


def multi_head_attention(Q, K, V):
    num_batch, num_head, num_token_length, att_dim = K.shape
    #(0,1,2,3) -> permute로 뒤에서 변경하기 위한 순서! 
    # num_token_length : 배치단위로 처리하다 보면, 토큰, 즉 단어의 개수가 같지않아, max_length로 처리
    # att_dim : 모델의 hidden dimension과 다름. 
    Q = Q / (att_dim**0.5)
    
    attention_score = Q @ K.permute(0,1,3,2) # 4dim - transpose 불가, 빈번하게 사용됨
    # num_batch, num_head, att_dim, num_token_length
    # masking
    # attention_score_mask = 

    attention_score = torch.softmax(attention_score, dim=3)

    Z = attention_score @ V #     # num_batch, num_head,  num_token_length, att_dim
    
    return Z, attention_score
    
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, Q, K, V):
        # Self : Q=K=V / Cross: Q!=K!=V
        
        num_batch, num_head, num_token_length, att_dim = K.shape
        #(0,1,2,3) -> permute로 뒤에서 변경하기 위한 순서! 
        # num_token_length : 배치단위로 처리하다 보면, 토큰, 즉 단어의 개수가 같지않아, max_length로 처리
        # att_dim : 모델의 hidden dimension과 다름. 
        Q = Q / (att_dim**0.5)
        
        attention_score = Q @ K.permute(0,1,3,2) # 4dim - transpose 불가, 빈번하게 사용됨
        # num_batch, num_head, att_dim, num_token_length
        # masking
        # attention_score_mask = 
    
        attention_score = torch.softmax(attention_score, dim=3)
    
        Z = attention_score @ V #     # num_batch, num_head,  num_token_length, att_dim
        
        return Z, attention_score
     
class Encoder(torch.nn.Module):
    
    def __init__(self, hidden_dim, num_head, dropout_p = 0.5):
        super().__init__()
        
        self.num_head = num_head
        self.hidden_dim = hidden_dim
        
        
        self.MHA = MultiHeadAttention()
        
        self.W_Q = torch.nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.W_K = torch.nn.Linear(hidden_dim, hidden_dim, bias=False) 
        self.W_V = torch.nn.Linear(hidden_dim, hidden_dim, bias=False)
        
        self.W_O = torch.nn.Linear(hidden_dim, hidden_dim, bias=False)

        self.LayerNorm1 = torch.nn.LayerNorm(hidden_dim)
        self.LayerNorm2 = torch.nn.LayerNorm(hidden_dim)
        
        self.Dropout = torch.nn.Dropout(p=dropout_p)
        
        self.Linear1 = torch.nn.Linear(hidden_dim, hidden_dim)
        self.Linear2 = torch.nn.Linear(hidden_dim, hidden_dim)
        
        self.Activation = torch.nn.ReLU()

    def to_multihead(self, vector):
        num_batch, num_token_length, hidden_dim = vector.shape
        att_dim = hidden_dim // self.num_head
        vector = vector.view(num_batch, num_token_length, self.num_head, att_dim) # [num_batch, num_token_length, num_head, att_dim]
        vector = vector.permute(0,2,1,3) # [num_batch, num_head, num_token_length, att_dim]
        return vector
    
    def forward(self, input_Q, input_K, input_V):        
        # input_Q : [num_batch, num_token_length, hidden_dim]
        
        Q = self.W_Q(input_Q) # [num_batch, num_token_length, hidden_dim]
        K = self.W_K(input_K)  
        V = self.W_V(input_V)
        
        num_batch, num_token_length, hidden_dim = Q.shape
        
        Q = self.to_multihead(Q) # [num_batch, num_head, num_token_length, att_dim]
        K = self.to_multihead(K)
        V = self.to_multihead(V)        
        
        Z , attention_score = self.MHA(Q,K,V)  # [num_batch, num_head, num_token_length, att_dim]
        # Z , _ = self.MHA(Q,K,V) # 필요없으면
    
        Z = Z.permute(0,2,1,3)  # [num_batch, num_token_length, num_head, att_dim]
        Z = Z.reshape(num_batch, num_token_length, self.hidden_dim)
        
        Z = self.W_O(Z)
        
        Z = self.LayerNorm1(self.Activation(Z) + input_Q)
        Z1 = self.Dropout(Z)
        
        Z = self.Activation(self.Linear1(Z1))
        Z = self.Dropout(Z)
        Z = self.Activation(self.Linear2(Z))
        Z = self.Dropout(Z)
        
        Z = Z + Z1
        
        Z = self.LayerNorm2(Z)
        
        return Z
        
        
if __name__ == "__main__":
    device = torch.device('mps')
    num_batch = 16
    num_head = 2
    hidden_dim = 64
    num_token_length = 8
    
    X = torch.Tensor(torch.randn(num_batch, num_token_length, hidden_dim))
    print('X.shape:',X.shape)
    
    self_attention_encoder = Encoder(hidden_dim=hidden_dim, num_head=num_head)
    
    Z = self_attention_encoder(input_Q=X, input_K=X, input_V=X) # input_V = Y 이면 cross_head attention
    print('Z.shape:',Z.shape)

    
    from torch.nn.modules import TransformerEncoderLayer
    official_encoder = TransformerEncoderLayer(d_model=hidden_dim, nhead=num_head, dim_feedforward=hidden_dim)
    official_Z = official_encoder(X)
    print('official_Z.shape:', official_Z.shape)
