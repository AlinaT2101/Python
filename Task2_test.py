#Таценко Алина Дмитриевна 44-22-119 21
import unittest
from unittest.mock import MagicMock
from Task1 import func

class MyTestClasse(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    
    def test1(self):
        res= func(4)
        self.assertEqual(*res,-2.458297933817791)

    def test2(self):
        res= func(0)
        self.assertEqual(*res,0.0)

    def test3(self):
        res = func(0,5)
        self.assertEqual(len(res),2)
        self.assertEqual(res,[0.0, 17.091554636580657])
    
if __name__ == '__main__':
    unittest.main()    
