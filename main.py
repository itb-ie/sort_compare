# write a quicksort program
import random # needed to generate random array
import datetime
import sys
sys.setrecursionlimit(1000001)

def quick_sort(array, lo, hi):
    if (lo < hi): # will end when low == hi
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p+1, hi)

def partition(a, lo, hi):
    pivot = a[hi-1]
    i = lo
    for j in range (lo, hi-1):
        if (a[j] < pivot):
            a[i], a[j] = a[j], a[i]
            i+=1
    a[i], a[hi-1] = a[hi-1], a[i]
    return i

def bubble_sort(a, hi):
    found = True
    while (found):
        found = False
        for i in range (0, hi-1):
            if (a[i] > a[i+1]):
                found = True
                a[i], a[i+1] = a[i+1], a[i];


hi = int(input("cat de lng sa fie sirul?"))
a=[]
for i in range (0, hi):
    a.append(random.randint(1, 100))
b = a.copy()
#print("am generat sirul")
#print("am generat sirul")
#for i in range (0, hi):
#    print(a[i], end=" ")
start = datetime.datetime.now()
quick_sort(a, 0, hi)
print("the time was: ", datetime.datetime.now() - start)
#print("\nam sirul ")
#for i in range(0, hi):
#    print(a[i], end=" ")
start = datetime.datetime.now()
bubble_sort(b, hi)
print("the time was: ", datetime.datetime.now() - start)
#print("\nam sirul ")
#for i in range(0, hi):
#    print(b[i], end=" ")

