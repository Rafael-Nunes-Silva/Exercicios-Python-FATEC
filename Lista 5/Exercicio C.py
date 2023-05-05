cnt = 0
for i in range(1067, 3627+1):
    if i % 2 == 0 and i % 7 == 0:
        cnt += 1
print(cnt)