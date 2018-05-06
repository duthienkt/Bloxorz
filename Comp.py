from abc import abstractmethod

from Log import Log

__PROCESSING__ = False

if __PROCESSING__:
    from PDefine import *


class Button(object):
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = -1

    def draw(self):
        textAlign(CENTER, CENTER)
        stroke(0)
        if self.state != 1:
            if self.is_hover():
                if mousePressed:
                    self.state = 1
                else:
                    self.state = 2
            else:
                self.state = -1
        else:
            if self.is_hover():
                if not mousePressed:
                    self.on_click()
                    self.state = 2
            else:
                if not mousePressed:
                    self.state = -1

        if self.state == 1:
            fill(50)
        if self.state == 2:
            fill(200)
        if self.state == -1:
            fill(255)
        rect(self.x, self.y, self.w, self.h)
        noStroke()
        fill(0)
        text(self.text, self.x + self.w / 2, self.y + self.h / 2)
        textAlign(LEFT, BASELINE)

    def is_hover(self):
        return (mouseX >= self.x) and (mouseY >= self.y) and (mouseX <= self.x + self.w) and (mouseY <= self.y + self.h)

    @abstractmethod
    def on_click(self):
        Log.notice("click")
