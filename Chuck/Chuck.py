data = ["100000"]
k = int(data[0])

S = ""

for i in range(1, k+1):
    if i % 4 == 0:
        s = str(i)
    elif i % 2 == 1:
        s = str(i) + "2"
    else:
        s = str(i) + "0"
    
    S += s
    # print(i, s)

print(S[k-1])