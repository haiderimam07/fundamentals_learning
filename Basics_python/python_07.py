# 2d lists  and nested loops 

lists=[
    [1,2,2,4],
    [4,5,6,7],
    [2,4,5,7]
]
# print(len(lists[0]))
for i in range(len(lists)):
    for j in range(len(lists[0])):
        print(f"{lists[i][j]} : this")