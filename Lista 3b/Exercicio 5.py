num = input("Digite o número: ")

out = ""
count = len(num) - 1
while count >= 0:
    out += num[count]
    count -= 1

print(out)
