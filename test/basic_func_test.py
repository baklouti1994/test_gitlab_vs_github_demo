import unittest
from src.Basic import Basic


class TestBasicFunnctions(unittest.TestCase):
    def test_sum(self):
        op = Basic()
        self.assertEqual(op.sum(1,2),3)

    def test_sub(self):
        op = Basic()
        self.assertEqual(op.sub(2,1),1)


    def test_mul(self):
        op = Basic()
        self.assertEqual(op.mul(2,3),6)

    def test_div(self):
        op = Basic()
        self.assertEqual(op.div(3,2),1.5)


if __name__ == '__main__':
    unittest.main