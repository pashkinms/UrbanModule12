import unittest
import logging
from rt_with_exceptions import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frosen = True
    
    def test_some(self):
        self.assertFalse(False)
            
    def test_name(self):
        try:
            name, speed = 2, 3
            human = Runner(name, speed)
            logging.info('Test is sucsessfully passed')
        except TypeError as exp:            
            logging.warning(f"Неверный тип имени {name}: {exp}")
            self.assertFalse(True)
    
    def test_speed(self):
        try:
            name, speed = 'Ванечка', -10
            human = Runner(name, speed)
            logging.info('Test is sucsessfully passed')
        except ValueError as exp:
            logging.warning(f"Ошибка в значении скорости {speed}: {exp}")
            self.assertFalse(True)
            
    @unittest.skipIf(is_frosen, "Tests are frozen in this case.")
    def test_walk(self):
        human = Runner('Vasya', 5)
        for i in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)
    
    @unittest.skipIf(is_frosen, "Tests are frozen in this case.")
    def test_run(self):
        human = Runner('Vasya',5)
        for i in range(10):
            human.run()
        self.assertEqual(human.distance, 100)
   
    @unittest.skipIf(is_frosen, "Tests are frozen in this case.")
    def test_challenge(self):
        human1 = Runner('Vasilisa',5)
        human2 = Runner('Vasya', 10)
        for i in range(10):
            human1.walk()
            human2.run()
        self.assertNotEqual(human1.distance, human2.distance)
        
class TournamentTest(unittest.TestCase):
    is_frosen = True
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results={}
        return super().setUpClass()
        
    @unittest.skipIf(is_frosen, 'Tests are frozen in this case!')
    def setUp(self) -> None:
        self.runner1 = Runner('Usane', 10)
        self.runner2 = Runner('Andrew', 9)
        self.runner3 = Runner('Nick', 3)
        return super().setUp()
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    @unittest.skipIf(is_frosen, 'Tests are frozen in this case!')
    def test12(self):
        self.tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[2] == self.runner3)    
    
    @unittest.skipIf(is_frosen, 'Tests are frozen in this case!')
    def test13(self):    
        self.tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[2] == self.runner3)
    
    @unittest.skipIf(is_frosen, 'Tests are frozen in this case!')    
    def test123(self):
        self.tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[3] == self.runner3)
    
    @unittest.skipIf(True, 'Tests are frozen in this case!')    
    def test_overun(self):
        self.tournament = Tournament(8, self.runner3, self.runner2, self.runner1)
        self.all_results = self.tournament.start()
        print(self.all_results)
        self.assertTrue(self.all_results[3] == self.runner3) 
        self.assertTrue(self.all_results[2] == self.runner2)
        self.assertTrue(self.all_results[1] == self.runner1)   
        
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')  
        
if __name__ == '__main__':
    
    unittest.main(verbosity=2)
    