import data


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


def create_question_bank(question_data):
    question_bank = []
    for question in question_data:
        question_text = question['text']
        question_answer = question['answer']
        question_bank.append(Question(question_text, question_answer))
    return question_bank


print(create_question_bank(data.question_data))


#{'text': "A slug's blood is green.", 'answer': 'True'}
