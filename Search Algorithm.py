import numpy as np
import random
l = list(range(100))
random.shuffle(l)

found = False
for val in l:
    if val==2:
        print("found")
        found = True
        break;
if found== False:
    print("Not found")
