"""Count words that appear more than once in a sentence."""
from collections import Counter
import re


def count_repeated_words(sentence: str) -> dict[str, int]:
    words = re.findall(r"\b[\w']+\b", sentence.lower())
    counts = Counter(words)
    return {word: count for word, count in counts.items() if count > 1}


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    repeated = count_repeated_words(sentence)
    if repeated:
        for word, count in repeated.items():
            print(f"{word}: {count}")
    else:
        print("No repeated words found.")
