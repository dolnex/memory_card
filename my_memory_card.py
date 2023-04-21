#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QMessageBox, QButtonGroup

from  random import shuffle
from random import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []
que = Question('Какой национальности не существует?', right_answer='Смурфы', wrong1='Энцы', wrong2='Чулымцы', wrong3='Алеуты')
questions_list.append(que)
questions_list.append(Question('Государственный язык Бразилии', right_answer='Португальский', wrong1='Итальянский', wrong2='Испанский', wrong3='Бразильский'))
questions_list.append(Question('Как правильно на английском Питон?', right_answer='Python', wrong1='Pyton', wrong2='Piton', wrong3='Paython'))
questions_list.append(Question('В каком году началась 2 мировая война?', right_answer='1939', wrong1='1942', wrong2='1921', wrong3='1954'))
questions_list.append(Question('Какая планета на 3 месте от солнца?', right_answer='Земля', wrong1='Юпитер', wrong2='Меркурий', wrong3='Марс'))

app = QApplication([])
window = QWidget()
window.resize(400,100)
window.cur_question = -1
window.setWindowTitle('Memory Card')
btn = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')
#вопросы
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Смурфы')
rbtn_2 = QRadioButton('Энцы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

rbtn_group = QButtonGroup()
rbtn_group.addButton(rbtn_1)
rbtn_group.addButton(rbtn_2)
rbtn_group.addButton(rbtn_3)
rbtn_group.addButton(rbtn_4)

#лэйауты
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат текста')
text_result = QLabel('прав ты  или нет?')
text_correct = QLabel('Смурфы')

layout_res = QVBoxLayout()
layout_res.addWidget(text_result, alignment = Qt.AlignLeft)
layout_res.addWidget(text_correct, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

#главное окно
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn, stretch=1)


AnsGroupBox.hide()

layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1) #вопрос
layout_card.addLayout(layout_line2) #варианты ответов
layout_card.addLayout(layout_line3) #кнопка ответить/следующий вопрос

window.setLayout(layout_card)
#функции
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    rbtn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    rbtn_group.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    text_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    text_result.setText(res)
    show_result()

def next_question():
    if len(questions_list) != 0:
        window.total += 1
        window.cur_question = 1
    q = questions_list[randint(0, len(questions_list) - 1)]
    ask(q)
    questions_list.remove(q)



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n- Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', round((window.score/window.total*100), 0), '%')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверено!')       
            print('Статистика\n- Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
            print('Рейтинг: ', round((window.score/window.total*100), 0), '%')

def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
        if que in questions_list:
            questions_list.remove(que)
    else:
        if len(questions_list) > 0:
            next_question()
        else:
            exit()



window.score = 0
window.total = 1


btn.clicked.connect(click_OK)
window.show()
app.exec_()