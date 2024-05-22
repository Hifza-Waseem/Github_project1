import PyQt5.QtWidgets as qtw
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        result_field = qtw.QLineEdit()
        container.setLayout(qtw.QGridLayout())

        result_field.setReadOnly(True)

        btn_result = qtw.QPushButton('Enter')
        btn_result.clicked.connect(lambda: self.enter_pressed(result_field))

        btn_clear = qtw.QPushButton('Clear')
        btn_clear.clicked.connect(lambda: self.clear_pressed(result_field))

        btn_9 = qtw.QPushButton('9')
        btn_9.clicked.connect(lambda: self.number_pressed('9', result_field))

        btn_8 = qtw.QPushButton('8')
        btn_8.clicked.connect(lambda: self.number_pressed('8', result_field))

        btn_7 = qtw.QPushButton('7')
        btn_7.clicked.connect(lambda: self.number_pressed('7', result_field))

        btn_6 = qtw.QPushButton('6')
        btn_6.clicked.connect(lambda: self.number_pressed('6', result_field))

        btn_5 = qtw.QPushButton('5')
        btn_5.clicked.connect(lambda: self.number_pressed('5', result_field))

        btn_4 = qtw.QPushButton('4')
        btn_4.clicked.connect(lambda: self.number_pressed('4', result_field))

        btn_3 = qtw.QPushButton('3')
        btn_3.clicked.connect(lambda: self.number_pressed('3', result_field))

        btn_2 = qtw.QPushButton('2')
        btn_2.clicked.connect(lambda: self.number_pressed('2', result_field))

        btn_1 = qtw.QPushButton('1')
        btn_1.clicked.connect(lambda: self.number_pressed('1', result_field))

        btn_0 = qtw.QPushButton('0')
        btn_0.clicked.connect(lambda: self.number_pressed('0', result_field))

        btn_plus = qtw.QPushButton('+')
        btn_plus.clicked.connect(lambda: self.operation_pressed('+', result_field))

        btn_minus = qtw.QPushButton('-')
        btn_minus.clicked.connect(lambda: self.operation_pressed('-', result_field))

        btn_multiply = qtw.QPushButton('*')
        btn_multiply.clicked.connect(lambda: self.operation_pressed('*', result_field))

        btn_divide = qtw.QPushButton('/')
        btn_divide.clicked.connect(lambda: self.operation_pressed('/', result_field))

        container.layout().addWidget(result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_multiply, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divide, 5, 3)

        self.layout().addWidget(container)

        # Store the current value and operator
        self.current_value = ''
        self.current_operator = ''
        self.pending_value = ''

    def number_pressed(self, number, result_field):
        self.current_value += number
        result_field.setText(self.current_value)

    def operation_pressed(self, operator, result_field):
        self.current_operator = operator
        self.pending_value = self.current_value
        self.current_value = ''
        result_field.clear()

    def enter_pressed(self, result_field):
        if self.current_operator and self.pending_value and self.current_value:
            try:
                if self.current_operator == '+':
                    result = float(self.pending_value) + float(self.current_value)
                elif self.current_operator == '-':
                    result = float(self.pending_value) - float(self.current_value)
                elif self.current_operator == '*':
                    result = float(self.pending_value) * float(self.current_value)
                elif self.current_operator == '/':
                    result = float(self.pending_value) / float(self.current_value)
                else:
                    result = float(self.current_value)

                result_field.setText(str(result))
                self.current_value = str(result)
                self.pending_value = ''
                self.current_operator = ''
            except ZeroDivisionError:
                result_field.setText("Error: Division by zero")
            except Exception as e:
                result_field.setText("Error")
                print(e)

    def clear_pressed(self, result_field):
        result_field.clear()
        self.current_value = ''
        self.pending_value = ''
        self.current_operator = ''


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
