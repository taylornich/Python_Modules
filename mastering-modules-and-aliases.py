import text_utils

def main():
    user_string = input("Enter a string: ")

    reversed_input = text_utils.reverse(user_string)
    print(f"Your reversed string: {reversed_input}")

    capitalized_input = text_utils.capitalize(user_string)
    print(f"Your capitalized string: {capitalized_input}")

if __name__ == "__main__":
    main()
