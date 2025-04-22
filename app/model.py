import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import joblib
import os

model_path = r"C:\Users\anshs\Documents\Mental-Wellness-project\model_files"

# Load the tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)

# Load the model (for PyTorch)
model = DistilBertForSequenceClassification.from_pretrained(model_path)

label_encoder = joblib.load(os.path.join(model_path, "label_encoder.pkl"))
model.eval()

def predict_mental_health(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    return label_encoder.inverse_transform([pred])[0]
