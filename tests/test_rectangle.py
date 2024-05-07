# class TestRectangle:
#     def setup_method(self):
#         self.rectangle = Rectangle(10, 20)
    
#     def test_area(self):
#         assert self.rectangle.area() == 10 * 20
    
#     def test_perimeter(self):
#         assert self.rectangle.perimeter() == 2*10 + 2*20


def test_area(my_rectangle):
    # rectangle = Rectangle(10, 20)
    # assert rectangle.area() == 10 * 20

    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    # rectangle = Rectangle(10, 20)
    # assert rectangle.perimeter() == 2*10 + 2*20

    assert my_rectangle.perimeter() == 2*10 + 2*20


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
