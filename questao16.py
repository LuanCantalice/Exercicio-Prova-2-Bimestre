n = 0
n1 = 1
n2 = 1
n3 = 1
print(n)
print(n1)

while (n1 < 501):
    print(n1)
    n1 = n2 + n3
    n2 = n3
    n3 = n1
print(n1)
