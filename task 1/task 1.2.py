
'''def sorting_gadgets(l):
    l.sort()
    l.sort(key=lambda x: int(x[1]), reverse=True)
    return [(i[0], int(i[1]), True if int(i[1]) else False) for i in l]'''  #function that returns list of tuples

n = int(input('Enter number of gadgets: '))
print('Enter gadget names and quantities (each gadget on a new line)')
gadgets = [input().split() for _ in range(n)]
gadgets.sort()                                                              #sorting alphabetically then by quantity
[print(i[0]) for i in sorted(gadgets, key=lambda x:int(x[1]), reverse=True)]    #only printing gadget names

#print(sorting_gadgets(gadgets))