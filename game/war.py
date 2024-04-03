from random import shuffle as shf
from random import randbytes
from time import sleep
fulldeck = list([])
win=0
for i in range(1,53,1):
    fulldeck.append(i)
def shuffledeck():
    shf(fulldeck)
    p = fulldeck[:26]
    b = fulldeck[26:]
    return p, b
def cardpull():
    print("\n\nPlayer has " + str(len(ply)) + " cards left")
    print("The house has " + str(len(bot)) + " cards left")
    pc = ply.pop()
    bc = bot.pop()
    print(pc, bc)
    print("Player: " + str(pc%13))
    print("House: " + str(bc%13))
    if pc % 13 > bc % 13:
        print("Player wins")
        if randbytes(1) == 1:
            ply.insert(0, pc)
            ply.insert(0, bc)
        else:
            ply.insert(0, bc)
            ply.insert(0, pc)
    elif bc % 13 > pc % 13:
        print("House wins the battle")
        if randbytes(1) == 1:
            bot.insert(0, pc)
            bot.insert(0, bc)
        else:
            bot.insert(0, bc)
            bot.insert(0, pc)
    else:
        bot.insert(0, pc)
        ply.insert(0, bc)
ply, bot = shuffledeck()
print(ply, bot)
while win == 0:
    sleep(.05)
    if len(ply) > 0 and len(bot) > 0:
        cardpull()
    elif len(ply) == 0:
        print("lose")
        win = -1
    elif len(bot) == 0:
        print("win")
        win = 1
        