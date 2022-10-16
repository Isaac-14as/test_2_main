from re import M
import unittest
from main import Matrix

class TestMatrix(unittest.TestCase):

    def test_sub(self):
        a = [[1,2,3], [4,5,6], [7,8,9]]
        b = [[1,2,3], [4,5,6]]
        a = Matrix(a)
        b = Matrix(b)
        self.assertEqual((a - b), "Матрицы отличаются размерностью")
        c = [[1,2,3], [4,5,6], [7,8,9]]
        c = Matrix(c)
        answer = [[0,0,0], [0,0,0], [0,0,0]]
        self.assertEqual(getattr((a - c), 'matrix_list'), getattr(Matrix(answer), 'matrix_list'))
    

    def test_add(self):
        a = [[1,2,3], [4,5,6], [7,8,9]]
        b = [[1,2,3], [4,5,6]]
        a = Matrix(a)
        b = Matrix(b)
        self.assertEqual((a + b), "Матрицы отличаются размерностью")
        c = [[1,2,3], [4,5,6], [7,8,9]]
        c = Matrix(c)
        answer = [[2,4,6], [8,10,12], [14,16,18]]
        self.assertEqual(getattr((a + c), 'matrix_list'), getattr(Matrix(answer), 'matrix_list'))
    
    def test_mul(self):
        a = [[1,2,3], [4,5,6], [7,8,9]]
        b = [[1,2,3], [4,5,6]]
        a = Matrix(a)
        b = Matrix(b)
        self.assertEqual((a * b), "Кол-во столбцов первой матрицы не равно кол-ву строк второй")
        c = [[1,2], [4,5], [7,8]]
        c = Matrix(c)
        answer = [[30,36], [66, 81], [102,126]]
        print((a * c))
        self.assertEqual(getattr((a * c), 'matrix_list'), getattr(Matrix(answer), 'matrix_list'))

    def test_truediv(self):
        a = [[5,10,15], [20,25,30], [35,40,45]]
        a = Matrix(a)
        self.assertEqual((a / 0), "Невозможно деление на 0")
        answer = [[1,2,3], [4,5,6], [7,8,9]]
        self.assertEqual(getattr((a / 5), 'matrix_list'), getattr(Matrix(answer), 'matrix_list'))