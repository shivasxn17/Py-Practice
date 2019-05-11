if __name__ == "__main__":
    students_marks_dict = {}

    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        
        if score in students_marks_dict:
            students_marks_dict[score].append(name)
        else:
            students_marks_dict[score] = [name]

    output = sorted(students_marks_dict[list(sorted(students_marks_dict))[1]])
   
    if len(output) > 1:
        for ele in output:
            print(ele)
    else:
        print(output[0])            