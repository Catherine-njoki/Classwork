def show_history() -> None:
    print("\n== Brief History of Python ==")
    print("== Created in the year 1991 ==")
    print("== Python 3 in the year 2008 ==")
    print("\n*** Program that computes the average ***")


def get_names_score() -> tuple[list[str], list[float]]:
    names_of_students = []
    scores = []

    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please enter a number greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input")

    print("\nEnter student name and their scores:")

    for i in range(count):
        name = input(f'Student {i + 1} name: ').strip()
        if not name:
            name = f'Student {i + 1}'
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print("Invalid input")

    return names_of_students, scores


def assign_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def display_results(names: list[str], scores: list[float]) -> None:
    print("\n=========== Students Results ===========")
    for name, score in zip(names, scores):
        grade = assign_grade(score)
        print(f'{name} : Score = {score}, Grade = {grade}')

    average = sum(scores) / len(scores)
    print(f"\nClass Average Score: {average:.2f}")


if __name__ == '__main__':
    show_history()
    students_names, students_scores = get_names_score()
    display_results(students_names, students_scores)
