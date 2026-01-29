import { useState, useEffect } from "react";

const API_URL = "http://127.0.0.1:5000";

function App() {
  const [title, setTitle] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [videos, setVideos] = useState([]);
  const [error, setError] = useState("");

  // Fetch videos
  const fetchVideos = async () => {
    try {
      const res = await fetch(`${API_URL}/videos`);
      const data = await res.json();
      setVideos(data);
    } catch (err) {
      setError("❌ Cannot connect to backend server");
    }
  };

  useEffect(() => {
    fetchVideos();
  }, []);

  // Add video
  const addVideo = async () => {
    setError("");
    try {
      const res = await fetch(`${API_URL}/videos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: title,
          video_url: videoUrl,
        }),
      });

      if (!res.ok) throw new Error("Failed");

      setTitle("");
      setVideoUrl("");
      fetchVideos();
    } catch (err) {
      setError("❌ Cannot connect to backend server");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Video Dashboard</h1>

      <h3>Add Video</h3>
      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <br /><br />
      <input
        placeholder="Video URL or ID"
        value={videoUrl}
        onChange={(e) => setVideoUrl(e.target.value)}
      />
      <br /><br />
      <button onClick={addVideo}>Add Video</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h3>Videos</h3>
      <ul>
        {videos.map((v) => (
          <li key={v.id}>{v.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
