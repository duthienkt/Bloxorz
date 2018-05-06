from Comp import Button
from InputSheet import INPUTS
from Log import Log

__PROCESSING__ = False

if __PROCESSING__:
    from PDefine import *

Log.notice("LOXORZ")
startTime = millis()
input_0 = INPUTS[0]

#
# name = "BFS"
# output_0 = input_0.BFS()
#
name = "DFS"
output_0 = input_0.DFS()
#
# name = "A*"
# output_0 = input_0.A_Star()



endTime = millis()

Log.mess(name)
Log.notice("Time: " + str(endTime - startTime) + "ms")



if output_0 is None:
    Log.error("Solution is not found!")
    drawing_state = input_0
else:
    drawing_state = output_0[0]
    Log.notice("Solution: " + str(len(output_0)) + "steps")
output_frame_id = 0


class PreviousButton(Button):
    def __init__(self):
        Button.__init__(self, "PREV", 1100 - 70, 10, 60, 20)

    def on_click(self):
        global drawing_state
        global output_frame_id
        if output_0 is None:
            return
        if output_frame_id > 0:
            output_frame_id -= 1
            drawing_state = output_0[output_frame_id]


class NextButton(Button):
    def __init__(self):
        Button.__init__(self, "NEXT", 1100, 10, 60, 20)

    def on_click(self):
        global drawing_state
        global output_frame_id
        if output_0 is None:
            return
        if output_frame_id < len(output_0) - 1:
            output_frame_id += 1
            drawing_state = output_0[output_frame_id]


previous_button = PreviousButton()
next_button = NextButton()


def setup():
    size(1208, 700, P3D)
    fill(255, 0, 0)


def draw_axis():
    stroke(255, 0, 0)
    line(0, 0, 0, 10, 0, 0)
    stroke(0, 255, 0)
    line(0, 0, 0, 0, 10, 0)
    stroke(0, 0, 255)
    line(0, 0, 0, 0, 0, 10)


def draw():
    background(180)
    pushMatrix()
    global drawing_state
    distance_ratio = max(drawing_state.m, drawing_state.n) / 3
    camera(50 * cos(-PI / 4 * 0) * distance_ratio, 70 * distance_ratio, 50 * sin(-PI / 4 * 0) * distance_ratio,
           drawing_state.m * 5,
           0.0, drawing_state.n * 5,
           0.0, -1.0, 0.0)
    draw_axis()
    # drawing_state = drawing_state.clone()
    if drawing_state is not None:
        drawing_state.draw()
    popMatrix()
    Log.draw()
    previous_button.draw()
    next_button.draw()


def keyPressed():
    Log.mess(keyCode)
    global drawing_state
    v = drawing_state.clone()
    if keyCode == 38:
        v.move_up()
    if keyCode == 40:
        v.move_down()
    if keyCode == 37:
        v.move_left()
    if keyCode == 39:
        v.move_right()
    if v.is_ok():
        drawing_state = v

    if keyCode == 83:
        Log.save("Log_" + str(millis()) + ".txt")
