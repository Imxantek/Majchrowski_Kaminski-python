import sys


def count_paragraphs():
    paragraphs = 0
    wasEmpty = True
    for line in sys.stdin:
        stripped = line.strip()
        if stripped != "" and wasEmpty:
            paragraphs += 1
            wasEmpty = False
        elif stripped == "":
            wasEmpty = True

    print(f"Number of paragraphs: {paragraphs}")

if __name__ == "__main__":
    count_paragraphs()