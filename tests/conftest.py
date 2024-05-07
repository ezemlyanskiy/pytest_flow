import pytest

from source.school import Classroom, Student, Teacher
from source.shapes import Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return Rectangle(5, 6)


@pytest.fixture
def mcgonagall():
    return Teacher('Minerva McGonagall')


@pytest.fixture
def students():
    students_list = [
        'Harry Potter',
        'Hermione Granger',
        'Ron Weasley',
        'Draco Malfoy',
        'Luna Lovegood',
        'Neville Longbottom',
        'Pansy Parkison',
        'Cedric Diggory',
        'Cho Chang',
    ]
    return [Student(name) for name in students_list]


@pytest.fixture
def transfiguration_class(mcgonagall, students):
    return Classroom(mcgonagall, students, 'Transfiguration')
