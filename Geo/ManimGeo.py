from manim import *
import numpy as np


def to_degrees(x):
    return x * 360.0 / TAU

def to_radians(x):
    """

    :param x:
    :return: x 的弧度值
    """
    return x * DEGREES


def xy_to_numpy(e: dict):
    return np.array([e['x'], e['y'], 0.0])


def xyz_to_numpy(e: dict):
    return np.array([e['x'], e['y'], e['z']])


def wh_to_numpy(e: dict):
    return np.array([e['w'], e['h'], 0.0])


def ManimPoint2D(x, y) -> Dot:
    return Dot(np.array([x, y, 0.0]))


def ManimPoint(x, y, z) -> Dot:
    return Dot(np.array([x, y, z]))


def ManimLine(start: dict, end: dict) -> Line:
    return Line(
        start=xy_to_numpy(start),
        end=xy_to_numpy(end)
    )


def ManimRect(pos: dict, wh: dict) -> Rectangle:
    """
        创建一个 Rectangle 对象。

        参数：
        - pos (dict): 一个包含位置信息的字典，可能的键有：
            - 'x' (float): 水平方向的位置坐标。
            - 'y' (float): 垂直方向的位置坐标。
        - wh (dict): 一个包含宽度和高度信息的字典，可能的键有：
            - 'width' (float): 矩形的宽度。
            - 'height' (float): 矩形的高度。

        返回：
        - Rectangle：创建的矩形对象。
    """
    return Rectangle(height=wh['h'], width=wh['w']).shift(xy_to_numpy(pos))

def ManimCircleDirect(x, y, radius) -> Circle:
    return ManimCircle({'x':x, 'y':y}, radius)


def ManimCircle(pos: dict, radius) -> Circle:
    """
            创建一个 Circle 对象。

            参数：
            - pos (dict): 一个包含位置信息的字典，可能的键有：
                - 'x' (float): 水平方向的位置坐标。
                - 'y' (float): 垂直方向的位置坐标。
            - radius(float): 圆形半径

            返回：
            - Rectangle：创建的矩形对象。
        """
    return Circle(radius=radius).shift(xy_to_numpy(pos))


def ManimTrace(pos: dict) -> TracedPath:
    return TracedPath(xy_to_numpy(pos)).set_color(RED).scale(0.618)


def ManimFormula(text: str, **kwargs):
    return Text(text=text)
