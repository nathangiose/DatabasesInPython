import time
start=time.time()

Number = [42, 12, 13, 89, 63, 11]

def sortselection(lists):
    #count = 0
    for x in range(len(lists)):
        minimum = lists[x]
        for y in range(x, len(lists), 1):
            if lists[y] < minimum:
                #count = +1
                minimum = lists[y]
                lists[y], lists[x] = lists[x], lists[y]
       # print(x)
    #print(count)
    return(lists)

print(sortselection(Number))
end=time.time()
print(end-start)
