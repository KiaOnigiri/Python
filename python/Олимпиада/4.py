N = int(input())

cards = [int(input()) for _ in range(N)]

chain = []

for card in cards:
    if not chain:
        chain.append(card)
    else:
        if card >= chain[0]:
            chain.insert(0, card)
        else:
            chain.append(card)

number = int(''.join(map(str, chain)))

print(number)
