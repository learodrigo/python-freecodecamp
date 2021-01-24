employee_file_path = "extras/index.html"
employee_file = open(employee_file_path, "w")

employee_file.write("Toby - Humas resources\n")

employee_file.close()

employee_file = open(employee_file_path, "w")

employee_file.write("<p>This is an index done with python</p>")

employee_file.close()
