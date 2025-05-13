from pipelines.text_pipeline import TextPipeline
from hf_api import HFChatbot

class ChatbotEngine:
    def __init__(self):
        self.pipeline = TextPipeline()
        self.chatbot = HFChatbot()

    def chat(self, user_input):
        tokens = self.pipeline.preprocess_text(user_input)
        return self.chatbot.generate_response(user_input)