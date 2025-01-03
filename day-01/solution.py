

with open('input.txt') as file:
    u,v = zip(*[line.rstrip().split("   ") for line in file]) 

# part 1
sum([abs(x-y) for x,y in zip(*[sorted([int(j) for j in w]) for w in (u,v)])])

# part 2
# not efficient, but fast enough in this case
sum([int(x)*sum([x == i for i in v]) for x in u])
