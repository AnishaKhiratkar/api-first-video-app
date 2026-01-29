from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from extensions import mongo

dashboard_bp = Blueprint("dashboard", __name__)

# ---------- Dashboard ----------
@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    videos = list(mongo.db.videos.find({"is_active": True}))

    result = []
    for v in videos:
        result.append({
            "id": str(v["_id"]),
            "title": v["title"],
            "description": v["description"],
            "thumbnail_url": v["thumbnail_url"]
        })

    print("✅ Dashboard query executed")

    return jsonify({
        "status": "success",
        "count": len(result),
        "videos": result
    })


# ---------- Get Single Video ----------
@dashboard_bp.route("/video/<video_id>", methods=["GET"])
def get_video(video_id):
    try:
        video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})

        if not video:
            return jsonify({"status": "error", "message": "Video not found"}), 404

        print("✅ Single video query executed")

        return jsonify({
            "status": "success",
            "video": {
                "id": str(video["_id"]),
                "title": video["title"],
                "description": video["description"],
                "thumbnail_url": video["thumbnail_url"]
            }
        })

    except Exception:
        return jsonify({"status": "error", "message": "Invalid video ID"}), 400


# ---------- ADD VIDEO (NEW STEP) ----------
@dashboard_bp.route("/video", methods=["POST"])
def add_video():
    data = request.json

    required_fields = ["title", "description", "youtube_id"]
    for field in required_fields:
        if field not in data:
            return jsonify({"status": "error", "message": f"{field} is required"}), 400

    video = {
        "title": data["title"],
        "description": data["description"],
        "youtube_id": data["youtube_id"],
        "thumbnail_url": f"https://img.youtube.com/vi/{data['youtube_id']}/hqdefault.jpg",
        "is_active": True
    }

    result = mongo.db.videos.insert_one(video)

    print("✅ Video inserted successfully")

    return jsonify({
        "status": "success",
        "video_id": str(result.inserted_id)
    }), 201
