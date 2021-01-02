import math, ctypes

#watch out some mistakes might occure here
def get_polar_coord(x1, y1, length, angle):

    # print("angle : {}".format(angle))
    # print("angle_mod : {}".format(angle % (2 * math.pi)))

    x2 = length * math.cos(angle % (2 * math.pi))
    y2 = length * math.sin(angle % (2 * math.pi))

    # its - because its from top to bottom unlike a normal graph
    return (x2 + x1, y1 - y2)

def get_angle(x1, y1, x2, y2):

    if x2 - x1 == 0:

        if y2 - y1 > 0:
            return 3/2 * math.pi
        else:
            return math.pi / 2

    angle = math.atan((y1 - y2) / (x2 - x1))

    if x2 - x1 < 0:
        if y2 - y1 < 0:
            angle += math.pi
        else:
            angle = math.pi + angle

    else:
        if y2 - y1 > 0:
            angle += 2 * math.pi

    return angle

def get_distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_window_size():

    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
