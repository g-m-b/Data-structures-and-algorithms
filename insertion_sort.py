def insertion_sort(a):
    for i in range(len(a)):
        pos=i
        while (pos>0 and a[pos]<a[pos-1]):
            a[pos],a[pos-1]=a[pos-1],a[pos]
            pos=pos-1
if __name__ == '__main__':
    a=[10,5,4,7,8]
    insertion_sort(a)
    for i in range(len(a)):
        print(a[i])
