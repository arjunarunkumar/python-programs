def quicksort(array):
    quicksorthelper(array,0,len(array)-1)

def quicksorthelper(array,first,last):
    if first<last:
        mid=partition(array, first , last)

        quicksorthelper(array, first , mid-1)
        quicksorthelper(array, mid+1 , last)

def partition(array, first , last):
    pivot = array[first]
    leftpoint = first + 1
    rightpoint = last

    done = False
    while not done:
        while leftpoint <= rightpoint and array[leftpoint] <=pivot :
            leftpoint = leftpoint + 1

        while array[rightpoint] >= pivot and rightpoint >=leftpoint:
            rightpoint = rightpoint - 1

        if rightpoint < leftpoint:
            done = True
        else:
            temp=array[leftpoint]
            array[leftpoint] = array[rightpoint]
            array[rightpoint] = temp

    temp=array[first]
    array[first] = array[rightpoint] 
    array[rightpoint] = temp

    return rightpoint

array = [10 ,11 , 14 , 9 , 4, 2, 7]
quicksort(array)
print(array)

    
