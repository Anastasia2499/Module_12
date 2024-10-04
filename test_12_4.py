import logging
import runner_tournament
import unittest
import traceback


class Runner_test(unittest.TestCase):

    def test_walk(self):
        try:
            runner1 = runner_tournament.Runner("Марс", -20)
            for _ in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning(f"Неверная скорость для Runner")
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            runner2 = runner_tournament.Runner(123)
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner')
            logging.warning(traceback.format_exc())

    def test_challenge(self):
        runner3 = runner_tournament.Runner("Феликс")
        runner4 = runner_tournament.Runner('Барсик')
        for _ in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
