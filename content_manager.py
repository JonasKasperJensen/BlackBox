class ContentManager:
    def __init__(self, black_box):
        self.black_box = black_box

    def upload_secure_content(self, content):
        # Simulate data encryption (for demonstration)
        encrypted_content = f"encrypted({content})"
        self.black_box.upload_content(encrypted_content)

# Example
content_manager = ContentManager(box_a)
content_manager.upload_secure_content("This is private user data.")
