import unittest
#from sets import set

import symmetric_diff

class TestSymmDiff(unittest.TestCase):
    def test__pass(self):
        x = set([1,2,3])
        y = set([3,4,5])
        z = x ^ y
        out = symmetric_diff.symm_diff(x,y)
        self.assertEqual(z, out)

    def test__fail(self):
        x = set([1, 2, 3])
        y = set([3, 4, 5])
        z = x | y
        out = symmetric_diff.symm_diff(x, y)
        self.assertNotEqual(z, out)


if __name__ == '__main__':
    unittest.main()