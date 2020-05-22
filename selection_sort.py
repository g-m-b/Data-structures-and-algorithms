def select_sort(a):
    for i in range(len(a)):
        min_pos=i
        for j in range(i,len(a)):
            if a[j]<a[min_pos]:
                min_pos=j
            a[i],a[min_pos]=a[min_pos],a[i]
if __name__ == '__main__':
    a=[10,6,5,4,3,2]
    select_sort(a)
    for i in range(len(a)):
        print(a[i])
