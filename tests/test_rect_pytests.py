import pytest
from src.math.line_segment import LineSegment
from src.math.vector2 import Vector2
from src.math.rect import Rect


def test_edges():
    rect = Rect(10, 10, 20, 20)
    edges = [
            LineSegment((10, 10), (30, 10)),
            LineSegment((30, 10), (30, 30)),
            LineSegment((30, 30), (10, 30)),
            LineSegment((10, 30), (10, 10)),
        ]
    for i in range(4):
        assert edges[i] == rect.edges[i], "Asserting: "+str(edges[i] == rect.edges[i])#str(edges[i])+" "+str(rect.edges[i])


def test_intersect_line():
    line = LineSegment(Vector2(0, 0), Vector2(10, 10))
    rect = Rect(5, 5, 11, 11)
    assert rect.intersect_line(line) == Vector2(5, 5)


def test_intersect_line2():
    line = LineSegment(Vector2(0, 0), Vector2(5, 5))
    rect = Rect(5, 5, 11, 11)
    assert rect.intersect_line(line) == Vector2(5, 5)


def test_intersect_line3():
    line = LineSegment(Vector2(0, 0), Vector2(3, 3))
    rect = Rect(5, 5, 11, 11)
    assert rect.intersect_line(line) is None


def test_intersect_line4():
    line = LineSegment(Vector2(0, 0), Vector2(-5, -5))
    rect = Rect(-5, -5, 11, 11)
    assert rect.intersect_line(line) == Vector2(-5, -5)


def test_intersect_line5():
    line = LineSegment(Vector2(0, 5), Vector2(13, 5))
    rect = Rect(5, 0, 11, 11)
    assert rect.intersect_line(line) == Vector2(5, 5)
