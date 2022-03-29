import unittest
import functions

class TestFunctions(unittest.TestCase):
    #tests for function1
    def test_removeVowels(self):
        #Removes vowels from 'Hello' to print 'Hll'
        self.assertEqual(functions.removeVowels("Hello"), "Hll", "Should be 'Hll'")  

        #Removes vowels from 'Multiple words in string' to print 'Mltpl wrds n strng'
        self.assertEqual(functions.removeVowels("Multiple words in string"), "Mltpl wrds n strng", "Should be 'Mltpl wrds n strng'")
        
        #Tries to remove vowels from integer and throws error
        with self.assertRaises(TypeError):  
            result = functions.removeVowels(456)
        
        #Takes a string of only vowels in both upper and lower case and returns an empty string
        self.assertEqual(functions.removeVowels("uiooaeUIoUAEUOIaeuioiouae"), "", "Should be ''") 
        
        #Takes an empty string and returns an empty string
        self.assertEqual(functions.removeVowels(""), "", "Should be ''")   
       
        #Takes a string with no vowels and returns the smae string
        self.assertEqual(functions.removeVowels("Cmptrscnc"), "Cmptrscnc", "Should be 'Cmptrscnc'")
    #tests for function2
    def test_multiply(self):
        self.assertEqual(functions.multiply(3,2),6)  #test 1 - 3*2=6
        self.assertEqual(functions.multiply(5,5),25)  #test 2 - 5*5=25
        self.assertEqual(functions.multiply(4,9), 36) #test 3 - 4*9=36
        self.assertEqual(functions.multiply(7,2), 14) #test 4 - 7*2=14
        self.assertEqual(functions.multiply(2,1), 2)  #test 5 - 2*1=2

if __name__ == '__main__':
    unittest.main()

   