from random import randint


def input_validator(used_attempts, total_attempts):
    while True:
        try:
            prompt = int(
                input(f"Attempt {used_attempts}/{total_attempts} — Enter your guess: ")
            )
            return prompt
        except ValueError:
            print("Must be an integer")


def calculate_score(attempts, used_attempts):
    difficulty_multiplier = 0
    match attempts:
        case 10:
            difficulty_multiplier = 100
        case 7:
            difficulty_multiplier = 150
        case 5:
            difficulty_multiplier = 200

    return (attempts - used_attempts + 1) * difficulty_multiplier


def feedback(actual_number, guessed_number, attempts):
    if guessed_number > actual_number:
        return "📈 Too high! Try lower."
    elif guessed_number < actual_number:
        return "📉 Too low! Try higher."
    else:
        return f"🎉 Correct! You got it in {attempts} attempts!"


def generate_secret_number(last):
    return randint(1, last)
