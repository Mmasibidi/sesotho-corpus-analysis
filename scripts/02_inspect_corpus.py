"""
Inspect the Sesotho corpus.

This script reports basic metadata about the corpus
without modifying the original file.
"""

from pathlib import Path

corpus_file = Path(
    "data/raw/Autshumato.MonolingualCorpus(Sesotho).v2.1.st.txt"
)

print("Sesotho corpus inspection")
print("-------------------------")

print("Corpus file:", corpus_file)
print("File exists:", corpus_file.exists())

if corpus_file.exists():
    file_size = corpus_file.stat().st_size

    print("File size (bytes):", file_size)

    with corpus_file.open("r", encoding="utf-8") as file:
        line_count = sum(1 for line in file)

    print("Number of lines:", line_count)

    print("\nFirst five lines of the corpus:")
    print("-------------------------------")

    with corpus_file.open("r", encoding="utf-8") as file:
        for number, line in enumerate(file):
            if number == 5:
                break
            print(line.strip())