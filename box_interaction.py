def meet_boxes(box1, box2):
    print(f"{box1.identity} is meeting {box2.identity}.")
    shared_experience = f"Shared interaction: {box1.identity} + {box2.identity}"
    box1.upload_content(shared_experience)
    box2.upload_content(shared_experience)
    print(f"Experience recorded in both boxes: {shared_experience}")

# Example
meet_boxes(box_a, box_b)
