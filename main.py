import re

def process_multilingual_text(input_text):
    """
    Cleans, normalizes, and extracts structured vocabulary tokens 
    from raw input text for multilingual analysis.
    """
    cleaned_text = re.sub(r'[^\w\s]', '', input_text.strip())
    words = cleaned_text.split()
    word_freq = {}
    for word in words:
        word_lower = word.lower()
        word_freq[word_lower] = word_freq.get(word_lower, 0) + 1
    
    return {
        "status": "success",
        "total_words": len(words),
        "unique_words": len(word_freq),
        "frequency_map": word_freq
    }

if __name__ == "__main__":
    sample = "Hello world! Learning languages with Python is fast and effective."
    result = process_multilingual_text(sample)
    print("Execution Result:", result)
