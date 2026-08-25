"""
Create a basic profile of the Sesotho corpus.

This script reads the raw corpus and reports basic
structural information without modifying the corpus.
"""

from pathlib import Path

corpus_file = Path(
    "data/raw/Autshumato.MonolingualCorpus(Sesotho).v2.1.st.txt"
)

print("Sesotho corpus profile")
print("----------------------")

if not corpus_file.exists():
    print("ERROR: Corpus file not found.")
else:
    total_lines = 0
    empty_lines = 0
    non_empty_lines = 0
    total_tokens = 0
    total_tokens = 0 
    unique_tokens = set()

    shortest_line = None
    longest_line = None

    with corpus_file.open("r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            total_tokens += len(line.split())
            unique_tokens.update(line.split())

            line = line.strip()

            if line == "":
                empty_lines += 1
            else:
                non_empty_lines += 1

            if shortest_line is None or len(line) < len(shortest_line):
                    shortest_line = line

            if longest_line is None or len(line) > len(longest_line):
                    longest_line = line

    print("Total lines:", total_lines)
    print("Empty lines:", empty_lines)
    print("Non-empty lines:", non_empty_lines)
    print("Total tokens:", total_tokens)
    print("Unique tokens:", len(unique_tokens))
    print("Shortest line (characters):", len(shortest_line))
    print("Longest line (characters):", len(longest_line))

    print("\nShortest line:")
    print(shortest_line)

    print("\nLongest line:")
    print(longest_line)