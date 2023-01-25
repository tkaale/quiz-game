import data
import guiz_brain


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_bank = []
for question in data.question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_bank.append(Question(question_text, question_answer))

print(question_bank)

quiz = guiz_brain.QuizBrain(create_question_bank(data.question_data))
quiz.next_question()



#{'text': "A slug's blood is green.", 'answer': 'True'}
