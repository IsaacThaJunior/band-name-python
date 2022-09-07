from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    quiz = question['text']
    answer = question['answer']

    new_question = Question(quiz, answer)

    question_bank.append(new_question)
