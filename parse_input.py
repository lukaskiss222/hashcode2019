def load():
    n = int(input())

    photos = []

    for i in range(n):
        tupla = []
        inpt = input().split()

        tupla.append(0 if inpt[0] == 'H' else 1)

        temp = []
        for j in range(2, len(inpt)):
            temp.append(inpt[j])

        tupla.append(temp)

        photos.append(tuple(tupla))
    return photos
