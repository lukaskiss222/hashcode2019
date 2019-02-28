

def get_tags(slide):
    if slide[0] == 0:
        return slide[1][0]
    return slide[1][0].intersection(slide[1][1])


# list of slides
# each element is (1/0, (tags1, tags2)) -- tags2 are optional
# tags1/tags2 are frozensets
def evaluate(slides):
    score = 0
    for i in range(1, len(slides)):
        slide1 = get_tags(slides[i])
        slide2 = get_tags(slides[i+1])

        score += min(
            len(slide1.intersection(slide2)),
            len(slide1.difference(slide2)),
            len(slide2.difference(slide1))
        )
    return score
