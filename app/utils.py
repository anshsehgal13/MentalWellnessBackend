from app.db import scores_collection

label_map = {
    0: "anxiety",
    1: "bipolar",
    2: "depression",
    3: "normal",
    4: "personality disorder",
    5: "stress",
    6: "suicidal"
}

WEIGHTS = {
    "anxiety": 2,
    "bipolar": 3,
    "depression": 3,
    "normal": 0,
    "personality disorder": 3,
    "stress": 2,
    "suicidal": 5
}

THRESHOLD = 10

def update_user_score(user_id: str, tag: int) -> bool:
    tag_label = label_map.get(tag, "unknown")
    increment = WEIGHTS.get(tag_label, 1)

    existing = scores_collection.find_one({"user_id": user_id})

    if existing:
        scores = existing["scores"]
        scores[tag_label] = scores.get(tag_label, 0) + increment
        scores_collection.update_one({"user_id": user_id}, {"$set": {"scores": scores}})
    else:
        scores_collection.insert_one({"user_id": user_id, "scores": {tag_label: increment}})
        scores = {tag_label: increment}

    return scores.get(tag_label, 0) >= THRESHOLD
