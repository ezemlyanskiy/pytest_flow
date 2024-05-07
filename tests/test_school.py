import pytest

from source.school import Classroom, Student, Teacher, TooManyStudents


def test_add_student(transfiguration_class):
    new_student = Student('Ginny Weasley')
    transfiguration_class.add_student(new_student)
    assert new_student in transfiguration_class.students


def test_too_many_students(transfiguration_class):
    new_student = Student('Dean Thomas')
    with pytest.raises(TooManyStudents):
        transfiguration_class.add_student(new_student)
        transfiguration_class.add_student('Parvati Patil')


@pytest.mark.parametrize('student_name', ['Ron Weasley', 'Draco Malfoy'])
def test_remove_student(transfiguration_class, student_name):
    transfiguration_class.remove_student(student_name)
    for student in transfiguration_class.students:
        assert student.name != student_name


def test_change_teacher(transfiguration_class):
    new_teacher = 'Alastor Moody'
    transfiguration_class.change_teacher(new_teacher)
    assert transfiguration_class.teacher == new_teacher
