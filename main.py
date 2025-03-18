school_scores = {
        "Math": {
            "Alice": [85, 90, 78],
            "Bob": [72, 88, 91],
            "Charlie": [95, 100, 92]
        },
        "Science": {
            "Alice": [80, 85, 88],
            "Bob": [78, 82, 85],
            "Diana": [90, 91, 89]
        },
        "History": {
            "Charlie": [70, 75, 80],
            "Diana": [88, 92, 84]
        }
    }
def calculate_class_averages(classrooms):
    class_average = {}

    for classroom, students in classrooms.items():
        if not students:
            class_average[classroom] = 0
            continue

        score = 0
        num_grades = 0

        for grades in students.values():
            for grade in grades:
                score += grade
                num_grades += 1
        class_average[classroom] = score / num_grades 

    return class_average

calculate_class_averages(school_scores)