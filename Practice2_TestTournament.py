import runner_and_tournament
import unittest
import pprint

class TournamentTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results={}
        return super().setUpClass()
        
    
    def setUp(self) -> None:
        self.runner1 = runner_and_tournament.Runner('Usane', 10)
        self.runner2 = runner_and_tournament.Runner('Andrew', 9)
        self.runner3 = runner_and_tournament.Runner('Nick', 3)
        return super().setUp()
    
    @classmethod
    def tearDownClass(cls) -> None:
        pprint.pprint(cls.all_results)
        return super().tearDownClass()
    
    def test12(self):
        self.tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[2] == self.runner3)    
    
    
    def test13(self):    
        self.tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[2] == self.runner3)
        
    def test123(self):
        self.tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[3] == self.runner3)
        
    def test_overun(self):
        self.tournament = runner_and_tournament.Tournament(8, self.runner3, self.runner2, self.runner1)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[3] == self.runner3) 
        self.assertTrue(self.all_results[2] == self.runner2)
        self.assertTrue(self.all_results[1] == self.runner1)   
if __name__ == '__main__':
        unittest.main()
        
    
    