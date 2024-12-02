def getLists():
    with open(r'day 1\puzzle_input.txt', "r") as file:
        puzzle_input = []
        for line in file.readlines():
            line = line.removesuffix('\n')
            puzzle_input.append(line)

    split_list = []
    list1 = []
    list2 = []


    for line in puzzle_input:
        line = line.split(" ")
        split_list.append(line)

    for list in split_list:
        list1.append(int(list[0]))
        list2.append(int(list[3]))
    
    
    return list1, list2

def main():

    list1, list2 = getLists()
    difference_list = []

    for x in range(len(list1)):
        smallest1 = min(list1)
        smallest2 = min(list2)

        if smallest1 > smallest2:

            difference = smallest1-smallest2
        else:

            difference = smallest2-smallest1

        difference_list.append(difference)
        list1.remove(smallest1)
        list2.remove(smallest2)

    print(sum(difference_list))
    return sum(difference_list)
    


if __name__ == "__main__":
    main()