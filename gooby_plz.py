import numpy as np
import scoring
import parse_input

data = parse_input.load()

data.sort(key=lambda x: len(x.tags))
ids = [x.id for x in data]
print(len(ids))
for i in ids:
    print(i)
