def  bin_search(a,v,l,r):
    if r>=l:
        mid=l+r//2
        if v==a[mid]:
            return True
        elif v<a[mid]:
            return bin_search(a,v,l,mid-1)
        else:
            return bin_search(a,v,mid+1,r)
    else:
        return False
if __name__ == '__main__':
    a=[1,2,3,4,5,6]
    v=6
    x=bin_search(a,v,0,len(a)-1)
    if x=='True':
        print('Element is present in list')
    else:
        print('Element is not present in the list')
