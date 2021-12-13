import React /*, { useEffect, useRef } */ from "react";
// import { ReactMediaRecorder } from "react-media-recorder";
import axios from "axios";
import VideoRecorder from "react-video-recorder";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";
import S3FileUpload from "react-s3";
import "./App.css";

const baseURL = "https://jsonplaceholder.typicode.com/posts";
const config = {
  bucketName: "",
  dirName: "VIDEO" /* optional */,
  region: "us-east-1",
  accessKeyId: "",
  secretAccessKey: "",
};

const upload = (file) => {
  S3FileUpload.uploadFile(file, config)
    .then((data) => {
      console.log("data", data);
    })
    .catch((err) => {
      console.log("err", err);
    });
};

const FromVideoRecorder = ({ push }) => {
  const [videoBlob, setVideo] = React.useState(null);
  // console.log("🚀 ~ file: App.js ~ line 146 ~ VideoRecordPage ~ post", post);

  function createVideo(videoBlob) {
    console.log(
      "🚀 ~ file: App.js ~ line 84 ~ createVideo ~ videoBlob",
      videoBlob
    );
    axios
      .post(baseURL, {
        body: videoBlob,
      })
      .then((response) => {
        console.log("🚀 ~ file: App.js ~ line 90 ~ .then ~ response", response);
        // setPost(response.data);
      });
  }
  const myFile = new File([videoBlob], "demo.mp4", { type: "video/mp4" });
  console.log(
    "🚀 ~ file: App.js ~ line 56 ~ FromVideoRecorder ~ myFile",
    myFile
  );
  return (
    <VideoRecorder
      isFlipped={false}
      // isOnInitially
      countdownTime={0}
      mimeType="video/webm;codecs=vp8,opus"
      constraints={{
        audio: true,
        video: {
          width: { exact: 480, ideal: 480 },
          height: { exact: 640, ideal: 640 },
          aspectRatio: { exact: 0.7500000001, ideal: 0.7500000001 },
          resizeMode: "crop-and-scale",
        },
      }}
      onRecordingComplete={(videoBlob) => {
        // Do something with the video...
        console.log("videoBlob", videoBlob);
        setVideo(videoBlob);
        // createVideo(videoBlob);
        upload(myFile.name);
        // push("/videoPreview", { videoBlob });
      }}
      /* renderActions={({
        onStartRecording,
        onStopRecording,
        isCameraOn,
        streamIsReady,
        isVideoInputSupported,
        isInlineRecordingSupported,
        thereWasAnError,
        isConnecting,
        isRunningCountdown,
        isReplayingVideo
      }) => {
        console.log({ isReplayingVideo });
        if (
          (!isInlineRecordingSupported && !isVideoInputSupported) ||
          thereWasAnError ||
          isConnecting ||
          isRunningCountdown ||
          isReplayingVideo
        ) {
          return null;
        }

        return (
          <div style={{ position: "absolute", bottom: "10%" }}>
            <button
              onClick={() => {
                if (isCameraOn && streamIsReady) {
                  onStartRecording();
                }
              }}
            >
              Record
            </button>
            <button onClick={onStopRecording}>Stop</button>
          </div>
        );
      }} */
    />
  );
};

const VideoRecordPage = (props) => {
  console.log("🚀 ~ file: App.js ~ line 162 ~ VideoRecordPage ~ props", props);
  return (
    <div className="App">
      <h1>Video record</h1>

      <div style={{ width: "100%", maxWidth: 480, height: 640 }}>
        <FromVideoRecorder push={props.history.push} />
      </div>

      {/* <div style={{ width: "100%", maxWidth: 480, height: 640 }}>
        <video
          src={window.URL.createObjectURL(props.location.state.videoBlob)}
          width={480}
          height={640}
          autoPlay
          loop
          controls
        />
      </div> */}
    </div>
  );
};

const VideoPreviewPage = (props) => {
  return (
    <div className="App">
      <h1>Video preview</h1>

      {props.location.state && props.location.state.videoBlob && (
        <div style={{ width: "100%", maxWidth: 480, height: 640 }}>
          <video
            src={window.URL.createObjectURL(props.location.state.videoBlob)}
            width={480}
            height={640}
            autoPlay
            loop
            controls
          />
        </div>
      )}
    </div>
  );
};

export default function App() {
  return (
    <Router>
      <Switch>
        <Redirect to="/videoRecord" exact path="/" />
        <Route path="/videoRecord" component={VideoRecordPage} />
        <Route path="/videoPreview" component={VideoPreviewPage} />
      </Switch>
    </Router>
  );
}
