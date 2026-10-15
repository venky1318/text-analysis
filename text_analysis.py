
# Text Analysis

import re
from collections import Counter


def analyze_text(text):
    """Calculate word, character, vowel, and repeated-word statistics."""

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Extract words while ignoring punctuation.
    words = re.findall(r"\b[\w']+\b", text.lower())

    # Count vowels in the original text, ignoring letter case.
    vowels = sum(1 for char in text.lower() if char in "aeiou")

    # Count the number of times each word appears.
    word_counts = Counter(words)

    # Keep only words that occur more than once.
    repeated_words = {
        word: count
        for word, count in word_counts.items()
        if count > 1
    }

    return {
        "word_count": len(words),
        "character_count": len(text),
        "vowel_count": vowels,
        "repeated_words": repeated_words,
        "unique_words": len(word_counts)
    }


def display_results(text, results):
    """Display the text and its analysis results."""

    print("\n" + "=" * 52)
    print("                  TEXT ANALYSIS")
    print("=" * 52)

    print("\nOriginal Text:")
    print(text if text.strip() else "(Empty text)")

    print("\n" + "-" * 52)
    print("                  ANALYSIS RESULTS")
    print("-" * 52)

    print(f"Word Count       : {results['word_count']}")
    print(f"Character Count  : {results['character_count']}")
    print(f"Vowel Count      : {results['vowel_count']}")
    print(f"Unique Words     : {results['unique_words']}")

    print("\nRepeated Words:")
    if results["repeated_words"]:
        for word, count in sorted(results["repeated_words"].items()):
            print(f"  {word}: {count} times")
    else:
        print("  No repeated words found.")

    print("=" * 52)


def main():
    # Sample paragraph for analysis
    sample_text = (
        "Python is useful for text analysis. "
        "Python can count words and characters. "
        "Text analysis helps us understand words."
    )

    print("TEXT ANALYSIS PROGRAM")
    print("1. Analyze sample text")
    print("2. Enter your own text")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        text = sample_text
    elif choice == "2":
        text = input("Enter the text to analyze: ")
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")
        return

    try:
        results = analyze_text(text)
        display_results(text, results)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
