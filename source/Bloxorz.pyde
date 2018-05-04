from DSA import Comparator, Heap

__PROCESSING__ = False

if __PROCESSING__:
    from PDefine import *


class IntCmp(Comparator):
    def compare(self, a, b):
        return -a + b


int_h = Heap(IntCmp()).push(101).push(200)


#
# def setup():
#     size(1280, 720, P3D)
#
#
# def draw():
#     background(0)
#     for i in range(2):
#         text(str(int_h.data[0]) + " " + str(int_h.data[1]), 10, 10)

def setup():
    size(100, 100, P3D)
    noFill()


def draw():
    background(204)
    camera(70.0, 35.0, 120.0, 50.0, 50.0, 0.0,
           0.0, 1.0, 0.0)
    translate(50, 50, 0)
    rotateX(-PI / 6)
    rotateY(PI / 3)
    box(45)
