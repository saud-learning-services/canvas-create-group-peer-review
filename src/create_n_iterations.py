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
    '''Given an original list of elements, creates n new orders where no nth element in the new lists matches that element in another. n must be lower than the number of elements in the originalList.

    Parameters:
    myList (list): any list of any length
    n (int): the number of unique non-matching orders for the list

    Returns:
    a dictionary with list{n-1} and originalList
    {'list0': ['j', 'k', 'i'],
    'list1': ['k', 'i', 'j'],
    'originalList': ['i', 'j', 'k']}
    '''

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

                evaluation_dicts = []
                for i in zip(*listOfLists):
                    j = list(i)
                    first = j[0]
                    rest = j[1:]

                    new_dict = {first: rest} 
                    evaluation_dicts.append(new_dict)
                
                return(listDict, evaluation_dicts)
                break   