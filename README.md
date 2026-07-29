
# Entrance Exam Simulator
#### Video Demo:<URL https://youtu.be/B1mzuDMq0s8?si=B-5Ef0JrJrg5oTgu>
#### Description:
Welcome to the "Entrance Exam Simulator"! This project is designed to provide a fun and interactive way for users to test their knowledge in various subjects, including Mathematics, Physics, and Chemistry. Using the whimsical `cowsay` library, this simulator makes the exam-taking experience enjoyable and engaging.

## Project Overview
The Entrance Exam Simulator is a command-line application that simulates an entrance exam in three subjects: Mathematics, Physics, and Chemistry. Users are greeted by Tux, the friendly Linux penguin from the `cowsay` library, who guides them through the process of selecting subjects, answering questions, and receiving their scores.

### Features:
- **Subject Selection:** Users can choose from three subjects to answer questions from.
- **Randomized Questions:** Each subject has a set of pre-defined questions stored in CSV files, which are randomly selected during the quiz.
- **Answer Validation:** The user's answers are checked against the correct answers, and a score is kept throughout the exam.
- **Score Display:** At the end of the exam, Tux displays the user's score and provides feedback on whether they passed or failed.

## Files and Functionality
- **main.py:** This is the main file that runs the entrance exam simulator. It contains the primary functions for running the quiz, displaying questions, and checking answers.
- **subject_selection() Function:** This function prompts the user to select a subject from the available options. Once a subject is chosen, it is removed from the list to avoid repetition.
- **random_question() Function:** This function reads questions from a CSV file corresponding to the chosen subject and selects a random question to display.
- **answer_check() Function:** This function checks if the user's answer is correct and updates the score accordingly.
- **CSV Files:** There are three CSV files (`maths.csv`, `physics.csv`, and `chemistry.csv`), each containing a set of questions, multiple-choice options, and the correct answer.

## Design Choices
- **Cowsay Library:** The use of the `cowsay` library adds a playful element to the project. Different characters from `cowsay` provide feedback and guidance to the user, making the experience more enjoyable.
- **Command-Line Interface:** The decision to use a command-line interface makes the project accessible and easy to run without requiring additional dependencies or graphical interfaces.
- **CSV File Format:** Storing questions in CSV files allows for easy modification and expansion of the question sets. Each subject's questions are kept in a separate file for better organization.
- **Random Question Selection:** Randomly selecting questions from a pool ensures that each quiz session is unique and prevents memorization of answers.

## Usage Instructions
1. Ensure you have Python installed on your machine.
2. Install the `cowsay` library using pip: `pip install cowsay`
3. Place the project files (`main.py` and the CSV files) in a directory.
4. Run the project by executing `python main.py` in your command-line interface.
5. Follow the prompts to select subjects and answer questions.
6. At the end of the exam, view your score and feedback.

## Future Enhancements
- **Additional Subjects:** Adding more subjects and corresponding CSV files to expand the range of topics covered.
- **Graphical User Interface:** Developing a graphical user interface (GUI) to make the simulator more visually appealing and user-friendly.
- **Timed Quizzes:** Implementing a timer for each question to add a sense of urgency and simulate real exam conditions.
- **Detailed Feedback:** Providing detailed explanations for each answer to help users learn from their mistakes.

We hope you enjoy using the Entrance Exam Simulator and find it a valuable tool for testing your knowledge in various subjects!
