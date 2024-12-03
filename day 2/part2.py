from part1 import checkDifference, checkSafe, getReports
    
def removeLevelsAndCheck(report : list):
    
    for x in range(len(report)):
        
        indexes = []

        for y in range(len(report)):
            if y!=x:
                indexes.append(y)
        
        new_report = [report[x] for x in indexes]
        if checkSafe(new_report):
            return True

def main():
    reports = getReports()
    safe_count = 0
    for report in reports:
        if checkSafe(report):
            safe_count+=1
        else:
            if removeLevelsAndCheck(report):
                safe_count+=1

    print(safe_count)

main()
        