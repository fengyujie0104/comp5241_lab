import json

# 读取 JSON 文件
with open('student.json', 'r') as file:
    data = json.load(file)

# 访问 JSON 数据
students = data['students']
print(students)

# 遍历学生列表
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, City: {student['city']}")

# 计算平均年龄
total_age = sum(student['age'] for student in students)
average_age = total_age / len(students)
print(f"Average Age: {average_age}")