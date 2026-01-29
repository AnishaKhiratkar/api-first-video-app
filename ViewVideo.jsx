import { useEffect, useState } from "react";
import { getVideo } from "../api/videoApi";

export default function ViewVideo({ videoId }) {
  const [video, setVideo] = useState(null);

  useEffect(() => {
    if (videoId) {
      getVideo(videoId).then(setVideo);
    }
  }, [videoId]);

  if (!video) return null;

  return (
    <div>
      <h3>Video Details</h3>
      <p><b>Title:</b> {video.title}</p>
      <p><b>URL:</b> {video.url}</p>
    </div>
  );
}
