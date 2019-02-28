from .photo import Photo


def load():
    n = int(input())

    photos = []

    for i in range(n):
        inpt = input().split()
        orient = 1 if inpt[0] == 'H' else 0
        photos.append(Photo(i, orient, inpt[2:]))
    return photos
