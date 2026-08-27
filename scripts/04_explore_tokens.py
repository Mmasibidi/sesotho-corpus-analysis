"""
Explore the token structure of the Sesotho corpus.

This script is exploratory. It does not modify the raw corpus.
"""

from pathlib import Path
from collections import Counter

corpus_file = Path(
    "data/raw/Autshumato.MonolingualCorpus(Sesotho).v2.1.st.txt"
)

print("Sesotho corpus token exploration")
print("--------------------------------")

if not corpus_file.exists():
    print("ERROR: Corpus file not found.")

else:
    tokens = []

    with corpus_file.open("r", encoding="utf-8") as file:
        for line in file:
            tokens.extend(line.split())

    # Basic token information
    print("Total tokens:", len(tokens))
    print("First 20 tokens:")
    print(tokens[:20])

    # Non-alphabetic tokens
    non_alphabetic_tokens = [
        token for token in tokens
        if not token.isalpha()
    ]

    print("\nTokens containing non-alphabetic characters:",
          len(non_alphabetic_tokens))

    print("First 50 examples:")
    print(non_alphabetic_tokens[:50])

    # Frequency of non-alphabetic tokens
    non_alphabetic_counts = Counter(non_alphabetic_tokens)

    print("\nMost frequent non-alphabetic token types:")
    for token, count in non_alphabetic_counts.most_common(30):
        print(repr(token), ":", count)

    # Hyphen investigation
    hyphen_tokens = [
        token for token in tokens
        if "-" in token
    ]

    print("\nTokens containing hyphens:", len(hyphen_tokens))

    hyphen_counts = Counter(hyphen_tokens)

    print("Most frequent hyphen-containing tokens:")
    for token, count in hyphen_counts.most_common(30):
        print(repr(token), ":", count)

    # Position of hyphens
    leading_hyphen = [
        token for token in hyphen_tokens
        if token.startswith("-")
    ]

    trailing_hyphen = [
        token for token in hyphen_tokens
        if token.endswith("-")
    ]

    internal_hyphen = [
        token for token in hyphen_tokens
        if not token.startswith("-") and not token.endswith("-")
    ]

    print("\nHyphen position:")
    print("Leading hyphen:", len(leading_hyphen))
    print("Trailing hyphen:", len(trailing_hyphen))
    print("Internal hyphen:", len(internal_hyphen))

    # Apostrophe investigation
    apostrophe_tokens = [
        token for token in tokens
        if "'" in token
    ]

    print("\nTokens containing apostrophes:",
          len(apostrophe_tokens))

    apostrophe_counts = Counter(apostrophe_tokens)

    print("Most frequent apostrophe-containing tokens:")
    for token, count in apostrophe_counts.most_common(30):
        print(repr(token), ":", count)

    # Quotation mark investigation
    quotation_tokens = [
        token for token in tokens
        if '"' in token
    ]

    print("\nTokens containing quotation marks:",
          len(quotation_tokens))

    quotation_counts = Counter(quotation_tokens)

    print("Most frequent quotation-containing tokens:")
    for token, count in quotation_counts.most_common(30):
        print(repr(token), ":", count)

    # Capitalisation investigation
    uppercase_tokens = [
        token for token in tokens
        if token.isupper()
    ]

    lowercase_tokens = [
        token for token in tokens
        if token.islower()
    ]

    mixed_case_tokens = [
        token for token in tokens
        if not token.isupper() and not token.islower()
        and any(char.isalpha() for char in token)
    ]

    print("\nCapitalisation:")
    print("Uppercase tokens:", len(uppercase_tokens))
    print("Lowercase tokens:", len(lowercase_tokens))
    print("Mixed/other case tokens:", len(mixed_case_tokens))

    print("\nMost frequent uppercase tokens:")
    uppercase_counts = Counter(uppercase_tokens)

    for token, count in uppercase_counts.most_common(20):
        print(repr(token), ":", count)

    # Unicode character investigation
    character_counts = Counter(
        character
        for token in tokens
        for character in token
    )

    print("\nMost frequent characters:")
    for character, count in character_counts.most_common(50):
        print(repr(character), ":", count)

    # Sentence punctuation investigation
    sentence_punctuation = [".", "?", "!"]

    attached_sentence_punctuation = [
        token for token in tokens
        if len(token) > 1
        and token[-1] in sentence_punctuation
    ]

    standalone_sentence_punctuation = [
        token for token in tokens
        if token in sentence_punctuation
    ]

    print("\nSentence punctuation:")
    print("Standalone sentence punctuation:",
          len(standalone_sentence_punctuation))

    print("Tokens ending in sentence punctuation:",
          len(attached_sentence_punctuation))

    print("\nExamples of tokens ending in sentence punctuation:")
    for token in attached_sentence_punctuation[:30]:
        print(repr(token))