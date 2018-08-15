""" file = open("testfile.txt","w")
file.write("HelloWorld")
file.write("This is our new text file")
file.write("and this is another line")
file.write("Why? Because we can.")
file.close """


bFoundStudents = 0
bFoundFees = 0
bFoundMessages = 0
bFoundBatch = 0
bFoundCodes = 0
bFoundAttendance = 0
bFoundsBatch = 0
iCounter = 0


# Arrays
arryStudents = []
arryStudentFees = []
arrayFees = []
arrayBatch = []
arrayCodes = []
arrayAttendance = []
arraysBatch = []

myFile = "fees_data_30_Jun_2018_00_53_57.txt"
file = open(myFile,"r")

for line in file:
    line = line.strip('\n')
    # print(line)

    if line in "{hns_student~":
        bFoundStudents = 1
        iCounter = 1
    if bFoundStudents == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arryStudents.append(line)

    if line in "}" and bFoundStudents == 1:
        bFoundStudents = 0
        iCounter = 0

        
    if line in "{hns_fees~":
        bFoundFees = 1
        iCounter = 1
    if bFoundFees == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arryStudentFees.append(line)

    if line in "}" and bFoundFees == 1:
        bFoundFees = 0
        iCounter = 0
    
    if line in "{hns_messages~":
        bFoundMessages = 1
        iCounter = 1
    if bFoundMessages == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arrayFees.append(line)

    if line in "}" and bFoundMessages == 1:
        bFoundMessages = 0
        iCounter = 0

    if line in "{hns_batch~":
        bFoundBatch = 1
        iCounter = 1
    if bFoundBatch == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arrayBatch.append(line)

    if line in "}" and bFoundBatch == 1:
        bFoundBatch = 0
        iCounter = 0

    if line in "{hns_codes~":
        bFoundCodes = 1
        iCounter = 1
    if bFoundCodes == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arrayCodes.append(line)

    if line in "}" and bFoundCodes == 1:
        bFoundCodes = 0
        iCounter = 0

    if line in "{hns_attendance~":
        bFoundAttendance = 1
        iCounter = 1
    if bFoundAttendance == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arrayAttendance.append(line)

    if line in "}" and bFoundAttendance == 1:
        bFoundAttendance = 0
        iCounter = 0
    
    if line in "{hns_sbatch~":
        bFoundsBatch = 1
        iCounter = 1
    if bFoundsBatch == 1:
        if iCounter == 1:
            iCounter = 0
        else:
            arraysBatch.append(line)

    if line in "}" and bFoundsBatch == 1:
        bFoundsBatch = 0
        iCounter = 0
    

# print('\n')
# print(arryStudents)
# print('\n')
# print(arryStudentFees)
# print('\n')
# print(arrayFees)
# print('\n')
# print(arrayBatch)
# print('\n')
# print(arrayCodes)
# print('\n')
# print(arrayAttendance)

for line in arryStudents:
    print(line.split("^"))