def bubblesort(listofnumbers):
    moreswaps = True
    while moreswaps:
        moreswaps = False
        for element in range(len(listofnumbers)-1):
            if listofnumbers[element] > listofnumbers[element+1]:
                moreswaps=True
                temp = listofnumbers[element]
                listofnumbers[element] = listofnumbers[element + 1]
                listofnumbers[element+1] = temp
    return listofnumbers

def sortelements():
    mylist=[2,1,4,5,6,2,3,1,2,4,5,6,11,9,7]
    sortedlist=bubblesort(mylist)
    print(sortedlist)
