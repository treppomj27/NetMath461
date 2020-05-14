
from itertools import combinations

Deck = []
Ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Suits = ['♠', '♣', '♡', '♢']
for i in range(0, 13):
    for j in range(0, 4):
        Deck.append(Ranks[i] + Suits[j])

Hands = list(combinations(Deck, 2))
N = len(Hands)

A = []
for i in range(0, N):
    if Hands[i][0][:1] == 'A' or Hands[i][1][:1] == 'A':
        A.append(Hands[i])

B = []
for i in range(0, N):
    if Hands[i][0] == 'A♠' or Hands[i][1] == 'A♠':
        B.append(Hands[i])

print('# of Two Card Hands:', N)
print('# of Two Card Hands with an Ace:', len(A))
print('# of Two Card Hands with the Ace of Spades:', len(B))

C_and_A = []
for i in range(0, len(A)):
    if A[i][0][:1] == 'A' and A[i][1][:1] == 'A':
        C_and_A.append(A[i])

C_and_B = []
for i in range(0, len(B)):
    if B[i][0][:1] == 'A' and B[i][1][:1] == 'A':
        C_and_B.append(B[i])

print('C_and_A:', len(C_and_A))
print('C_and_B:', len(C_and_B))

print('P(Pocket Aces | Ace) =', round(len(C_and_A) / len(A) * 100, 2), '%')
print('P(Pocket Aces | Ace of Spades) =', round(len(C_and_B) / len(B) * 100, 2), '%')
