def getSecondLowest(lst_of_students,sorting_key):
    lowest = min(lst_of_students,key=lambda x: x[sorting_key-1])
    sec_lst = [subl for subl in lst_of_students if subl[1] != lowest[1]]
    sec_lowest_elements = sorted([subl for subl in sec_lst if subl[1] == sec_lst[0][1]])
    return sec_lowest_elements

if __name__ == "__main__":
    lst_of_students = list()

    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        lst_of_students.append([name,score])

    output = getSecondLowest(lst_of_students,2)

    if len(output) > 1:
        for ele in output:
            print(ele[0])
    else:
        print(output[0][0])            