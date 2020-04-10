# --------------
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# concatenation of two classes
new_class = class_1+class_2
print(new_class)
print('='*20)
# adding a new student to the new class
new_class.append('Peter Warden')
print(new_class)
print('='*20)
# correcting the wrong student enetry
new_class.remove('Carla Gentry')
print(new_class)


# --------------
# Code starts here
courses = {'Math':65,'English':70 , 'History':80,'French':70,'Science':60}
print(courses)
# total mark of Geoffrey Hinton
total = sum(courses.values())
print(total)
# percentage mark of Geoffrey Hinton
percentage = total/5
print(percentage,'%')
# Code ends here


# --------------
# Code starts here




mathematics ={'Geoffrey Hinton': 78,'Andrew Ng': 95,'Sebastian Raschka': 65,'Yoshua Benjio': 50,'Hilary Mason': 70,'Corinna Cortes': 66,'Peter Warden': 75}
# finding the topper in mathematics

topper = max(mathematics,key = mathematics.get)
print (topper)


# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name = topper.split()[0]
last_name = topper.split()[1]
full_name = last_name +' '+ first_name
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


