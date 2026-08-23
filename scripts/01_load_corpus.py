"""
Load the Sesotho corpus.

This script is part of the reproducible computational workflow
for the Sesotho Corpus Analysis project.
"""

from pathlib import Path

corpus_file = Path(
    "data/raw/Autshumato.MonolingualCorpus(Sesotho).v2.1.st.txt"
)

print("Sesotho corpus analysis project")
print("Corpus file:", corpus_file)
print("File exists:", corpus_file.exists())