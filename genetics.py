import random
import matplotlib.pyplot as plt
from statistics import mean 
import pandas as pd

def punnet(x, y):
    if x == 2 and y == 2: 
        z = 2
    elif (x == 2 and y == 1) or (x == 1 and y == 2):
        h = random.randint(0,100)
        if h < 50:
            z = 1
        elif h >= 50:
            z = 2
    elif (x == 0 and y == 1) or (x == 1 and y == 0):
        h = random.randint(0,100)
        if h < 50:
            z = 0
        elif h >= 50:
            z = 1
    elif x == 1 and y == 1:
        h = random.randint(0,100)
        if h <= 25:
            z = 0
        elif h >= 75:
            z = 2
        else:
            z = 1
    elif (x == 2 and y == 0) or (x == 0 and y == 2):
        z = 1
    elif x == 0 and y == 0:
        z = 0
    return z
 
 #the autism gene is recessive and present in 1 in 100 on average
b = [2]*1 + [1]*2 + [0]*1

pop = 3000

a=[]
for i in range(pop):    
    a.append(random.choice(b)) # so a is our base population

x = a.count(0)


c = []
q = []
u = []
v = []

q.append(a.count(0))
for j in range(200):
    for i in range(12):
        while len(a) > 0:
            d = a.pop()
            e = a.pop()
            k = punnet(d,e)
            j = punnet(d,e)
            c.append(k)
            c.append(j) ## c is our new population
        q.append(c.count(0)) ## q is the number of zeros in C
        random.shuffle(c)
        a = c.copy()
        c.clear()
    a = []
    for i in range(pop):    
        a.append(random.choice(b)) # so a is our base population
    v.append(q[-1]) ## v is the final number of zeros in the first run
    q[:] = [x / pop for x in q]
    u.append(q)
    q = []

print(v)
print(mean(v)/pop)



my_df = pd.DataFrame(u)
my_df.to_csv('3000popR.csv', index=False, header=False)