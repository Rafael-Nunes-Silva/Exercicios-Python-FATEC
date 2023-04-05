texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based onmutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, andwhatever your background, we welcome you.".lower().replace('.', ' ').replace(',', ' ').split(" ")

cnt = 0

def EstaEmPython(c):
    for h in "python":
        if h == c:
            return 1
    return 0

for x in texto:
    if len(x) < 4:
        continue
    for c in x:
        if EstaEmPython(c):
            cnt += 1
            break

print(cnt)
