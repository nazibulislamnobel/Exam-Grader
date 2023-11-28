def read_answers(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

def grade_exam(correct_answers, student_answers):
    correct_count = 0
    correct_indices = []
    incorrect_indices = []

    for i in range(len(correct_answers)):
        if correct_answers[i] == student_answers[i]:
            correct_count += 1
            correct_indices.append(i + 1)
        else:
            incorrect_indices.append(i + 1)

    return correct_count, correct_indices, incorrect_indices

def main():
    correct_answers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D']
    
    try:
        student_answers = read_answers('/content/drive/MyDrive/student_solution.txt')
    except FileNotFoundError:
        print("Error: The file 'student_solution.txt' was not found.")
        return

    if len(student_answers) != len(correct_answers):
        print("Error: The number of student answers does not match the number of correct answers.")
        return

    correct_count, correct_indices, incorrect_indices = grade_exam(correct_answers, student_answers)

    with open('/content/drive/MyDrive/test_result.txt', 'w') as result_file:
        if correct_count >= 7:
            result_file.write(f'Congratulations!! You passed the exam\n')
        else:
            result_file.write(f'Sorry, you did not pass the exam\n')

        result_file.write(f'You answered {correct_count} questions correctly and {len(incorrect_indices)} questions incorrectly\n')
        result_file.write(f'The numbers of the questions you answered correctly are: {" ".join(map(str, correct_indices))}\n')
        result_file.write(f'The numbers of the questions you answered incorrectly are: {" ".join(map(str, incorrect_indices))}\n')

    if correct_count >= 7:
        print("Congratulations!! You passed the exam")
    else:
        print("Sorry, you did not pass the exam")
    print(f'You answered {correct_count} questions correctly and {len(incorrect_indices)} questions incorrectly')
    print(f'The numbers of the questions you answered correctly are: {correct_indices}')
    print(f'The numbers of the questions you answered incorrectly are: {incorrect_indices}')

if __name__ == "__main__":
    main()