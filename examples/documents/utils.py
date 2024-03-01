from typing import List

from zep_python.document import Document


def naive_split_text(text: str, max_chunk_size: int):
    """Naive text splitter chunks document into chunks of max_chunk_size,
    using paragraphs and sentences as guides."""
    chunks = []

    # remove extraneous whitespace
    text = " ".join(text.split())
    # split into paragraphs
    paragraphs = text.split("\n\n")

    # clean up paragraphs
    paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 0]

    for paragraph in paragraphs:
        if 0 > len(paragraph) <= max_chunk_size:
            chunks.append(paragraph)
        else:
            sentences = paragraph.split(". ")
            current_chunk = ""

            for sentence in sentences:
                if len(current_chunk) + len(sentence) > max_chunk_size:
                    chunks.append(current_chunk)
                    current_chunk = sentence
                else:
                    current_chunk += ". " + sentence

            chunks.append(current_chunk)

    return chunks


def read_chunk_from_file(file: str, chunk_size: int):
    with open(file, "r") as f:
        text = f.read()

    chunks = naive_split_text(text, chunk_size)

    print(
        f"Splitting text into {len(chunks)} chunks of max size"
        f" {chunk_size} characters."
    )

    return chunks


def print_results(results: List[Document]):
    for result in results:
        print(result.content, result.metadata, " -> ", result.score, "\n")
