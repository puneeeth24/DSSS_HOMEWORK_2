import random


def generate_random_number(min_value, max_value):
    """
    Generates a random integer within a given range

    Parameters:
    min_value(int): The minimum value of the range
    max_value(int): The maximum value of the range

    Returns:
    int : A random integer within the specified range
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random arithmetic operator(,-,*) 

    Returns:
    str: A randomly chosen arithmetic operator
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem(num1, num2, operator):
    problem = f"{num1} {operator} {num2}"
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    # Start with 3 questions
    total_questions = 1 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    while True:
        num1 = generate_random_number(1, 10)  # calling function generate_random_number()
        num2 = generate_random_number(1, 5)   # calling function generate_random_number()
        operator = generate_random_operator() # calling function generate_random_operator()

        problem, correct_answer = generate_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer")
            continue


        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
            # Increment the total questions for the next iteration
            total_questions += 1
        
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
            break

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
