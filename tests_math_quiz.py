import unittest
from math_quiz import generate_random_number, generate_random_operator, generate_math_problem


class TestMathGame(unittest.TestCase):

    def generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def generate_random_operator(self):
        # Test if the generated operator is one of '+', '-' or '*'
        operators = {'+', '-', '*'}
        for _ in range(1000): #test a large numbe of random values
             rand_operator = generate_random_operator()
             self.assertIn(rand_operator, operator)

    def generate_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 6, '-', '8 - 6', 2),               
                (9, 11, '*', '9*11', 99),
                (20, 2, '/', '20/2', 10),
                (0, 9, '+', '0 + 9', 9),  # Test with zero as the first operand
                (7, 0, '*', '7 * 0', 0),  # Test with zero as the second operand
                (-3, 2, '+', '-3 + 2', -1),  # Test with negative numbers
                (10, 2, '/', '10 / 2', 5),  # Test with division (assuming Python 3.x behavior)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
