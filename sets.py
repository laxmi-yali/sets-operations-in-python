
# Sets Homework
set1 = {"apple","banana","mango","orange","mango"}
set2 = {"grapes","chikku","lemon","mango"}

print(type(set1))

print(set1 | set2) # Union operation (combines all elements from both sets without duplicates)
print(set1 & set2) # Intersection (returns only the common elements)
print(set1 - set2) # Difference (Returns elements present in the first set but not in the second)
print(set1 ^ set2) # Symmetric Difference (Returns elements that are in either set,but not in both)
print(len(set1))

set1.add("dates") # Add an element
print(set1)

set1.discard("mango") #  Discard an element (Removes an element if it exists. No error occurs if it doesn't exist)
print(set1)

set1.discard("pinaple")
print(set1)

set1.remove("banana") # Remove an element
print(set1)

print("orange" in set1) # check membership
print("mango" not in set2)

set1.pop() # remove a random element from the set
print(set1)

set1.clear() # removes all elements
print(set1)


set3 = {"rohan",}

print(set3)

empty_set = set()
print(empty_set)

# ==== 1. Problem =====

python_students = {"Asha", "Ravi", "Kiran"}
java_students = {"Ravi", "Kiran","Priya"}

print(python_students | java_students)
print(python_students & java_students)
print(python_students - java_students)
print(python_students ^ java_students)