ELLIPSE = 0
RECT = 0
ARC = 0
TRIANGLE = 0
SPHERE = 0
BOX = 0
QUAD = 0
LINE = 0
PI = 3.14


def size(w, h, renderer):
    pass


P2D = 0
P3D = 0
PDF = 0


def arc(a, b, c, d, start, stop):
    '''
    :param a: float
    :param b: float
    :param c: float
    :param d: float
    :param start: float
    :param stop: float
    :return:
    '''
    pass


def background(v0, v1=0, v2=0, v3=0):
    pass


def text(txt, x, y, z_or_box_x, _box_y):
    pass


def camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
    pass


def noFill():
    pass


def translate(x, y, z=0):
    pass


def rotateX(angle):
    pass


def rotateY(angle):
    pass


def rotateZ(angle):
    pass


def box(v0, v1=-1, v2=-1):
    pass


def fill(v0, v1, v2, v3=255):
    pass


def line(v0, v1, v2, v3, v4, v5):
    pass


def stroke(v0, v1, v2, v3=255):
    pass


def noStroke():
    pass


def textSize(v0):
    pass


frameCount = 0


def sin(x):
    return 0


def cos(x):
    return 0


def scale(x, y, z):
    pass


def popMatrix():
    pass


def pushMatrix():
    pass


def max(x, y):
    return x


def saveStrings(filename, data):
    pass


keyCode = 0


def millis():
    return 0


LEFT = 0
CENTER = 0
RIGHT = 0
TOP = 0
BOTTOM = 0
BASELINE = 0


def textAlign(modeX, modeY=BASELINE):
    pass

def rect(a, b, c, d, tl, tr, br, bl):
    pass

mouseX = 0
mouseY = 0
mousePressed = False
