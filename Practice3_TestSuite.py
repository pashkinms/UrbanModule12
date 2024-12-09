import unittest
import Practice1_RunnerTest
import Practice2_TestTournament


runTour = unittest.TestSuite()

runTour.addTest(unittest.TestLoader().loadTestsFromTestCase(Practice1_RunnerTest.RunnerTest))
runTour.addTest(unittest.TestLoader().loadTestsFromTestCase(Practice2_TestTournament.TournamentTest))

testStarter = unittest.TextTestRunner(verbosity=2)

testStarter.run(runTour)
