class SyntheticImmuneSystem:
    def __init__(self):
        self.network = {}

    def register_box(self, black_box):
        self.network[black_box.identity] = black_box
        print(f"Registered {black_box.identity} in the Synthetic Immune System.")

    def collaborate(self, box1_identity, box2_identity, shared_content):
        box1 = self.network[box1_identity]
        box2 = self.network[box2_identity]
        box1.upload_content(shared_content)
        box2.upload_content(shared_content)
        print(f"Collaboration complete between {box1.identity} and {box2.identity}.")

# Example
immune_system = SyntheticImmuneSystem()
box_a = BlackBoxAI("Box_A")
box_b = BlackBoxAI("Box_B")
immune_system.register_box(box_a)
immune_system.register_box(box_b)
immune_system.collaborate("Box_A", "Box_B", "Shared knowledge: resilience.")
