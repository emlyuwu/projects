
btset = int(input("What bitset?\n"))
btrng = 2**btset

chce = int(input(f"Number between 1 and {btrng}:\n"))
inpi = 1
while inpi == 1:
    if chce > btrng or chce < 1:
        print("you are stupid")
    else:
        inpi = 0

brt = 1
mxx = btrng
mnm = 0
while brt == 1:
    gss = ((mxx-mnm)/2)+mnm
    print(f"\nGuessing {gss}")
    if chce > gss:
        print("Higher")
        mnm = gss
    elif chce < gss:
        print("Lower")
        mxx = gss
    elif gss == chce:
        print(f"Number is {gss}")
        brt = 0