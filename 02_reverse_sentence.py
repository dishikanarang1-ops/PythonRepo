"""Reverse the order of words in a sentence."""

def reverse_sentence(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Reversed sentence:", reverse_sentence(sentence))
