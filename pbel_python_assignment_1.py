# IBM PBEL Python Assignment - 1
# Submitted by: Subhan Adil

# Q1
user_input = int(input("Please enter a whole number: "))
if user_input % 2 == 0:
    print(f"Result: {user_input} is an Even number.")
else:
    print(f"Result: {user_input} is an Odd number.")

# Q2
for current_num in range(1, 11):
    print(current_num, end=" ")
print() 

# Q3
loop_index = 1
while loop_index <= 10:
    print(loop_index, end=" ")
    loop_index += 1
print()

# Q4
chosen_table = int(input("Enter the number you want a table for: "))
for multiplier in range(1, 11):
    print(f"{chosen_table} x {multiplier} = {chosen_table * multiplier}")

# Q5
for candidate in range(1, 51):
    if candidate % 3 == 0:
        print(candidate, end=" ")
print()

# Q6
student_name = "Subhan Adil"  
academic_marks = 88        
student_height = 5.8       
print(f"Profile Summary -> Name: {student_name}, Marks: {academic_marks}, Height: {student_height}")

# Q7
text_digits = "123"
parsed_int = int(text_digits)  
calculated_sum = parsed_int + 10
print(f"Original string '{text_digits}' converted to integer and added to 10 equals: {calculated_sum}")

# Q8
test_value = int(input("Enter a value to check if it's divisible by 2 and 3: "))
if test_value % 2 == 0 and test_value % 3 == 0:
    print(f"Verified: {test_value} passes both division tests.")
else:
    print(f"Failed: {test_value} is not divisible by both 2 and 3.")

# Q9
first_val = int(input("Enter value for variable A: "))
second_val = int(input("Enter value for variable B: "))
print(f"Initial State: A = {first_val}, B = {second_val}")
first_val, second_val = second_val, first_val
print(f"Swapped State: A = {first_val}, B = {second_val}")