import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name1 = runner.Runner('Lada')
        for i in range(10):
            name1.walk()
        self.assertEqual(name1.distance, 50)

    def test_run(self):
        name2 = runner.Runner('Nikolai')
        for i in range(10):
            name2.run()
        self.assertEqual(name2.distance, 100)

    def test_challenge(self):
        name3 = runner.Runner('Varvara')
        name4 = runner.Runner('Vladislav')
        for i in range(10):
            name3.walk()
            name4.run()
        self.assertNotEqual(name3.distance, name4.distance)

if __name__ == "__main__":
    unittest.main()