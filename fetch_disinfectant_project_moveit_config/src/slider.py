#!/usr/bin/env python3


import sys
import math
from PyQt5.QtWidgets import (QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication,  QSlider, QLabel)
from PyQt5.QtCore import Qt


class SliderDisplay(QWidget):

    def __init__(self, name, min, max, ticks, dec = 0, fraction = 0):
        super(SliderDisplay, self).__init__()
        self.name  = name
        self.min   = min
        self.max   = max
        self.ticks = ticks
        self.dec   = dec
        self.fraction = fraction
        self.val   = 1.0/self.ticks


        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.min)
        self.slider.setMaximum(self.ticks)
        self.label = QLabel(self.name + ' {}'.format(1.0/self.ticks))
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.slider)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.slider.valueChanged.connect(self.v_change)
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def v_change(self):
        if self.fraction == 0:
            self.val = float(self.slider.value())/self.ticks*self.max
            sig = str(int(math.log10(self.ticks)))
            string = '{0}: {1:.' + str(self.dec) +'f}'
            self.label.setText(string.format(self.name,self.val))
        else:
            self.val = float(self.slider.value())/self.ticks*self.max/(10**self.fraction)
            sig = str(int(math.log10(self.ticks)))
            string = '{0}: {1:.' + str(self.dec) +'f}'
            self.label.setText(string.format(self.name,self.val))

    def value(self):
        return self.val
        

def main_f(name, min, max, ticks, dec = 0):
    app = QApplication(sys.argv)
    ex = SliderDisplay(name, min, max, ticks, dec)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_f('Try', 0, 1, 100, 2)
