# Sesotho Corpus Analysis

## Project Overview

This project develops a reproducible computational workflow for the
analysis and preprocessing of a Sesotho monolingual corpus.

The project uses the Autshumato Monolingual Corpus (Sesotho) v2.1 as
the primary corpus.

The initial focus is on understanding the structure and linguistic
characteristics of the corpus before developing a final preprocessing
strategy.

## Corpus

**Corpus:** Autshumato Monolingual Corpus (Sesotho) v2.1

**Raw corpus file:**

`Autshumato.MonolingualCorpus(Sesotho).v2.1.st.txt`

The raw corpus is stored locally and is not committed to this
repository.

## Computational Workflow

The project follows a staged and reproducible workflow:

```text
01_load_corpus.py
        ↓
02_inspect_corpus.py
        ↓
03_profile_corpus.py
        ↓
04_explore_tokens.py
        ↓
05_preprocess_corpus.py
        ↓
Future analysis stages

Markdown
### 01. Load Corpus

`01_load_corpus.py`

Checks that the corpus file exists and establishes the input file for
the computational workflow.

### 02. Inspect Corpus

`02_inspect_corpus.py`

Reports basic corpus metadata without modifying the original corpus.

Current observations include:

- File size
- Number of lines
- Sample corpus lines

### 03. Profile Corpus

`03_profile_corpus.py`

Provides basic structural statistics about the corpus, including:

- Total number of lines
- Empty and non-empty lines
- Total whitespace-delimited tokens
- Number of unique tokens
- Shortest line
- Longest line

### 04. Explore Tokens

`04_explore_tokens.py`

Investigates the structure of tokens before preprocessing.

The exploration includes:

- Non-alphabetic tokens
- Punctuation
- Hyphenated tokens
- Apostrophe-containing tokens
- Quotation marks
- Capitalisation
- Character frequencies
- Sentence punctuation

This stage is exploratory and does not modify the raw corpus.

### 05. Preprocess Corpus

`05_preprocess_corpus.py`

Creates a derived processed version of the corpus.

The current preprocessing approach is deliberately conservative.

The initial implementation investigates the separation of sentence
punctuation while preserving forms that may have linguistic or
lexical significance.

Examples identified in the corpus include:

- Abbreviations: `J.B.`, `H.E.`, `U.S.A.`, `B.A.`
- Hyphenated forms: `COVID-19`, `KwaZulu-Natal`
- Apostrophe-containing forms: `Vuk'uzenzele`
- Numbers and numerical expressions

These observations demonstrate that indiscriminate punctuation removal
could alter potentially meaningful corpus information.

## Initial Corpus Profile

The initial corpus profiling produced the following results:

| Measure | Result |
|---|---:|
| Total lines | 216,854 |
| Empty lines | 0 |
| Non-empty lines | 216,854 |
| Total tokens | 4,600,267 |
| Unique tokens | 72,296 |

The initial token exploration identified:

- 398,040 tokens containing non-alphabetic characters
- 13,918 tokens containing hyphens
- 2,970 tokens containing apostrophes
- 11,110 tokens containing quotation marks

## Preprocessing Principle

The preprocessing strategy is **evidence-based and conservative**.

Rather than applying blanket rules such as removing all punctuation,
the corpus is first examined to determine how punctuation, numbers,
capitalisation, abbreviations, hyphens and apostrophes function in the
data.

The objective is to minimise information loss while producing data
that are suitable for subsequent computational and linguistic
analysis.

Preprocessing decisions will be validated against actual corpus
examples before being treated as final.

## Reproducibility

The computational workflow is version controlled using Git.

The repository records the development of the analysis scripts and
preprocessing decisions.

The raw and processed corpus files are excluded from Git through
`.gitignore`.

This separation allows the computational procedures to be versioned
without unnecessarily distributing corpus data.

## Current Status

Completed:

- Repository setup
- Corpus loading
- Corpus inspection
- Corpus profiling
- Token exploration
- Initial preprocessing investigation
- First conservative preprocessing pass
- Git version control of the workflow

Current methodological focus:

- Refining tokenisation
- Determining appropriate punctuation handling
- Evaluating abbreviations
- Evaluating hyphenated forms
- Evaluating apostrophe-containing forms
- Evaluating numbers and numerical expressions
- Evaluating capitalisation
- Establishing validation criteria for preprocessing

## Next Steps

The next stage is to refine and validate the preprocessing strategy
before proceeding to frequency analysis and other corpus-based
analyses.

Future stages will include:

1. Finalise preprocessing rules.
2. Validate the processed corpus against the raw corpus.
3. Document preprocessing decisions.
4. Develop frequency analysis.
5. Save reproducible analysis results.
6. Conduct further corpus-based linguistic and lexicographic analysis.