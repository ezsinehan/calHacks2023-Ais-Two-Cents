import React from "react";
import video from "./video.mp4";

class VideoPlayer extends React.Component {
  render() {
    return (
      <div>
        <video controls width="640" height="360">
          <source src={video} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    );
  }
}

export default VideoPlayer;
