import "./App.css";
import React from "react";
import ReactDOM from "react-dom/client";
import FileUpload from "./FileUpload";
import reportWebVitals from "./reportWebVitals";
import VideoPlayer from "./VideoPlayer";
import RecommendationsComponent from "./RecommendationsComponent";
import SampleText from "./SampleText";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <div>
    {/* <FileUpload /> */}
    <VideoPlayer />
    <SampleText />
    <RecommendationsComponent />
  </div>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
