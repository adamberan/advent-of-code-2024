
with open('input.txt') as file:
    reports = [line.rstrip().split(" ") for line in file]

# part 1:
def safe(report):
    diff = [int(v)-int(u) for u,v in zip(report, report[1:])]
    return max([abs(d) for d in diff]) <= 3 and (max(diff) < 0 or min(diff) > 0)
sum([safe(report) for report in reports])

# part 2:  
def damper_safe(report):
    # k ~ dampered element
    return any([safe([x for i,x in enumerate(report) if i != k]) for k in range(len(report))])
sum([damper_safe(report) for report in reports])