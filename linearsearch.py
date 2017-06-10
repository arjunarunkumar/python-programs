def linearsearch(item , itemlist):
    start = 0
    found = False
    while start < len(itemlist) and not found:
        if(itemlist[start] == item):
            found = True
        start = start + 1
    return found

shopcart = ["apple" , "mangoes", "grapes", " bananas"]
item = input("enter the item to be searched")
isitfound = linearsearch(item, shopcart)
if isitfound:
    print("item present")
else:
    print("item not found")

    
