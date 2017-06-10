def binarysearch(searchitem,dataset):
    start = 0
    end = len(dataset)-1
    found = False
    while(start<=end and not found):
        mid = (start+end)//2
        if(dataset[mid] == searchitem):
            found = True
        elif (dataset[mid] < searchitem):
            start = mid + 1
        else:
            end = mid -1
    return found


list_of_numbers = [1,2,3,4,5,6,12,13,14,15,17]
item = int(input("enter the item to be searched"))
isitfound = binarysearch(item, list_of_numbers)
#if isitfound:
#    print("item present")
#else:
#    print("item not found")
print(len(list_of_numbers))
print(list_of_numbers)
if(isitfound):
    print(item)
else:
    print("not found")


    
print(list_of_numbers[2])
