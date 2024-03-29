from projects.question_model import Question
from projects.data import question_data
from projects.quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    quiz = question['question']
    answer = question['correct_answer']

    new_question = Question(quiz, answer)

    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f'Your final score was: {quiz.current_score}/{quiz.question_number}')
