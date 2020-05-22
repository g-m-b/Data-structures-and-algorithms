def linearsearch(a,n,v):
    for i in range(0,n):
        if a[i]==v:
            return True
    return False

if __name__ == '__main__':

    a=[10,54,89,3,2]
    n=len(a)
    v=3
    x=linearsearch(a,n,v)
    if x=='True':
        print('Number is present in the list')
    else:
        print('Number is not in list')
