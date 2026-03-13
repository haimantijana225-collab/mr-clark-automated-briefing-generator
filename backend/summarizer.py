import re

def summarize_text(text):

    # Clean text
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    # Split sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)

    slides = []
    chunk_size = 4

    for i in range(0, len(sentences), chunk_size):

        chunk = sentences[i:i+chunk_size]

        points = []

        for s in chunk:
            s = s.strip()

            if len(s) > 40:
                points.append(s)

        if points:
            slides.append(points)

    return slides[:6]