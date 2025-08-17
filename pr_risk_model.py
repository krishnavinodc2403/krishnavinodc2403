from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import gdown
import os

model_path = "model/codebert-finetuned-risk-checker-v2"
drive_url = "https://drive.google.com/drive/folders/14oo7uVzdTRLFsw2Qn121Uv-KxNaHgaz1?usp=share_link"

if not os.path.exists(model_path):
    os.makedirs(model_path, exist_ok=True)
    gdown.download_folder(drive_url, output=model_path)

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

def predict_risk(pr_text):
    # Tokenize PR text (e.g., code diff, commit message)
    inputs = tokenizer(pr_text, return_tensors="pt", truncation=True, max_length=512)
    
    # Predict
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get predicted class (0=Safe, 1=Risky)
    return torch.argmax(outputs.logits).item()
