class Poker():
    def __init__(self) -> None:
        self.hand = [0] * 14
        self.score = 0
        self.count = 0


    def draw(self, card):
        self.hand[card] += 1
        self.count += 1

    def discard(self):
        self.hand = [0] * 14
        self.score += 1
        self.count = 0

    def check_fh(self):
        joker = self.hand[0]
        cards = self.hand[1:]
        pair = cards.count(2)
        # cards over 3 
        triple = filter(lambda x: x>=3, cards)
        if (joker + pair >= 3) and not (joker != 0):  # 3,0, 2,1,1,2 (not 0,3)
            return True
        if (joker + pair >= 1) and list(triple):
            return True



def solution(cards):
    gamer = Poker()
    for card in cards:
        gamer.draw(card)
        if gamer.count <5: 
            continue
        elif gamer.check_fh():
            gamer.discard()
    return gamer.score

print(solution([2,2,2,0,0,3,3,3,4,4,10,11,12,11]))