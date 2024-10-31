# Importing dependencies from transformers
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import sentencepiece
import wikipedia
import re

# Load tokenizer
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-large")

# Load model
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-large")

def summarize(text):
  # Create tokens - number representation of our text
  tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
  # Summarize
  summary = model.generate(**tokens)
  # Decode summary
  decoded = tokenizer.decode(summary[0])
  return decoded

def remove_special_characters(input_string):
    # Define a list of special characters to remove
    special_characters = '!@#$%^&*()_+[]{}|;:,.<>?`~'

    # Use a list comprehension to filter out the special characters
    cleaned_string = ''.join(char for char in input_string if char not in special_characters)

    return cleaned_string

def get_article(name):
  article = wikipedia.page(name)
  text = article.content
  clean_text = remove_special_characters(text)
  return clean_text

while True:
  Input = input("Name article: ")
  try:
    art = get_article(Input)
    if art:
      break
  except:
    print("There is no Article with your prompted name")
summarize(art)