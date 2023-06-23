data = ['mdmsafmammfds']

S = data[0]
# print(S)
S_dict = {}
outlier = 0

for c in S:
    if c not in S_dict.keys():
        S_dict[c] = 1
        outlier -= 1
    else:
        S_dict[c] += 1
        if S_dict[c] % 2 != 0:
            outlier -= 1
        else:
            outlier += 1

print(outlier)
if outlier == 0 or outlier == -1:
    print("yes")
else:
    print("no")