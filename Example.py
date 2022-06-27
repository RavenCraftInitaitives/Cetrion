# Example: Smooth Loading

import sys, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Angel, GUI2
from circular_progress import CircularProgress

class SplashScreen(QMainWindow, Angel.Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Import Circular Progress
        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15, 15)
        self.progress.add_shadow(True)
        self.progress.background_color = QColor('white')#QColor(68, 71, 90, 140)
        self.progress.setParent(self.centralwidget)
        self.progress.show()
        self.gradient = 25
        self.max_value = 1
        self.show()

        # Timer
        self.counter = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(25)

        self.worker = HappyBirthday()
        self.worker.p_update.connect(self.setMax)
        self.worker.p_finished.connect(self.stop)
        self.worker.start()
        self.main = MainWindow()

    def setMax(self, value):
        self.max_value = value

    def update(self):
        if self.counter < self.max_value - self.gradient:
            self.counter += 1
        else:
            self.counter += 1 * (self.max_value - self.counter) / self.max_value
        self.progress.set_value(self.counter)
        if self.counter >= 100:
            self.timer.stop()
            self.main.show() # Takes too long
            self.close()

    def stop(self):
        self.max_value = 100
        self.gradient = -1

class MainWindow(QMainWindow, GUI2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class HappyBirthday(QThread):
    p_update = pyqtSignal(int)
    p_finished = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        'Do your stuff here'
        self.p_update.emit(10)
        time.sleep(2)
        self.p_update.emit(30)
        time.sleep(2)
        self.p_update.emit(45)
        time.sleep(2)
        self.p_update.emit(74)
        time.sleep(2)
        self.p_finished.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SplashScreen()
    sys.exit(app.exec())
