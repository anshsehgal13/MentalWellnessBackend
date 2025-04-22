from fastapi import FastAPI
from app.schema import VentPost
from app.model import predict_mental_health
from app.utils import update_user_score, label_map
from app.db import posts_collection

app = FastAPI()

@app.post("/vent")
def submit_post(post: VentPost):
    label = predict_mental_health(post.content)
    label = int(label)  # Ensure it's a native int
    label_str = label_map.get(label, "unknown")

    posts_collection.insert_one({
        "user_id": post.user_id,
        "content": post.content,
        "predicted_tag": label_str
    })

    flag = update_user_score(post.user_id, label)

    return {
        "status": "success",
        "predicted_tag": label_str,
        "suggest_help": flag
    }
