import unittest
from math_quiz import generate_random_number, generate_random_operator, generate_math_problem

# Define a test class for the Math Quiz functions
class TestMathQuizFunctions(unittest.TestCase):

    # Test the generate_random_number function
    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    # Test the generate_random_operator function
    def test_generate_random_operator(self):
        # Test if the generated operator is one of '+', '-', or '*'
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    # Test the generate_math_problem function
    def test_generate_math_problem(self):
        # Test cases to check the correctness of generate_math_problem
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 1, '*', '4 * 1', 4),
            (5, 2, '+', '5 + 2', 7),
            (8, 6, '-', '8 - 6', 2),               
            (9, 7, '*', '9*7', 63),
        ]

        # Iterate over each test case
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # Generate a math problem using the generate_math_problem function
            problem, answer = generate_math_problem(num1, num2, operator)

            # Compare the generated problem with the expected problem
            self.assertEqual(problem, expected_problem)

            # Compare the generated answer with the expected answer
            self.assertEqual(answer, expected_answer)

# Run the tests if the script is executed
if __name__ == "__main__":
    unittest.main()
