import unittest
from unittest.mock import patch
from io import StringIO
import sys
import csv
import pytest
from project import subject_selection,random_question,answer_check
import cowsay

class TestSubjectSelection(unittest.TestCase):
    subjects=['maths', 'physics', 'chemistry']
    @patch('builtins.input', side_effect=['maths'])
    def test_subject_selection_valid_input(self, mock_input):
        global subjects
        captured_output = StringIO()
        sys.stdout = captured_output
        subject = subject_selection()
        sys.stdout = sys.__stdout__
        self.assertEqual(subject, 'maths')
    
    @patch('builtins.input', side_effect=['biology', 'physics'])
    def test_subject_selection_invalid_input_then_valid(self, mock_input):
        global subjects
        captured_output = StringIO()
        sys.stdout = captured_output
        subject = subject_selection()
        sys.stdout = sys.__stdout__
        self.assertEqual(subject, 'physics')


def test_random_question():
     result=random_question("chemistry")
     with open("chemistry.csv" ,"r") as file:
         reader=csv.DictReader(file)
         questions=[{ "question": row["question"],"options": row["options"],"answer": row["answer"],} for row in reader]
     assert result in questions
     result=random_question("physics")
     with open("physics.csv" ,"r") as file:
         reader=csv.DictReader(file)
         questions=[{ "question": row["question"],"options": row["options"],"answer": row["answer"],} for row in reader]
     assert result in questions
     with pytest.raises(FileNotFoundError):
        assert random_question("history")


def test_answer_check():
    assert answer_check({"question":"The unit of power is","options":"A) Watt,B) Volt,C) Joule,D) Ohm","answer":"A"},"a")==True
    assert answer_check({"question":"The motion of a pendulum is an example of","options":"A) Oscillatory motion,B) Linear motion,C) Circular motion,D) Periodic motion","answer":"A"},"b")==False
    assert answer_check({"question":"The unit of power is","options":"A) Watt,B) Volt,C) Joule,D) Ohm","answer":"A"},"b")!=True

if __name__== '__main__':
    unittest.main()
