def postup_debyl(n: int, k: int):
    place_v_depart = {i: int(num) for i, num in enumerate(input().split(), 1)}
    
    students = []
    
    for i in range(n):
        student = [int(num) for num in input().split()]
        student.pop(1)
        student.insert(1, i)
        students.append(student)
    
    students.sort()
    
    for student in students:
        for depart in student[2:]:
            if place_v_depart[depart] > 0:
                place_v_depart[depart] -= 1
                student.append(depart)
                break
        else:
            student.append(-1)
    
    students.sort(key=lambda stud: stud[1])
    return ' '.join([str(stud[-1]) for stud in students])
    
        

print(postup_debyl(*[int(num) for num in input().split()]))
