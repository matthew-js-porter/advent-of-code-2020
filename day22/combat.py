def play(player1: list, player2: list) -> int:
    plays_cache = []
    while len(player1) != 0 and len(player2) != 0:
        cards = {'1': player1.copy(), '2': player2.copy()}
        if cards in plays_cache:
            return (1, score(player2))
        plays_cache.append(cards)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            winner = play(player1.copy()[:card1], player2.copy()[:card2])[0]
            if winner == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)

        else:
            if card1 > card2:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)

    if len(player1) == 0:
        return (2, score(player2))
    else:
        return (1, score(player1))


def score(loser: list) -> int:
    winning_score = 0
    loser.reverse()
    for i in range(1, len(loser) + 1):
        winning_score += i * loser[i - 1]

    return winning_score


if __name__ == '__main__':
    player1 = [27, 29, 30, 44, 50, 5, 33, 47, 34, 38, 36, 4, 2, 18, 24, 16, 32, 21, 17, 9, 3, 22, 41, 31, 23]
    player2 = [25, 1, 15, 46, 6, 13, 20, 12, 10, 14, 19, 37, 40, 26, 43, 11, 48, 45, 49, 28, 35, 7, 42, 39, 8]
    print(play(player1, player2))
