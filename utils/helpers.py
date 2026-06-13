# utils/helpers.py — Utility functions

def sanitize_text(text: str) -> str:
    """Clean up text before passing to TTS."""
    text = text.strip()
    # Remove multiple spaces
    text = " ".join(text.split())
    return text


def chunk_text(text: str, max_chars: int = 500) -> list:
    """
    Split long text into chunks for smoother TTS playback.
    Splits on sentence boundaries where possible.
    """
    if len(text) <= max_chars:
        return [text]

    chunks = []
    sentences = text.replace("!", ".").replace("?", ".").split(".")
    current_chunk = ""

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if len(current_chunk) + len(sentence) < max_chars:
            current_chunk += sentence + ". "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
