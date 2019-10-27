import unittest
import src.Basic as Basic

class TestBasicFunnctions(unittest.TestCase):

    def test_sum(self):
        op = Basic.Basic()
        self.assertEqual(op.sum(1,2),3)


if __name__ == '__main__':
    unittest.main()