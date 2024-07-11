#
from day17_data import question_data
from day17_question_model import Question
from day17_quiz_brain import QuizBrain


question_bank = []

for _ in question_data:
    question_bank.append(Question(_["question"], _["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"You're final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}.")