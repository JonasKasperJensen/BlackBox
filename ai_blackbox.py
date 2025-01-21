from transformers import pipeline

class BlackBoxAI:
    def __init__(self, identity):
        self.identity = identity
        self.data = []
        self.ai_agent = pipeline("text-generation", model="gpt2")

    def upload_content(self, content):
        self.data.append(content)
        print(f"Content uploaded to {self.identity}: {content}")

    def generate_response(self, prompt):
        if not self.data:
            return "No data in the Black Box. Please upload content first."
        response = self.ai_agent(prompt, max_length=50, num_return_sequences=1)
        return response[0]["generated_text"]

# Example Usage
box = BlackBoxAI("User_1")
box.upload_content("This is a story about resilience and growth.")
print(box.generate_response("Write a poem about growth."))
