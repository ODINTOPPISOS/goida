from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QLineEdit, QWidget,
QVBoxLayout,QHBoxLayout, QApplication)
app = QApplication([])
class okno(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Запоминаем число.')
        self.input = QLabel('')
        self.znak = ''
        self.btn1 = QPushButton('Сброс')
        self.btn1.clicked.connect(lambda: self.input.setText(''))
        self.btn2 = QPushButton('Сброс всего')
        self.btn2.clicked.connect(self.obnul)
        self.btn3 = QPushButton('Стереть')
        self.btn4 = QPushButton('/')
        #
        self.btn5 = btn_num('7')
        self.btn6 = btn_num('8')
        self.btn7 = btn_num('9')
        self.btn8 = QPushButton('*')
        #
        self.btn9 = btn_num('4')
        self.btn10 = btn_num('5')
        self.btn11 = btn_num('6')
        self.btn12 = QPushButton('-')
        #
        self.btn13 = btn_num('1')
        self.btn14 = btn_num('2')
        self.btn15 = btn_num('3')
        self.btn16 = QPushButton('+')
        #
        self.btn17 = QPushButton('+-')
        self.btn18 = btn_num('0')
        self.btn19 = QPushButton(',')
        self.btn20 = QPushButton('=')
        #
        self.v1 = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        #
        self.h1.addWidget(self.label)
        #
        self.h2.addWidget(self.input)
        #
        self.h3.addWidget(self.btn1)
        self.h3.addWidget(self.btn2)
        self.h3.addWidget(self.btn3)
        self.h3.addWidget(self.btn4)
        #
        self.h4.addWidget(self.btn5)
        self.h4.addWidget(self.btn6)
        self.h4.addWidget(self.btn7)
        self.h4.addWidget(self.btn8)
        #
        self.h5.addWidget(self.btn9)
        self.h5.addWidget(self.btn10)
        self.h5.addWidget(self.btn11)
        self.h5.addWidget(self.btn12)
        #
        self.h6.addWidget(self.btn13)
        self.h6.addWidget(self.btn14)
        self.h6.addWidget(self.btn15)
        self.h6.addWidget(self.btn16)
        #
        self.h7.addWidget(self.btn17)
        self.h7.addWidget(self.btn18)
        self.h7.addWidget(self.btn19)
        self.h7.addWidget(self.btn20)
        #
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h7)
        self.setLayout(self.v1)
        self.show()
    def obnul(self):
        self.label.setText('')
        self.input.setText('')
        self.znak = ''


class btn_num(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.clicked.connect(self.zxc)
    def zxc(self):
        okno1.input.setText(okno1.input.text() + self.text())

okno1 = okno()
        
app.exec_()
        