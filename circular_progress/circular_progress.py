from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Custom Properties
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.background_color = 0xFFFFFF
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = True

        # Set default size without layout
        self.resize(self.width, self.height)

    def set_value(self, value):
        self.value = value
        self.repaint()

    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    def paintEvent(self, event):

        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width // 2
        value = int(self.value * 360 // self.max_value)

        # Painter
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges

        # Create Rectangle
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # Range Ring
        pen = QPen()
        pen.setColor(QColor(self.background_color))
        pen.setWidth(self.progress_width)
        paint.setPen(pen)
        paint.drawEllipse(margin, margin, width, height)

        # Pen
        pen.setColor(QColor(self.progress_color))

        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # Set ARC/ Circular Progress
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        # End
        paint.end()
