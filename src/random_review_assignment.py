import random

def __match_nth_element(manyLists, n):
    elementList = []
    for i in manyLists:
        elementList.append(i[n])
    #print(elementList)
    return(len(elementList) == len(set(elementList)))

def _get_nth_element(manyLists, n):
    elementList = []
    for i in manyLists:
        elementList.append(i[n])
    #print(elementList)
    return(elementList)

def _compare_all_elements(manyLists, listLength):
    elementCompare = []
    for i in range(listLength):
        elementCompare.append(__match_nth_element(manyLists, i))
    return(all(elementCompare))

def _create_n_lists(originalList, n):
    
    a = {}
    
    for i in range(n):
        key = f"list{i}"
        value = random.sample(originalList, len(originalList))
        a[key] = value
        
    a['originalList'] = originalList
    return(a)
    
def create_n_iterations(myList, n):
    k = len(myList)
    
    if (n >= k):
        print("n must be less than the length of the list")

    else:
   
        manyLists = []
        manyLists.append(myList)
        i = 0
        

        while True:
            listDict = _create_n_lists(myList, n)
            listOfLists = listDict.values()
            #print(f"next list: {test}")
            i +=1


            if _compare_all_elements(listOfLists, k):
                print(f"{i}: {listOfLists}")
                
                return(listDict)
                break   