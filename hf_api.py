from transformers import pipeline

class HFChatbot:
    def __init__(self, model_name="meta-llama/Llama-2-7b-chat-hf"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate_response(self, prompt):
        return self.generator(prompt, max_length=150)[0]['generated_text']
