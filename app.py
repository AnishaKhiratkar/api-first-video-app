from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# ✅ ENABLE CORS FOR EVERYTHING
CORS(app, resources={r"/*": {"origins": "*"}})

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["video_db"]
videos_collection = db["videos"]

print("✅ MongoDB connected successfully")

# ------------------------
# GET all videos
# ------------------------
@app.route("/videos", methods=["GET"])
def get_videos():
    videos = []
    for v in videos_collection.find():
        videos.append({
            "id": str(v["_id"]),
            "title": v["title"],
            "video_url": v["video_url"]
        })
    print("✅ All videos query executed")
    return jsonify(videos), 200


# ------------------------
# ADD video (POST)
# ------------------------
@app.route("/videos", methods=["POST", "OPTIONS"])
def add_video():
    if request.method == "OPTIONS":
        # CORS preflight
        return jsonify({"status": "ok"}), 200

    data = request.json
    print("📩 Received data:", data)

    if not data or "title" not in data or "video_url" not in data:
        return jsonify({"error": "Invalid data"}), 400

    result = videos_collection.insert_one({
        "title": data["title"],
        "video_url": data["video_url"]
    })

    print("✅ Video inserted")

    return jsonify({
        "status": "success",
        "id": str(result.inserted_id)
    }), 201


# ------------------------
# RUN SERVER
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
