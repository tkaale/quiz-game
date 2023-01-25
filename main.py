import data
import quiz_brain


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_bank = []
for question in data.question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)

while True:
    quiz.next_question()
    if quiz.still_has_questions() == True:
        continue
    else:
        break




# print(question_bank[1].answer)
# print(question_bank[1].text)
# {'text': "A slug's blood is green.", 'answer': 'True'}