import json  # Import the JSON module to handle JSON files


# load questions from a JSON file
def load_questions(filename):
    # Open the file in read mode
    with open(filename, "r") as file:
        # Load the JSON data from the file and return it
        return json.load(file)


# ask a question and check the answer
def ask_question(question_data):
    # Print the question text
    print(question_data["question"])
    # Loop through the options and print each one
    for option in question_data["options"]:
        print(option)
    # Prompt the user to choose an answer (A, B, or C)
    answer = input("Choose A, B, or C: ").strip().upper()
    # Return True if the user's answer matches the correct answer, otherwise False
    return answer == question_data["answer"]


# save quiz results to a JSON file
def save_results(filename, results):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write the results to the file in JSON format
        json.dump(results, file, indent=4)


# start the quiz
def start_quiz():
    # Load the questions from the "questions.json" file
    questions = load_questions("questions.json")
    # Initialize the count of correct answers
    correct_answers = 0
    # Get the total number of questions
    total_questions = len(questions)
    # Prompt the user to enter their name
    user_name = input("Enter your name: ")

    # Loop through each question in the list of questions
    for question in questions:
        # If the user answers the question correctly, increment the count of correct answers
        if ask_question(question):
            correct_answers += 1
    # Calculate the user's score as a percentage
    score = (correct_answers / total_questions) * 100
    # Print the user's result
    print(
        f"{user_name}, you have {correct_answers} correct answers out of {total_questions}"
    )

    # Try to load existing results from the "results.json" file
    try:
        with open("results.json", "r") as file:
            results = json.load(file)
    # If the file does not exist, create an empty list
    except FileNotFoundError:
        results = []
    # Append the user's result
    results.append({"name": user_name, "score": score})
    # Save the updated results back to the "results.json" file
    save_results("results.json", results)


# Start the quiz
start_quiz()
