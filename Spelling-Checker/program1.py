from textblob import TextBlob

a = "cmputr"  # incorrect spelling
print(f"original text: {a}")

b = TextBlob(a)

# prints the corrected spelling
print(f"corrected text: {str(b.correct())}")
