

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    p1 = patient_medical_speciality_list.count('P')
    p2 = patient_medical_speciality_list.count('O')
    p3 = patient_medical_speciality_list.count('E')
    s = ''
    if(p1>p2 and p1>p3):
        s = medical_speciality['P']
    elif(p2>p3 and p2>p1):
        s = medical_speciality['O']
    else:
        s = medical_speciality['E']
    return s

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)