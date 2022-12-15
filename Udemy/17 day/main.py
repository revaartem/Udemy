from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))

q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()
q_brain.quiz_final()
