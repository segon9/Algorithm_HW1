import sys

N = int(input())
list1 = set(map(int, sys.stdin.readline().split()))
M = int(input())
list2 = list(map(int, sys.stdin.readline().split()))

for i in list2 :
    if i in list1 :
        print("1")
    else :
        print("0")


'''
def binary_search(arr, num, start, end) :
    if(start >= end) :
        return 0

    mid = (start + end) // 2
    if(arr[mid] < num) :
        return binary_search(arr, num, mid + 1, end)
    elif(arr[mid] > num) :
        return binary_search(arr, num, start, mid-1)

    else :
        return 1
'''