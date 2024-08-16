import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.display = QLineEdit()
        grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            'C', 'Umar', 'BeK', '<-',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        positions = [(i, j) for i in range(1, 6) for j in range(4)]
        for position, button in zip(positions, buttons):
            if button != '':
                button_obj = QPushButton(button)
                button_obj.clicked.connect(self.on_button_click)
                grid.addWidget(button_obj, *position)

        self.setWindowTitle('Calculator(Bek)')
        self.setGeometry(400, 400, 300, 400)
        self.show()

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Bunday amal mavjud emas')
        elif text == "C":
            self.display.setText('')
        elif text == "<-":
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        else:
            self.display.setText(self.display.text() + text)

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
