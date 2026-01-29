// import { useState } from "react";
// import { addVideo } from "../api/videoApi";

// export default function AddVideo({ onAdded }) {
//   const [title, setTitle] = useState("");
//   const [url, setUrl] = useState("");

//   const submit = async () => {
//     const res = await addVideo({ title, url });
//     onAdded(res._id);
//     alert("Video Added Successfully");
//   };

//   return (
//     <div>
//       <h3>Add Video</h3>
//       <input
//         placeholder="Title"
//         value={title}
//         onChange={(e) => setTitle(e.target.value)}
//       />
//       <br /><br />
//       <input
//         placeholder="Video URL"
//         value={url}
//         onChange={(e) => setUrl(e.target.value)}
//       />
//       <br /><br />
//       <button onClick={submit}>Add</button>
//     </div>
//   );
// }

import { useState } from "react";
import { addVideo } from "../api/videoApi";

export default function AddVideo({ onAdded }) {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    try {
      setLoading(true);
      console.log("Adding video:", { title, url }); // DEBUG
      
      const res = await addVideo({ title, url });
      console.log("Video added:", res); // DEBUG
      
      onAdded(res._id);
      alert("Video Added Successfully!");
      
      // Clear form
      setTitle("");
      setUrl("");
    } catch (error) {
      console.error("Add video failed:", error); // DEBUG
      alert("Failed to add video: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>Add Video</h3>
      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        disabled={loading}
      />
      <br /><br />
      <input
        placeholder="Video URL or ID"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        disabled={loading}
      />
      <br /><br />
      <button onClick={submit} disabled={loading}>
        {loading ? "Adding..." : "Add Video"}
      </button>
    </div>
  );
}
