
def buuble_sort(a):
    n = len(a)

    swap = 1
    if swap:
        for j in range(n-1):
            swap = 0
            for i in range(n-j-1):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1],a[i]
                    swap = 1
    print(a)

a = [int(x) for x in input("Enter the array elements").split()]

buuble_sort(a)
#print(a)

