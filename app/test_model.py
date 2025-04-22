import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# Load the model and tokenizer
model_path = r"C:\Users\anshs\Documents\Mental-Wellness-project\model_files"
tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model = DistilBertForSequenceClassification.from_pretrained(model_path)

# Example input text (you can replace this with any text)
input_text = "i dont feel like living anymore"

# Tokenize the input text
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Make the prediction
with torch.no_grad():  # Disable gradient calculation
    outputs = model(**inputs)

# Get logits (raw model output)
logits = outputs.logits

# Apply softmax to convert logits to probabilities (if needed)
probabilities = torch.nn.functional.softmax(logits, dim=-1)

# Get the predicted class (argmax)
predicted_class = torch.argmax(probabilities, dim=-1)

# Output the result
print(f"Predicted class: {predicted_class.item()}")
print(f"Probabilities: {probabilities}")
