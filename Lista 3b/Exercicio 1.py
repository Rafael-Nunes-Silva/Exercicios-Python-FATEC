n = int(input("Insira o número: "))

count = 1

msg = ""

while count * (count + 1) * (count + 2) != n:
    count += 1
    msg = f"{n} é triangular, pois {count}.{count+1}.{count+2} = {n}"
    if(count >= n):
        msg = f"{n} não é triangular"
        break

print(msg)
