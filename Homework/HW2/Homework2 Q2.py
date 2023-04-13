import time

listfile1 = "listNumbers-10.txt"
listfile2 = "listNumbers-100.txt"
listfile3 = "listNumbers-1000.txt"
listfile4 = "listNumbers-10000.txt"
listfile5 = "listNumbers-100000.txt"
listfile6 = "listNumbers-1000000.txt"
files = [listfile1, listfile2, listfile3, listfile4, listfile5, listfile6]

targetfile1 = "listNumbers-10-nsol.txt"
targetfile2 = "listNumbers-100-nsol.txt"
targetfile3 = "listNumbers-1000-nsol.txt"
targetfile4 = "listNumbers-10000-nsol.txt"
targetfile5 = "listNumbers-100000-nsol.txt"
targetfile6 = "listNumbers-1000000-nsol.txt"
targets = [targetfile1, targetfile2, targetfile3, targetfile4, targetfile5, targetfile6]

def brute_force(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return (lst[i], lst[j])
    return "There are no pairs that sum equal the given target."

def binary_search(lst, target):
    lst.sort()
    for i in range(len(lst)):
        counterpart = target - lst[i]
        start = i + 1
        end = len(lst) - 1
        while start <= end:
            middle = (start + end) // 2
            if lst[middle] == counterpart:
                return (lst[i], counterpart)
            elif lst[middle] < counterpart:
                start = middle + 1
            else:
                end = middle - 1
    return "There are no pairs that sum equal the given target."

binary = []
#brute = []

for file in files:
    with open(file, encoding="utf8") as f:
        file_contents = [int(line.strip()) for line in f]
    print("Currently working in:", file)
    for target in targets:
        with open(target, encoding="utf8") as f:
            target_contents = [int(line.strip()) for line in f]
        for t in target_contents:
            #start = time.perf_counter()
            #result_brute = brute_force(file_contents, t)
            #end = time.perf_counter()
            #brute.append(end-start)

            start = time.perf_counter()
            result_binary = binary_search(file_contents, t)
            end = time.perf_counter()
            binary.append(end-start)
    #averagebrute = sum(brute)/len(brute) if len(brute) > 0 else 0
    averagebinary = sum(binary)/len(binary) if len(binary) > 0 else 0
    #print("The average speed of the brute function for this file is:", averagebrute)
    print("The average speed of the binary function for this file is:", averagebinary)
    #brute.clear()
    binary.clear()



            
