num = int(input("Insira o número a ser decomposto: "))

def Primo(n):
    for x in range(2, n):
        if n % x == 0:
            return 0
        x += 1
    return 1

if not Primo(num):
    msg = f"{num} = "
    res = num
    
    x = 2
    while res > 1:
        if Primo(x) and res % x == 0:
            msg += f"{x}"
            res /= x
            if res > 1:
                msg += " * "
            x = 2
        else:
            x += 1
    print(msg)
else:
    print(f"{num} é primo")
