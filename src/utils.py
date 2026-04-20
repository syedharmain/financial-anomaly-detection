def convert_labels(pred):
    # Convert -1 (fraud) → 1, and 1 (normal) → 0
    return [1 if x == -1 else 0 for x in pred]