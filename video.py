def video_schema(title, description, youtube_id, thumbnail_url):
    return {
        "title": title,
        "description": description,
        "youtube_id": youtube_id,
        "thumbnail_url": thumbnail_url,
        "is_active": True
    }
