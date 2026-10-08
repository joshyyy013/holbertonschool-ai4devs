def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores) if scores else 0
    return average


def print_average(student, scores):
    if not scores:
        print(f"{student} has no scores available.")
        return

    average = calculate_average(scores)
    print(f"{student}'s average: {average:.1f}")


def main():
    print_average("Alex", [70, 80, 90])
    print_average("Sam", [])


if __name__ == "__main__":
    main()