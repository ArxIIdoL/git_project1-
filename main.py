import sys
from UI import Ui_MainWindow as MainWindow_Des
from random import randint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, MainWindow_Des):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        for _ in range(randint(2, 6)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            radius, center_x, center_y = randint(5, 30), randint(60, 280), randint(60, 210)
            qp.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec())
