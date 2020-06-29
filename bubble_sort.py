'''
The def takes the array, the elements are swapped in place.
'''
def bubble_sort(arr):
    arr_len=len(arr)
    for i in range(arr_len):
        for j in range(0,arr_len-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
if __name__ == '__main__':
    a=[1,5,3,2,7,9,10]
    bubble_sort(a)
    for i in range(len(a)):
        print(a[i])
