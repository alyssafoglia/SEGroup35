

#Function2
def function2(n1,n2):
    return n1*n2
    


import unittest
class Testing(unittest.TestCase):
#tests for function2

#test 1 - 3*2=6
    def test1(self):
        self.assertEquals(function2(3,2),6)
        
    
 #test 2 - 5*5=25
    def test2(self):
        self.assertEqual(function2(5,5),25)

#test 3 - 4*9=36
    def test3(self):
        self.assertEqual(function2(4,9), 36)

#test 4 - 7*2=14
    def test4(self):
        self.assertEqual(function2(7,2), 14)

#test 5 - 2*1=2
    def test5(self):
        self.assertEqual(function2(2,1), 2)


if __name__ == '__main__':
    unittest.main()