import ollama
import pandas

# course_details
course_name = "Linear Algebra"
start_date = "9/2/2024"
end_date = "12/9/2024"
num_classes_per_week = 2

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

students = {
    "student1": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Calculus II", "Introductory Statistics", "Discrete Mathematics", "Trigonometry", "Algebra II"
        ]
    },
    "student2": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Calculus II", "Algebra I", "Discrete Mathematics"
        ]
    },
    "student3": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Calculus II", "Algebra I", "Algebra II"
        ]
    },
    "student4": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Discrete Mathematics", "Algebra II", "Trigonometry"
        ]
    },
    "student5": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Algebra I", "Calculus II", "Discrete Mathematics"
        ]
    },
    "student6": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Introductory Statistics", "Algebra II", "Pre-calculus", "Trigonometry"
        ]
    },
    "student7": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Calculus II", "Pre-calculus", "Algebra II"
        ]
    },
    "student8": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Trigonometry", "Calculus I", "Calculus II"
        ]
    },
    "student9": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Pre-calculus", "Introductory Statistics", "Discrete Mathematics"
        ]
    },
    "student10": {
        "personal_comfort_rating": [[topic, 0] for topic in topic_list],
        "current_grade": 0,
        "previous_relevant_courses": [
            "Calculus II", "Pre-calculus", "Calculus I", "Trigonometry"
        ]
    }
}


def change_rating(student_name, topic_name, value):
    students[student_name]["personal_comfort_rating"][topic_list.index(topic_name)][1] = value

def change_grade(student_name, value):
    students[student_name]["current_grade"] = value

# for student in students:
#     change_rating(student, topic_list[1], 5)

# print(students)



course_details = "This course starts on " + str(start_date) + " and ends on " + str(end_date) + ", with " + str(num_classes_per_week) + " classes every week, every Monday and Wednesday."

msg3 = "Using " + str(students) + "generate a course calendar with dates of classes that fits the class skill level as a whole without student clustering over a 15 week period. For example, if they are both uncomfortable with a topic, it\
should take longer. The numbers in 'personal_comfort_rating' indicate a value students give on their comfort level with the subject between 1 and 10. A score of 0 means that topic has not been touched yet. The number in 'current_grade'\
represents the current grade in the class between 1 and 10 given by the teacher. A score of 0 means the class has not given out grades yet."

response3 = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': course_details + msg3,
    },
    ])

print(response3['message']['content'])