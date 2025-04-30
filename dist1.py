#Manageadictionary to store student names and their corresponding grades. Implement
 #functionality to add, update, delete, and display the grades.
student={
     "name":"66",
     "grade":"50",
       }
student["name2"]=66
print(student)
student.update({"collage":"dkte"})
print(student)
student.update({"name":"csg"})
print(student)
del student["collage"]
print(student)
student["name2"]-=6
#student["name"]-=6
print(student)
print(student)
#A)Create a list and perform basic operations like accessing, modifying, and adding/removing
# elements. B) Use slicing to extract a portion of a list.
 ##e) Reverse the order of elements in a list. F) Work with nested lists (lists within lists)
list=[55,56,8,98,5]
print(" elemenr",list[2])
list[2]=5
print(" elemenr",list)
list.append(99)
print(" elemenr",list)
list.remove(5)
print(" elemenr",list)
print(list[1:5])
print(list[-1:])
print(list.sort())
print(list)
list.sort(reverse=True)
print(list)
n=[[1,2,3],[4,5,6],[6,7,8]]
print(n)
n[2][1]=55
print(n)