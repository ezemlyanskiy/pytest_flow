import math

from source.shapes import Circle


class TestCircle:
    def setup_method(self, method):
        # print(f'Setting up {method}')
        self.circle = Circle(10)
    
    def teardown_method(self, method):
        # print(f'Tearing down {method}')

        del self.circle  # not necessary in this case

    def test_area(self):
        assert self.circle.area() == self.circle.radius * math.pi ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == self.circle.radius * math.pi * 2
    
    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()

    # def test_one(self):
    #     assert True

    # def test_two(self):
    #     assert True
