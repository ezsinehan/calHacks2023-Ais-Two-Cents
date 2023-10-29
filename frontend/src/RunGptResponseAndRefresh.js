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

// Inside your component's return statement
return (
  <div>
    <button onClick={runGptResponseAndRefresh}>Refresh Recommendations</button>
    {/* ... rest of your component */}
  </div>
);
