
n = int(input())

photos = []

for i in range(n):
    tupla = []
    inpt = input().split()

    tupla.append(1 if inpt[0] == 'H' else 0)

    for j in range(2, len(inpt)):
        tupla.append(inpt[j])

    photos.append(tuple(tupla))
