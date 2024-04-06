# student = {"name":"Rakesh",
#            "Batch":"Data Analytics",
#            "city":"Ujjain",
#            "Phone":"1234567"}
# std_list = []

# for data in student.items():
#     std_list.append(data[1])

# print(std_list)



# student.pop("city")
# student.update({"Phone":123456})
# student.update({None:"None Valu2e"})
# student.update({None:"None Valu3e"})
# print(student.get("Phone"))
# print(student)

# exist

student1 = {"name":"Rakesh","Batch":"Data Analytics","city":"Ujjain","Phone":"1234567"}
student2 = {"name":"Mukesh","Batch":"Data Analytics","city":"Indore","Phone":"1234567"}
student3 = {"name":"Anil","Batch":"Data Analytics","city":"Bhopal","Phone":"1234567"}
student4 = {"name":"Aman","Batch":"Data Analytics","city":"Jabalpur","Phone":"1234567"}
student5 = {"name":"Suresh","Batch":"Data Analytics","city":"Satna","Phone":"1234567"}

students = dict()
for data in (student1,student2,student3,student4,student5):
    students.update(data)
print(students)

