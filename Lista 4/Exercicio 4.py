texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based onmutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, andwhatever your background, we welcome you.".lower().replace('.', '').replace(',', '').split(" ")

lista = []

for x in texto:
    for c in "python":
        if x[0] == c or x[len(x)-1] == c:
            lista.append(x)

print(lista)
