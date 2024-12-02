from part1 import getLists

def getSimilarity():

    list1, list2 = getLists()
    
    similarity_list = []
    
    for x in list1:
        count = 0
        for y in list2:
            if x==y:
                count+=1
        similarity = x * count
        similarity_list.append(similarity)

    sumOfSimilarities = sum(similarity_list)
    print(sumOfSimilarities)

getSimilarity()