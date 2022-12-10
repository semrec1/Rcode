#insertion sort
def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        nxt_element = list[i]
        # Compare the current element with next one
        while (list[j] > nxt_element) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = nxt_element
list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list)
