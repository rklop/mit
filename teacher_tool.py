import ollama
import os
import json
import random as rand

script_dir = os.path.dirname(os.path.abspath(__file__))

# course_details
course_name = "Linear Algebra"
start_date = "9/2/2024"
end_date = "12/9/2024"
num_classes_per_week = 2
num_of_students = 10

msg1 = "Give a list of topics in a " + course_name + "course without extra details"
response1 = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': msg1,
    },
])

# print(response1['message']['content'])

expansion = response1['message']['content']

start = 0
for i in range(len(expansion)):
    if expansion[i] == '1':
        topics = expansion[i:]
        break

topic_list = [topic.split(". ", 1)[1] for topic in topics.strip().split("\n")]
# print(topic_list)

msg2 = "Give a list of 8 relevent previous courses for " + course_name + " without extra details"
response2 = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': msg2,
    },
])

print(response2['message']['content'])

students = {}

# Loop to create each student, initialized with 0 ratings and 0 current grade, which means that it hasn't been updated.
for i in range(1, num_of_students + 1):
    students[f"student{i}"] = {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": []
    }


# print(students)

# 
def change_rating(student_name, topic_name, value):
    students[student_name]["personal_comfort_rating"][topic_list.index(topic_name)][1] = value

def change_grade(student_name, value):
    students[student_name]["current_grade"] = value

for student in students:
    for topic in topic_list:
        change_rating(student, topic, rand.randint(0, 10))
    change_grade(student,rand.randint(6000, 9500) / 1000.0 )


print(students)


file_path1 = os.path.join(script_dir, "students.json")
with open(file_path1, 'w') as json_file:
    json.dump(students, json_file, indent=4)



course_details = "This course starts on " + str(start_date) + " and ends on " + str(end_date) + ", with " + str(num_classes_per_week) + " classes every week. There should be something to do on every Monday and Wednesday."

msg3 = "Using " + str(students) + "generate a course calendar in a word form listing the dates of classes that fits the class skill level as a whole without student clustering. For example, if they are both uncomfortable with a topic, it\
should take longer. The numbers in 'personal_comfort_rating' indicate a value students give on their comfort level with the subject between 1 and 10. A score of 0 means that topic has not been touched yet. The number in 'current_grade'\
represents the current grade in the class between 1 and 10 given by the teacher. A score of 0 means the class has not given out grades yet. Please use bullet points on each week."

response3 = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': course_details + msg3,
    },
])

print(response3['message']['content'])

result = response3['message']['content']

file_path2 = os.path.join(script_dir, "LLMresponse.txt")


with open(file_path2, "w") as text_file:
    text_file.write(result)