a1 = int(input())
a2 = int(input())
n1 = a1
while (a1 != 0) and (a2 != 0):
    if a1 > a2:
        a1 %= a2
    else:
        a2 %= a1
print(a1 + a2)