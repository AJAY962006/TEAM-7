const API_URL = "http://127.0.0.1:5000";

export async function fetchSentimentData(productName) {
  const response = await fetch(
    `${API_URL}/analyze/${encodeURIComponent(productName)}`
  );

  if (!response.ok) {
    throw new Error("Product not found");
  }

  return await response.json();
}