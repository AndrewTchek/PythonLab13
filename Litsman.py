import json, csv

# Словник початкових даних
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

# Запис вхідних даних до csv файлу
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

# Читання даних з csv файлу
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

# Запис даних до json файлу
try:
    jsonfile = open('json_data.json', 'w')
    jsonfile.write(json.dumps(data, indent=3))
    jsonfile.close()
except:
    print("Помилка запису даних до json файлу.")
    exit()

# Читання даних з json файлу
json_data = []
try:
    with open('json_data.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
except:
    print("Помилка читання даних з json файлу.")
    exit()

# Запис даних з json файлу у новий csv файл
try:
    with open('new_csv_data.csv', 'w', newline='') as csvfile:
        header = ["Surname", "Position", "Salary", "Gender"]
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for entry in json_data:
            writer.writerow([entry["Surname"], entry["Position"], entry["Salary"], entry["Gender"]])
except:
    print("Помилка запису даних у новий csv файл.")
    exit()

# Нові дані для додавання
new_rows = [
    {"Surname": "Oleg", "Position": "Manager", "Salary": 3000.0, "Gender": "M"},
    {"Surname": "Misha", "Position": "Designer", "Salary": 8200.0, "Gender": "M"}
]

# Додавання нових рядків у існуючий CSV файл
try:
    with open('new_csv_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in new_rows:
            writer.writerow([row["Surname"], row["Position"], row["Salary"], row["Gender"]])
except:
    print("Помилка дописування даних у CSV файл.")
    exit()
