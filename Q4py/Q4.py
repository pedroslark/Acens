A = []
B = []
V = []

while len(A) < 10:
    i = input('Digite um numero inteiro, entre 1 e 100, para o vetor A: ')
    if i >= 1 and i <= 100:
        A.append(i)

while len(B) < 10:
    i = input('Digite um numero inteiro, entre 1 e 100, para o vetor B: ')
    if i >= 1 and i <= 100:
        B.append (i)

for x in range (len(A) ):
    V.append (A[x])
    V.append (B[x])

print V

#GG easy :)

