from flask import Blueprint, jsonify
from bson.objectid import ObjectId
from extensions import mongo

video_bp = Blueprint("video_bp", __name__)

@video_bp.route("/videos", methods=["GET"])
def get_all_videos():
    videos = mongo.db.videos.find()  # ✅ matches your collection name

    output = []
    for v in videos:
        output.append({
            "id": str(v["_id"]),
            "title": v.get("title"),
            "description": v.get("description"),
            "youtube_id": v.get("youtube_id"),
            "thumbnail_url": v.get("thumbnail_url"),
            "is_active": v.get("is_active")
        })

    print("✅ All videos query executed")

    return jsonify({
        "status": "success",
        "count": len(output),
        "videos": output
    }), 200