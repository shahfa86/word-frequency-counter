def word_frequency(text):
    """
    Function to count the frequency of words in a given text.
    Returns a dictionary with words as keys and their frequency as values, sorted in descending order.
    """
    # Convert text to lowercase to ensure case insensitivity
    text = text.lower()
    
    # Remove punctuation from the text
    for char in ".,!?;:\"'()[]{}-_":
        text = text.replace(char, "")
    
    # Split the text into words
    words = text.split()
    
    # Initialize an empty dictionary to store word frequencies
    frequency = {}
    
    # Loop through each word and count occurrences
    for word in words:
        if word in frequency:
            frequency[word] += 1  # Increment count if word exists
        else:
            frequency[word] = 1  # Add word with initial count of 1
    
    # Sort the dictionary by frequency in descending order
    sorted_frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_frequency
  
print(word_frequency("Hello world! Hello, Python programmer."))
