import string

# Step 1: Define sentiment lexicons
positive_words = {"happy", "great", "good", "awesome", "fantastic", "love", "excellent", "joy", "amazing"}
negative_words = {"sad", "bad", "terrible", "awful", "hate", "horrible", "worst", "angry", "upset"}

# Step 2: Get user input
sentence = input("Enter a sentence: ")

# Step 3: Preprocess the input
# - Lowercase
# - Remove punctuation
# - Split into words (tokenize)
sentence = sentence.lower()
sentence = sentence.translate(str.maketrans('', '', string.punctuation))
words = sentence.split()

# Step 4: Rule-based matching
positive_count = sum(1 for word in words if word in positive_words)
negative_count = sum(1 for word in words if word in negative_words)

# Step 5: Sentiment classification
if positive_count > negative_count:
    sentiment = "Positive"
elif negative_count > positive_count:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Step 6: Output the result
print(f"Sentiment: {sentiment}")
