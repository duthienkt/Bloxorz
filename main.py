import time

from InputSheet import INPUTS


def millis():
    return int(round(time.time() * 1000))


startTime = millis()
input_0 = INPUTS[0]

name = "BFS"
output_0 = input_0.BFS()

# name = "DFS"
# output_0 = input_0.DFS()
#
# name = "A*"
# output_0 = input_0.A_Star()

endTime = millis()

print("Time: " + str(endTime - startTime) + "ms")

if output_0 is None:
    print("Solution is not found!")

else:
    print("Solution: " + str(len(output_0)) + "steps")
    stepLog = "Log:"
    for x in output_0:
        if len(x.log) > 0:
            stepLog += x.log[0] + "\n"
    print(stepLog)
