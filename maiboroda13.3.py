import json
import csv

# Читання даних з CSV-файлу
data = []
try:
    with open('new_csv_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Зчитування заголовків файлу
        for row in reader:
            # Додавання даних з файлу до списку словників
            data.append({"Surname": row[0], "Position": row[1], "Salary": float(row[2]), "Gender": row[3]})
except Exception as e:
    print(f"Помилка читання даних з CSV файлу: {e}")
    exit()

# Нові дані для додавання
new_rows = [
    {"Surname": "Brown", "Position": "Intern", "Salary": 2000.0, "Gender": "F"},
    {"Surname": "Taylor", "Position": "Analyst", "Salary": 6000.0, "Gender": "M"}
]

# Додавання нових рядків до зчитаних даних
data.extend(new_rows)

# Запис оновлених даних до JSON-файлу
try:
    with open('new_json_data.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=3)  # Запис даних у форматі JSON з відступами
except Exception as e:
    print(f"Помилка запису даних до JSON файлу: {e}")
    exit()

print("Дані успішно записано у JSON файл.")