
import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    
    def test_walk(self):
        human = Runner('Vasya')
        for i in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)
    
    def test_run(self):
        human = Runner('Vasya')
        for i in range(10):
            human.run()
        self.assertEqual(human.distance, 100)
    
    def test_challenge(self):
        human1 = Runner('Vasilisa')
        human2 = Runner('Vasya')
        for i in range(10):
            human1.walk()
            human2.run()
        self.assertNotEqual(human1.distance, human2.distance)
        
if __name__ == '__main__':
    unittest.main()
    