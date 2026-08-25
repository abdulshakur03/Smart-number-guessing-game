from utils import input_validator, calculate_score, feedback, generate_secret_number


def main():
    while True:
        play_game()
        restart = play_again()
        if restart == "n":
            print("Thanks for playing!")
            break


def play_game():
    print("Welcome to the Number Guessing Game!")
    max_range, max_attempts = difficulty_selector()
    print()
    used_attempts = 1
    secrete_number = generate_secret_number(max_range)
    total_attempt = max_attempts
    print(f"I'm thinking of a number between 1 and {max_range}.")
    print(f"You have {max_attempts} attempts.")
    print()
    while True:
        valid_input = input_validator(used_attempts, total_attempt)
        print(feedback(secrete_number, valid_input, used_attempts))
        if secrete_number == valid_input:
            score = calculate_score(total_attempt, used_attempts)
            print(f"Your score: {score} points")
            break
        elif secrete_number != valid_input and max_attempts == 1:
            print(f"You Lose\nThe secrete number is: {secrete_number}")
            print("Your score: 0 points")
            break
        max_attempts = max_attempts - 1
        used_attempts = used_attempts + 1
    print()


def difficulty_selector():
    while True:
        try:
            selected_level = int(
                input("Select difficulty:\n[1] Easy\n[2] Medium\n[3] Hard\n")
            )

            match selected_level:
                case 1:
                    return (50, 10)
                case 2:
                    return (100, 7)
                case 3:
                    return (200, 5)
                case _:
                    print("Invalid Input")
        except ValueError:
            print("Choose from 1-3")


def play_again():
    while True:
        user_input = input("Play again? (y/n): ").lower()
        if user_input in ("y", "n"):
            return user_input
        print("Either [y] or [n]")


if __name__ == "__main__":
    main()
