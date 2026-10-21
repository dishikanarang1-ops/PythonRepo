"""Find the first number in a string."""
import re


def find_first_number(text: str):
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return match.group() if match else None


if __name__ == "__main__":
    text = input("Enter text containing a number: ")
    number = find_first_number(text)
    print("First number:", number if number is not None else "No number found")
