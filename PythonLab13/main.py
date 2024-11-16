import json, csv

#Словник початкових даних
employees = [{"Surname":"Graves",
         "Position":"CEO",
         "Salary":17000.0,
         "Gender":"M"},
        {"Surname":"Johnson",
         "Position":"Developer",
         "Salary":4500.0,
         "Gender":"F"},
        {"Surname":"King",
         "Position":"Developer",
         "Salary":11000.0,
         "Gender":"M"},
        {"Surname":"Bradley",
         "Position":"TeamLead",
         "Salary":12500.0,
         "Gender":"M"},
        {"Surname":"Todd",
         "Position":"Manager",
         "Salary":7400.0,
         "Gender":"M"},
        {"Surname":"Smith",
         "Position":"Designer",
         "Salary":7000.0,
         "Gender":"F"}]

#Запис вхідних даних до csv файлу
try:
    csvfile = open('csv_data.csv', 'w', newline='')
    header = ["Surname", "Position", "Salary", "Gender"]
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for i in range(len(employees)):
        writer.writerow([employees[i]["Surname"], employees[i]["Position"], employees[i]["Salary"], employees[i]["Gender"]])
    csvfile.close()
except:
    print("Помилка запису даних до csv файлу.")
    exit()



#Читання даних з csv файлу
data = []
try:
    csvfile = open('csv_data.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',')
    reader.__next__()
    for row in reader:
        data.append({"Surname": row[0], "Position": row[1], "Salary": float(row[2]), "Gender": row[3]})
    csvfile.close()
except:
    print("Помилка читання даних з csv файлу.")
    exit()


#Запис даних до json файлу
try:
    jsonfile = open('json_data.json', 'w')
    jsonfile.write(json.dumps(data, indent=3))
    jsonfile.close()
except:
    print("Помилка запису даних до json файлу.")
    exit()
