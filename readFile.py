
import csv

found_students = 0
found_fees = 0
found_messages = 0
found_batch = 0
found_codes = 0
found_attendance = 0
found_sbatch = 0
counter = 0


# Arrays
students_array = []
student_fees_array = []
fees_array = []
batch_array = []
codes_array = []
attendance_array = []
sbatch_array = []

# File path
myFile = "fees_data_30_Jun_2018_00_53_57.txt"
file = open(myFile,"r")

for line in file:
    line = line.strip('\n')
    line = line.strip('~')
    # print(line)

    if line in "{hns_student~":
        found_students = 1
        counter = 1
    if found_students == 1:
        if counter == 1:
            counter = 0
        else:
            students_array.append(line)

    if line in "}" and found_students == 1:
        found_students = 0
        counter = 0

        
    if line in "{hns_fees~":
        found_fees = 1
        counter = 1
    if found_fees == 1:
        if counter == 1:
            counter = 0
        else:
            student_fees_array.append(line)

    if line in "}" and found_fees == 1:
        found_fees = 0
        counter = 0
    
    if line in "{hns_messages~":
        found_messages = 1
        counter = 1
    if found_messages == 1:
        if counter == 1:
            counter = 0
        else:
            fees_array.append(line)

    if line in "}" and found_messages == 1:
        found_messages = 0
        counter = 0

    if line in "{hns_batch~":
        found_batch = 1
        counter = 1
    if found_batch == 1:
        if counter == 1:
            counter = 0
        else:
            batch_array.append(line)

    if line in "}" and found_batch == 1:
        found_batch = 0
        counter = 0

    if line in "{hns_codes~":
        found_codes = 1
        counter = 1
    if found_codes == 1:
        if counter == 1:
            counter = 0
        else:
            codes_array.append(line)

    if line in "}" and found_codes == 1:
        found_codes = 0
        counter = 0

    if line in "{hns_attendance~":
        found_attendance = 1
        counter = 1
    if found_attendance == 1:
        if counter == 1:
            counter = 0
        else:
            attendance_array.append(line)

    if line in "}" and found_attendance == 1:
        found_attendance = 0
        counter = 0
    
    if line in "{hns_sbatch~":
        found_sbatch = 1
        counter = 1
    if found_sbatch == 1:
        if counter == 1:
            counter = 0
        else:
            sbatch_array.append(line)

    if line in "}" and found_sbatch == 1:
        found_sbatch = 0
        counter = 0
    

# print('\n')
# print(students_array)
# print('\n')
# print(student_fees_array)
# print('\n')
# print(fees_array)
# print('\n')
# print(batch_array)
# print('\n')
# print(codes_array)
# print('\n')
# print(attendance_array)

# for line in students_array:
#     print(line.split("^"))

# Using the csv module to parse the list
csv_reader = csv.reader(student_fees_array, delimiter='^')
for line in csv_reader:
    print(line)