from parse_input import load
import random
from scoring import get_slides_score, evaluate


def greedy(ph):
    verticals = 0
    for p in ph:
        p.taken = 0
        if p.orient == 0:
            verticals += 1

    index = 0
    while ph[index].orient != 1:
        index = random.randint(0, len(ph)-1)

    indices = [[index]]
    ph[index].taken = 1

    prev = indices[0]
    for _ in range(0, min(200, len(ph)-verticals-1)):
        best_i = -1
        best_score = -1
        for i, p in enumerate(ph):
            # no vertical images for now
            if p.taken == 1 or p.orient == 0:
                continue
            
            score = get_slides_score(ph[prev[0]].tags, p.tags)
            if score > best_score:
                best_score = score
                best_i = i
        
        ph[best_i].taken = 1
        indices.append([best_i])
        prev = indices[-1]

    for i, p in enumerate(ph):
        if p.taken == 0 and p.orient == 1:
            indices.append([i])

    print(len(indices))
    for ind in indices:
        print(ind[0])

    #print(evaluate(indices, ph))


if __name__ == "__main__":
    photos = load()
    greedy(photos)
