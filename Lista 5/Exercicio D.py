cnt = 0
for num in range(18644, 33087+1):
    if "2" in str(num) and not "7" in str(num):
        cnt += 1
print(cnt)