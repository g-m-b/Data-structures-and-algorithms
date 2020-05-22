def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
if __name__ == '__main__':
    a=[1,5,3,2,7,9,10]
    bubble_sort(a)
    for i in range(len(a)):
        print(a[i])
