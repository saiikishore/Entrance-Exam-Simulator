import cowsay
import csv
import random

subjects = ["maths", "physics", "chemistry"]

def main():
    cowsay.tux("Welcome to the Entrance Exam")
    count = 0
    for i in range(3):
        subject = subject_selection()
        for i in range(10):
            questions = random_question(subject)
            print(questions["question"])
            see_options = questions["options"].split(",")
            for i in see_options:
                print(i.strip())
            answer = input("What is the answer: ").strip()
            if answer_check(questions, answer) == True:
                count += 1
    cowsay.tux("You scored : " + str(count) + " marks")
    if count > 10:
        cowsay.trex("You have passed the exam")
    else:
        cowsay.stegosaurus("Better luck next time")


def subject_selection():
    while True:
        cowsay.ghostbusters(f"Choose subject {subjects}")
        subject = input("Enter: ").strip().lower()
        if subject in subjects:
            subjects.remove(subject)
            return subject
            break
        elif subject not in subjects:
            print("enter valid subject")
            continue
        else:
            continue


def random_question(n):
    name = n + ".csv"
    questions = []
    try:
        with open(name, "r") as file:
            reader = csv.DictReader(file)
            for rows in reader:
                questions.append(
                    {
                        "question": rows["question"],
                        "options": rows["options"],
                        "answer": rows["answer"],
                    }
                )
        return random.choice(questions)
    except FileNotFoundError:
        print("Not a Valid subject")
        raise


def answer_check(questions, answer):
    while True:
        if answer.lower() in ["a", "b", "c", "d"]:
            return questions["answer"] == answer.upper()
        else:
            answer = input("Enter valid option: ")


if __name__ == "__main__":
    main()
