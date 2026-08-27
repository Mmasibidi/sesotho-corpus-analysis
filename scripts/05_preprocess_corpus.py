"""
Preprocess the Sesotho corpus.

This script creates a processed version of the corpus
without modifying the original raw corpus.

Preprocessing principles:
- Preserve the raw corpus.
- Preserve case at this stage.
- Preserve numbers.
- Preserve hyphenated forms.
- Preserve embedded apostrophes.
- Preserve abbreviations.
- Separate sentence punctuation from ordinary words
  where this can be done safely.
"""

from pathlib import Path
import re


# Input: original raw corpus
raw_file = Path(
    "data/raw/Autshumato.MonolingualCorpus(Sesotho).v2.1.st.txt"
)

# Output: derived processed corpus
processed_file = Path(
    "data/processed/Autshumato.Sesotho.processed.v2.txt"
)


def separate_sentence_punctuation(token):
    """
    Separate final ? or ! from ordinary tokens.

    A final full stop is handled more cautiously because
    the corpus contains abbreviations such as J.B., H.E.,
    U.S.A., B.A. and P.O.Box.
    """

    # Question mark and exclamation mark
    if len(token) > 1 and token[-1] in "?!":
        return [token[:-1], token[-1]]

    # Full stop
    if len(token) > 1 and token.endswith("."):

        # Do not split abbreviation-like forms containing
        # more than one full stop.
        if token.count(".") > 1:
            return [token]

        # Do not split single-letter forms such as A. or B.
        if len(token) == 2 and token[0].isalpha():
            return [token]

        # Otherwise separate the final full stop.
        return [token[:-1], "."]

    return [token]


print("Sesotho corpus preprocessing")
print("-----------------------------")

if not raw_file.exists():
    print("ERROR: Raw corpus file not found.")

else:
    # Make sure the processed directory exists
    processed_file.parent.mkdir(parents=True, exist_ok=True)

    total_lines = 0
    total_tokens_before = 0
    total_tokens_after = 0

    with raw_file.open("r", encoding="utf-8") as infile, \
         processed_file.open("w", encoding="utf-8") as outfile:

        for line in infile:
            total_lines += 1

            # Initial whitespace tokenisation
            tokens = line.split()
            total_tokens_before += len(tokens)

            processed_tokens = []

            for token in tokens:
                processed_tokens.extend(
                    separate_sentence_punctuation(token)
                )

            total_tokens_after += len(processed_tokens)

            # Write processed tokens as a space-separated line
            outfile.write(" ".join(processed_tokens) + "\n")

    print("Processing complete.")
    print("Raw corpus:", raw_file)
    print("Processed corpus:", processed_file)
    print("Total lines:", total_lines)
    print("Tokens before preprocessing:", total_tokens_before)
    print("Tokens after preprocessing:", total_tokens_after)