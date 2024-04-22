
print("yeah yeah yeah menu menu menu baby\nencode stuff - 1\n")

def encode(n):
    binout = ""
    n = inp
    while n > 0:
        bindig = n%2
        binout = str(bindig) + binout
        n = n//2
    return binout
            
            
while True:
    inp = input("Number?\n")
    inp = int(inp)
    output = encode(inp)
    print(output)