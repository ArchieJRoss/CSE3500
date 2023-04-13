import heapq
#I used python because of this library which makes heap functions much easier to write.

def merge_sorted(list1, list2):
    #This line combines the two lists into one list, "biglist"
    biglist = list1 + list2
    #This line converts "biglist" into a heap
    heapq.heapify(biglist)

    #This line takes creates a new list where we can store the newly sorted items
    new_list = []

    #This portion starts a loop that will run until combined is empty and all elements have been transferred to the new list
    #We do so by appending the items in smallest items in the heap and then "popping" them from which removes them from the heap
    #Written in the same line we append the smallest item to the new list and remove it from the heap.
    while biglist:
        new_list.append(heapq.heappop(biglist))

    #This is just the return statement returning the final sorted list.
    return print(new_list)

if __name__ == "__main__":
    list1 = [1,3,5,6,9]
    list2 = [2,4,7,8]
    merge_sorted(list1,list2)