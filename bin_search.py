def  bin_search(input_list,value,left,right):
    """
    recursive implementation of binary search
    input_params:
       input_list, value to search, left index, right index
    """
    if right>=left:
        mid=(left+right)//2
        if value==input_list[mid]:
            return True
        elif value<input_list[mid]:
            return bin_search(input_list,value,left,mid-1)
        else:
            return bin_search(input_list,value,mid+1,right)
    else:
        return False
if __name__ == '__main__':
    input_list=[1,2,3,4,5,6]
    value=6
    if bin_search(input_list,value,0,len(input_list)-1):
        print('Element is present in list')
    else:
        print('Element is not present in the list')
