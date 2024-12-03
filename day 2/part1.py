

def getReports():
    with open(r'day 2\puzzle_input.txt', "r") as f:
        reports = []
        for line in f.readlines():
            line = line.removesuffix("\n")
            line = line.split(" ")
            reports.append(line)

    return reports


def checkDifference(report):
    difference_list = []
    
    for x in range(len(report)-1):
        if x!=len(report):
            difference = int(report[x]) - int(report[x+1])
            difference_list.append(difference)

    return difference_list


def checkSafe(report):

    dList = checkDifference(report)

    if all(diff > 0 and diff <= 3 for diff in dList):
        return True
    
    elif all(diff < 0 and diff >= -3 for diff in dList):
        return True
    
    else:
        return False
    
def main():
    reports = getReports()
    safe_count = 0
    
    for report in reports:
        print(reports.index(report) + 1, " - ", report, checkSafe(report))
        if checkSafe(report):
            safe_count+=1
    
    return safe_count

if __name__ == "__main__":
    main()