"""Reverse a string."""

def reverse_string(text: str) -> str:
    return text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))
