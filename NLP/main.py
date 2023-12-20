'''
고딩코딩 MNIST구현하고 강의하는 거 보고 감명받아서 카피코딩
'''

# Procedure
# 1. Collect Data
# 2. Prepare Data
# 3. Choose a model / make a model
# 4. Train the model
# 5. Test the model
# 6. Update/optimize parameters
# 7. Make predictions

import random
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torch import nn

train_dataset = datasets.MNIST(root='data', train = True, download=True, transform=ToTensor())
test_dataset = datasets.MNIST(root='data', train = False, download=True, transform=ToTensor())

## Image Dataload test (based on MNIST)
# image, label = train_dataset[0] # 1st data : 5 
# plt.imshow(image, cmap='gray')
# plt.show()
# print('label: ', label)

batch_size = 100

train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size)

## If cuda available this code 
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

## ***If M1 GPU[MPS : Multi Process Service] available***   this code 
device = torch.device('mps:0' if torch.backends.mps.is_available() else 'cpu')
print (f"PyTorch version:{torch.__version__}") # 1.12.1 이상
print(f"MPS 장치를 지원하도록 build 되었는지: {torch.backends.mps.is_built()}") # True 여야 합니다.
print(f"MPS 장치가 사용 가능한지: {torch.backends.mps.is_available()}") # True 여야 합니다.
# !python -c 'import platform;print(platform.platform())'

print(f'Device: {device}')

input_size = 28*28
output_size = 10

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(input_size, output_size)
        
    def forward(self, x):
        out = self.flatten(x)
        out = self.linear(out)
        return out

model = NeuralNet().to(device)
# print(model)

learning_rate = 0.001

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)


def train(train_dataloader, model, loss_fn, optimizer):
    for batch, (X, y) in enumerate(train_dataloader):
        X, y = X.to(device), y.to(device)
        
        pred = model(X)
        loss = loss_fn(pred, y)
        
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        
        if batch%100 == 0:
            loss = loss.item()
            print(f'loss: {loss}, batch: {batch}')

def test(test_dataloader, model, loss_fn):
    size = len(test_dataloader.dataset)
    num_batches = len(test_dataloader)
    test_loss, correct = 0, 0
    
    with torch.no_grad():
        for X, y in test_dataloader:
            X, y = X.to(device), y.to(device)
            
            pred = model(X)
            
            test_loss += loss_fn(pred,y).item()
            correct += (pred.argmax(1)==y).type(torch.float).sum().item()
            
    test_loss/=num_batches
    correct/=size
    print(f"Test Error: \n Accuracy: {(100*correct):0.1f}%, Avg loss: {test_loss:>8f} \n")
        
epochs = 10

for t in range(epochs):
    print(f"Epoch {t+1}\n ------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)
print("Done!")

real_test_dataset = datasets.MNIST(root='data', train=False, download=True)
rand = random.randint(0, 9999)
X, y = test_dataset[rand][0], test_dataset[rand][1]
A = real_test_dataset[rand][0]

# print(X) # Tensor
# print(y) # Label
# print(A) # Img

model = model.to('cpu') # device transform, if you use mps

with torch.no_grad():
    pred = model(X)
    predicted, actual = pred[0].argmax(0), y
    print(f"predicted: {predicted}. actual: {actual}")
    plt.imshow(A, cmap='gray')
    plt.show()





