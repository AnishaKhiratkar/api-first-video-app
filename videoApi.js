const BASE_URL = "http://127.0.0.1:5000";

export async function addVideo(data) {
  const res = await fetch(`${BASE_URL}/videos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getVideo(id) {
  const res = await fetch(`${BASE_URL}/videos/${id}`);
  return res.json();
}
