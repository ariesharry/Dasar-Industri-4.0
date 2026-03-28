import streamlit as st
import cv2
import av
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode

import os
from twilio.rest import Client
import streamlit as st

@st.cache_resource
def get_ice_servers():
    """Fetch TURN servers from Twilio (fallback to Google STUN if credentials missing)."""
    try:
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    except KeyError:
        st.warning("Twilio credentials not found. Falling back to free STUN server. This may fail on Streamlit Cloud.")
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    client = Client(account_sid, auth_token)
    token = client.tokens.create()
    return token.ice_servers

# Load YOLO model (cached for performance)
@st.cache_resource
def load_model():
    return YOLO('yolov8n.pt')  # You can change to 'yolov8s.pt', etc.

model = load_model()

class ObjectDetectionProcessor(VideoProcessorBase):
    def __init__(self):
        self.model = model

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Convert frame to numpy array (BGR)
        img = frame.to_ndarray(format="bgr24")

        # Run YOLO inference
        results = self.model(img, verbose=False)

        # Draw bounding boxes and labels
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    label = f"{self.model.names[cls]} {conf:.2f}"
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Return as video frame
        return av.VideoFrame.from_ndarray(img, format="bgr24")

# Streamlit UI
st.set_page_config(page_title="Real-Time Object Detection", page_icon="🔍")
st.title("AI Real-Time Object Detection")
st.write("Allow camera access and see live detections.")

col1, col2, col3 = st.columns([1, 2, 1])  # center the video
with col2:
    webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=ObjectDetectionProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
        rtc_configuration={"iceServers": get_ice_servers()}  # <-- add this
    )

st.info("Detection runs on each frame. For better performance, ensure your system has a GPU or use a lighter model.")