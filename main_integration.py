# Initialize synthetic immune system
immune_system = SyntheticImmuneSystem()

# Create and register Black Boxes
box_a = BlackBoxAI("Box_A")
box_b = BlackBoxAI("Box_B")
immune_system.register_box(box_a)
immune_system.register_box(box_b)

# Upload content and simulate AIT
box_a.upload_content("A user's perspective on creativity.")
box_b.upload_content("A user's perspective on innovation.")
print(box_a.generate_response("What drives creativity?"))

# Collaborate through the synthetic immune system
immune_system.collaborate("Box_A", "Box_B", "Shared learning on creativity and innovation.")

# Demonstrate meeting and secure content upload
meet_boxes(box_a, box_b)
content_manager = ContentManager(box_a)
content_manager.upload_secure_content("User's private journal entry.")
