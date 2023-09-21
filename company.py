"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 95000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# 1
for dep in departments:
    print(dep['title'])
print()

# 2
personnel_list = []
for dep in departments:
    for person in dep['employers']:
        personnel_list.append(f"{person['first_name']} {person['last_name']}")
print(personnel_list)
print()


# 3
personnel_dict = {}
for dep in departments:
    for person in dep['employers']:
        personnel_dict[f"{person['first_name']} {person['last_name']}"] = dep['title']
print(personnel_dict)
print()


# 4
personnel_list = []
for dep in departments:
    for person in dep['employers']:
        if person['salary_rub'] > 100000:
            personnel_list.append(f"{person['first_name']} {person['last_name']}")
print(personnel_list)
print()


# 5
personnel_list = []
for dep in departments:
    for person in dep['employers']:
        if person['salary_rub'] < 80000:
            personnel_list.append(person['position'])
print(personnel_list)
print()


# 6
personnel_dict = {}
for dep in departments:
    personnel_dict[dep['title']] = 0
    for person in dep['employers']:
        personnel_dict[dep['title']] += person['salary_rub']
for k,v in personnel_dict.items():
    print(f'Зарплатный фонд отдела {k} составляет {v} рублей')
print()


# 7
personnel_list = []
for dep in departments:
    for person in dep['employers']:
        personnel_list.append(person['salary_rub'])
    print(f'Минимальная заработная плата в отделе {dep["title"]} составила {min(personnel_list)}')
    personnel_list = []
print()


# 8
for dep in departments:
    for person in dep['employers']:
        personnel_list.append(person['salary_rub'])
    print(f'В отделе {dep["title"]} минимальная з/п составила {min(personnel_list)} руб., '
          f'максимальная з/п составила {max(personnel_list)} руб., '
          f'средняя з/п составила {sum(personnel_list)/len(personnel_list)} руб.')
    personnel_list = []
print()


# 9
for dep in departments:
    for person in dep['employers']:
        personnel_list.append(person['salary_rub'])
print(f'Средняя з/п по компании составила {sum(personnel_list)/len(personnel_list)} руб.')
print()


# 10
personnel_list = []
for dep in departments:
    for person in dep['employers']:
        if person['salary_rub'] > 90000 and person['position'] not in personnel_list:
            personnel_list.append(person['position'])
print(f'Больше 90000 рублей получают следующие должности: {personnel_list}')
print()


# 11
personnel_list = []
female_names = ['Michelle', 'Nicole', 'Christina', 'Caitlin']
for dep in departments:
    for person in dep['employers']:
        if person['first_name'] in female_names:
            personnel_list.append(person['salary_rub'])
    print(f'В отделе {dep["title"]} средняя з/п среди девушек составила {int(sum(personnel_list)/len(personnel_list))} руб.')
    personnel_list = []
print()


# 12
vowel_str = 'aeiouy'
for dep in departments:
    for person in dep['employers']:
        if person['last_name'][-1] in vowel_str:
            personnel_list.append(f"{person['first_name']} {person['last_name']}")
print(personnel_list)
print()


# 13
total_taxes_dict = {}
for dep in departments:
    department = dep['title']
    for tax in taxes:
        if tax['department'] == department or tax['department'] is None:
            if department in total_taxes_dict:
                total_taxes_dict[department] += tax['value_percents']
            else:
                total_taxes_dict[department] = tax['value_percents']
print(total_taxes_dict)
print()

# 14
personnel_salary_list = []
person_salary_dict = {}
for dep in departments:
    for person in dep['employers']:
        person_salary_dict['name'] = f"{person['first_name']} {person['last_name']}"
        person_salary_dict['department'] = dep['title']
        person_salary_dict['before_tax'] = person['salary_rub']
        for k,v in total_taxes_dict.items():
            if dep['title'] == k:
                person_salary_dict['after_tax'] = int(
                    person_salary_dict['before_tax'] * (1-v/100))
                person_salary_dict['tax'] = int(person_salary_dict['before_tax']*v/100)
        personnel_salary_list.append(person_salary_dict)
        person_salary_dict = {}
for person in personnel_salary_list:
    print(f"Имя: {person['name']}, зарплата на руки: {person['after_tax']}, "
          f"зарплата до уплаты налогов: {person['before_tax']}")
print()


# 15
department_tax_sum = {}
for person in personnel_salary_list:
    if person['department'] not in department_tax_sum:
        department_tax_sum[person['department']] = person['tax']
    else:
        department_tax_sum[person['department']] += person['tax']
print(sorted(department_tax_sum.items(), key = lambda item: item[1]))
print()


# 16
for person in personnel_salary_list:
    if person['tax']*12 > 100000:
        print(f"Имя: {person['name']}, уплачено налогов за год {person['tax']*12}")
print()


# 17
min_taxes_person = {'name': '', 'tax': 0}
for person in personnel_salary_list:
    if min_taxes_person['tax'] == 0:
        min_taxes_person['tax'] = person['tax']
        min_taxes_person['name'] = person['name']
    else:
        if min_taxes_person['tax'] > person['tax']:
            min_taxes_person['tax'] = person['tax']
            min_taxes_person['name'] = person['name']
print(f"Минимальный налог компания платит за сотрудника {min_taxes_person['name']}")