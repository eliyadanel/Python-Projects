# List Comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]   # new_list = [new_item for item in list]
print(new_list)
name = "Eliya"
letters = [letter for letter in name]
print(letters)
range_list = [(n * 2) for n in range(1, 5)]
print(range_list)
# new_list = [new_item for item in list if test]
import random
import pandas

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)
all_caps = [name.upper() for name in names if len(name) > 4]
print(all_caps)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

result = [number for number in numbers if number % 2 == 0]
print(result)

# new_dict = {new_key: new_value for (key, value) in dict.items()}
students_scores = {student: random.randint(40, 100) for student in names}
print(students_scores)
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

sentence = "what is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Sunday": 24,
}
weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)

students_dict = {
    "Student": ("Angela", "Eliya", "James", "Lily"),
    "Scores": (56, 76, 98, 80),
}
student_df = pandas.DataFrame(students_dict)
print(student_df)
for (index, row) in student_df.iterrows():
    print(index)
    print(row.Scores)
