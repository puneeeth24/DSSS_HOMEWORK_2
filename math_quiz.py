import random
    # defining a function to generate a random value within a range 
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

    # defining a function to generate a random operator (+, - , *) 
def generate_random_operator():
    """
    Generates a random arithmetic operator(,-,*) 

    Returns:
    str: A randomly chosen arithmetic operator
    """
    return random.choice(['+', '-', '*'])

    # Performing arithmetic operations ( +, -, *) on two randomly generated numbers
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
    # Initialize the score and total questions
    score = 0
    # Initially starting with one question
    total_questions = 1 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # The while loop iterates till user enters corrects answers. 
    # After a wrong answer it exits the loop and prints (correct answers / total questions) 
    while True:
        num1 = generate_random_number(1, 10)  # calling function generate_random_number()
        num2 = generate_random_number(1, 5)   # calling function generate_random_number()
        operator = generate_random_operator() # calling function generate_random_operator()
        # calling function generate_math_problem with arguments num1, num 2, operator\
        # store value of variable answer in correct_answer 
        problem, correct_answer = generate_math_problem(num1, num2, operator) 
        print(f"\nQuestion: {problem}")

        try:
            # Attempt to read an integer from user input
            user_answer = int(input("Your answer: "))
        except ValueError:
            # If a ValueError occurs (e.g., the user enters a non-integer),
            # catch the exception and handle it here
            print("Invalid input. Please enter a valid integer")
            # Continue to the next iteration of the loop (if applicable)
            continue

        # Check user's answer and update the score
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
            #Increment the total questions for the next iteration
            total_questions += 1
                    
        # Display correct answer for incorrect responses and end the game
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
            break
    
    # Display final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
        # Run the math quiz function when the script is executed
    math_quiz()
