my_name = input("name: ")
my_age = input ("age: ")
print(f"My name is {my_name} and I am {my_age} years old")
first_number =int(input("first number: "))
second_number = int(input("second number: "))
operation = input("operation: ")
if operation == "+":
   print(first_number + second_number)
elif operation == "-":
   print(first_number - second_number)
elif operation == "*":
   print(first_number * second_number)
elif operation == "/":
   print(first_number / second_number)
else: 
   print("operation is not valid")

bus_capacity = 20
people_inbus = int(input("people in bus "))
people_in_the_line = int(input("people in line"))
empty_seats = bus_capacity - people_inbus

if empty_seats > people_in_the_line :
      print(f"there is{empty_seats} empty seats")
elif empty_seats <= people_in_the_line :
      print("the bus is full")



