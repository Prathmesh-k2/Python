student={
    "name":"abc",
    "age":100,
    "collage":"xyz",
}
print(student)
print(student["age"])
student[ "age"]=10
print(student)
print(student.keys())
print(len(student))
print(list(student.keys()))
print(student.values())
print(student.items())
student.update({"city":"uk"})
print(student)