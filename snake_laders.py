import random


def throw_dice():
    return random.randint(1, 6)


def game_board(player, score):
    player = player + score
    if player == 27:
        print("Bit by the snake")
        player = 1
    elif player == 21:
        print("Bit by the snake")
        player = 9
    elif player == 17:
        print("Bit by the snake")
        player = 4
    elif player == 19:
        print("Bit by the snake")
        player = 7
    elif player == 3:
        print("Climbed by the ladder")
        player = 22
    elif player == 5:
        print("Climbed by the ladder")
        player = 8
    elif player == 20:
        print("Climbed by the ladder")
        player = 29
    elif player == 11:
        print("Climbed by the ladder")
        player = 26
    return player  # this will return the position of player


def game_play(playerpos):
    score = throw_dice()
    print("Dice Throw :", score)
    prev = playerpos
    playerposition = game_board(playerpos, score)

    if playerposition > 30:
        playerposition = prev

    print("Player Position:", playerposition)
    print("   ")
    return playerposition


if __name__ == '__main__':
    print("Game Start")
    a = 0  # PLAYER 1
    b = 0  # PLAYER 2

    print("Player 1 = f")
    print("Player 2 = j")

    while a != 30 or b != 30:  # while True:  can also be written ...jab tak break na bol de True raihne  do
        key = input("Enter a key : ")
        if key == 'f':
            print("CHANCE OF A")
            a = game_play(a)
            if a == 30:
                print("Player A Winner")
                break

        elif key == 'j':
            print("CHANCE OF B")
            b = game_play(b)
            if b == 30:
                print("Player B Winner")
                break
        else:
            print("Enter correct key to throw a dice")
