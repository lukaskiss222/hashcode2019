import numba
def get_tags(index, photos):
    if len(index) == 1:
        return photos[index[0]].tags
    return photos[index[0]].tags.union(photos[index[1]].tags)


# slides is list of tuples [(i1, i2,), (i3,), ...]
# photos is list of photos
@numba.jit
def evaluate(indices, photos):
    score = 0
    for i in range(1, len(indices)):
        slide1 = get_tags(indices[i-1], photos)
        slide2 = get_tags(indices[i], photos)

        score += min(
            len(slide1.intersection(slide2)),
            len(slide1.difference(slide2)),
            len(slide2.difference(slide1))
        )
    return score


if __name__ == "__main__":
    from photo import Photo
    print(
        evaluate([[0], [3], [1, 2]], [
             Photo(0, 0, ['cat', 'beach', 'sun']),
             Photo(1, 1, ['selfie', 'smile']),
             Photo(2, 1, ['garden', 'selfie']),
             Photo(3, 0, ['garden', 'cat'])
        ])
    )
