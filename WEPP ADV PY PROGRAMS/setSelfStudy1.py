# 1) Managing an Online Store Inventory Scenario:
# You manage an online store that sells various products. You need to keep track of which
# products are in stock and which are out of stock.

# Use Python sets to manage this inventory.

# Tasks:

# 1. Create a set in_stock containing the products 'laptop', 'mouse', 'keyboard', and 'monitor'.
# 2. Create another set out_of_stock containing 'printer' and 'webcam'.
# 3. A new shipment arrives, restocking the 'printer' and adding a new product 'tablet'.
# Update the in_stock set accordingly.
# 4. A customer reports that the last 'monitor' was sold. Move 'monitor' to the out_of_stock set.
# 5. Find out which products are either in stock or out of stock, but not both.
# 6. Calculate which products are still available for sale.
'''
in_stock = {'laptop', 'mouse', 'keyboard', 'monitor'}
out_of_stock = {'printer', 'webcam'}

new_shipment = {'printer', 'tablet'}
in_stock.update(new_shipment)

sold_product = 'monitor'
out_of_stock.add(sold_product)

common_products = in_stock.intersection(out_of_stock)

available_products = in_stock.difference(out_of_stock)

print("In Stock products are:", in_stock)
print("Out of Stock products are:", out_of_stock)
print("Common Products in 'in_stock' and 'out_of_stock':", common_products)
print("Available Products for the sale are:", available_products)

'''

# 2) Student Enrollment System Scenario:
# You are developing a student enrollment system for a university. The university offers
# courses in different subjects, and some students are enrolled in multiple courses.

# Tasks:

# 1. Create a set course_A containing students 'Alice', 'Bob', 'Charlie'.
# 2. Create another set course_B containing students 'Charlie', 'David', 'Eva'.
# 3. Find out which students are enrolled in both course_A and course_B.
# 4. List all students who are enrolled in either course_A or course_B.
# 5. Identify students who are enrolled in course_A but not in course_B.
# 6. Determine the students who are enrolled in only one course.
'''
# course_A = {'Alice', 'Bob', 'Charlie'}
# course_B = {'Charlie', 'David', 'Eva'}
# commonStudentsInAB = course_A.intersection(course_B)

# allEnrolledStudents = course_A.union(course_B)

# studentsEnrolledInAOnly = course_A.difference(course_B)

# studentsEnrolledInBOnly = course_B.symmetric_difference(course_A)

# print("Common Students in 'course_A' and 'course_B':", commonStudentsInAB)
# print("All Enrolled Students are:", allEnrolledStudents)
# print("Students Enrolled in 'course_A' only are:", studentsEnrolledInAOnly)
# print("Students Enrolled in 'course_B' only are:", studentsEnrolledInBOnly)

'''
# 3) Healthcare Appointment Management
# Scenario:
# You are building a healthcare appointment system where patients can have either
# scheduled or walk-in appointments.
# Tasks:
# 1. Create a set scheduled_appointments with patient names 'Anna', 'Bob', and
# 'Clara'.
# 2. Create another set walk_in_appointments with patient names 'Clara', 'David', and
# 'Eva'.
# 3. Identify patients who have both scheduled and walk-in appointments.
# 4. List all patients who have any type of appointment.
# 5. Determine which patients have only walk-in appointments.
# 6. Add a new patient 'Frank' to the walk-in appointments and remove 'Eva' from
# scheduled appointments (if present).

scheduled_appointments=set(('Anna', 'Bob','Clara'))
walk_in_appointments=set(('Clara', 'David','Eva'))
pWithBothAppointment=scheduled_appointments.intersection(walk_in_appointments)
print(f"Patients who have both type of appointments are:{pWithBothAppointment}")
allPatientsWithAnyAppo=scheduled_appointments.union(walk_in_appointments)
print(f"List of all the patients who have any type of appointments are: {allPatientsWithAnyAppo}")
pWithOnlyWalkAppo=walk_in_appointments.difference(scheduled_appointments)
print(f"List of all the patients who have only walk-in appointments are: {pWithOnlyWalkAppo}")
newPatient="Frank"
walk_in_appointments.add(newPatient)
print(f"After adding {newPatient} in the 'walk_in_appointments',the list is: {walk_in_appointments}")
if "Eva" in scheduled_appointments:
    scheduled_appointments.remove("Eva")

