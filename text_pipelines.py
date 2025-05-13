from transformers import AutoTokenizer

class TextPipeline:
    def __init__(self, model_name="meta-llama/Llama-2-7b-chat-hf"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def preprocess_text(self, text):
        tokens = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        return tokens
