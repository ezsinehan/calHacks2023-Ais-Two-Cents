import React, { useEffect, useState } from "react";

function RecommendationsComponent() {
  const [recommendations, setRecommendations] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/get_recommendations")
      .then((response) => response.json())
      .then((data) => {
        setRecommendations(data.recommendations);
      });
  }, []);

  // Split the string into an array of recommendations based on newlines
  const recList = recommendations
    ? recommendations.split("\n").filter((rec) => rec.trim() !== "")
    : [];

  async function runGptResponseAndRefresh() {
    // Run gptresponse.py through Flask
    const response = await fetch("http://127.0.0.1:5000/run_gpt_response", {
      method: "POST",
    });
    const data = await response.json();

    if (data.status === "success") {
      // Refresh recommendations
      fetch("http://127.0.0.1:5000/get_recommendations")
        .then((response) => response.json())
        .then((data) => {
          setRecommendations(data.recommendations);
        });
    } else {
      console.error("Failed to run gptresponse.py");
    }
  }

  return (
    <div>
      <h1>Recommendations Made Using Audience Emotion and Sample Text</h1>
      <ul>
        {recList.map((rec, index) => (
          <li key={index}>{rec.trim()}</li>
        ))}
      </ul>
      <button onClick={runGptResponseAndRefresh}>
        Refresh Recommendations
      </button>
    </div>
  );
}

export default RecommendationsComponent;
