n1 = 0
n2 = 1
n3 = 1
n4 = 1
print(n1)
print(n2)

while (n2 < 501):
    print(n2)
    n2 = n3 + n4
    n3 = n4
    n4 = n2
print(n2)


