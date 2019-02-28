import numpy as np
import scoring
import parse_input

data = parse_input.load()

data.sort(key=lambda x: len(x.tags))

best = data[:10]
N = len(best)
M = len(data)

res = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        if i != j:
            res[i,j] = scoring.evaluate([(i,), (j,)], data)

print(res)
