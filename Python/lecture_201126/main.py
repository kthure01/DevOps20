def print_grade(percent):
    if percent >= 90:
        grade = "A"
    elif percent >= 80:
        grade = "B"
    elif percent >= 70:
        grade = "C"
    elif percent >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade


def calculate_percent(score):
    return (score / points_possible) * 100


points_possible = 100

student_name = input("Ange studentens namn: ")

try:
    score = int(input("Ange studentens score: ") or 0)
    percent = calculate_percent(score)
except Exception:
    print(f"Exception: ")
    exit(99)

grade = print_grade(percent)
print(f"{student_name} har {score} poäng vilket ger betyg {grade}")

print(dir(tuple))
