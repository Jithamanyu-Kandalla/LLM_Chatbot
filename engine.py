from pipelines.text_pipeline import text_pipelines
from hf_api import HFChatbot

class ChatbotEngine:
    def __init__(self):
        self.pipeline = text_pipelines()
        self.chatbot = HFChatbot()

    def chat(self, user_input):
        tokens = self.pipeline.preprocess_text(user_input)
        return self.chatbot.generate_response(user_input)