"""Remove duplicate items from a list while preserving order."""

def remove_duplicates(items: list) -> list:
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    raw = input("Enter items separated by commas: ")
    items = [item.strip() for item in raw.split(",")]
    print("Without duplicates:", remove_duplicates(items))
