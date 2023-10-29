import React, { useState } from "react";

function FileUpload() {
  const [file, setFile] = useState(null);

  const handleFile = (event) => {
    setFile(event.target.files[0]);
    // console.log(event.target.files[0]);
  };

  function handleUpload() {
    const formData = new FormData();
    formData.append("file", file);
    fetch("http://127.0.0.1:5000", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("success", result);
      })
      .catch((error) => {
        console.log("Error: ", error);
      });
  }

  return (
    <div>
      <h2>Upload your mp4</h2>
      <form onSubmit={handleUpload}>
        <input
          type="file"
          name="file"
          accept="video/mp4"
          onChange={handleFile}
        />
        <button>Upload</button>
      </form>
    </div>
  );
}

export default FileUpload;
