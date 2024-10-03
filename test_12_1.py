import unittest

from Module_12 import runner


class Runner_test(unittest.TestCase):
    def test_walk(self):
        runner1 = runner.Runner("Марс")
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = runner.Runner("Кузя")
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = runner.Runner("Феликс")
        runner4 = runner.Runner('Барсик')
        for _ in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    unittest.main()
