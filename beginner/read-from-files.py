file_path = "extras/employees.txt"

# "r" - read only
# "w" - write
# "a" - append at the end
# "r+" - read and write

employee_file = open(file_path, "r")

if employee_file.readable():
    # print(employee_file.readline())
    # print(employee_file.readlines()
    for employee in employee_file.readlines():
        print(employee)

employee_file.close()
