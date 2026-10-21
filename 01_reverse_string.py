"""Reverse a string."""

def reverse_string(text: str) -> str:
    return text[::-1]
# run the file

if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))
