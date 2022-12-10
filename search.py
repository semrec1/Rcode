#linear search
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
list=[1,2,3,4,5,6,7,8,9,10]
target=5

#binary search 
def binary_search(list, target):
    first = 0
    last = len(list)-1
    while first<=last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
list=[1,2,3,4,5,6,7,8,9,10]
target=5
