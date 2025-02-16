from flask import Flask, render_template, Response, request
import cv2
import os
import datetime

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Initialize camera
# Set camera frame size (width and height)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 840)  # Width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Height
recording = False  # Global flag for recording status
out = None  # Video writer object

def generate_frames():
    global out, recording
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Get current timestamp
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            
            # Add permanent timestamp at bottom left
            cv2.putText(frame, timestamp, (10, frame.shape[0] - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Add recording indicator if recording
            if recording:
                # Show only minutes and seconds during recording
                rec_time = datetime.datetime.now().strftime("%M:%S")  # MM:SS format
                rec_text = f"REC {rec_time}"
                # Red background for REC indicator (bottom-right)
                cv2.rectangle(frame, (frame.shape[1]-200, frame.shape[0]-50),  # Y-coordinate at bottom
                            (frame.shape[1], frame.shape[0]), (0, 0, 255), -1)
                cv2.putText(frame, rec_text, (frame.shape[1]-190, frame.shape[0]-20),  # Adjust Y-coordinate
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                # Write frame to video file
                out.write(frame)
            
            # Encode frame for browser display
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Render main page with video feed"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    """Capture and save snapshot"""
    success, frame = camera.read()
    if success:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"snapshots/{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        return "✅ Photo saved successfully!"
    return "❌ Failed to capture photo!"

@app.route('/record', methods=['POST'])
def record():
    """Start/stop video recording"""
    global recording, out
    if not recording:
        # Start recording
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"recordings/{timestamp}.mp4"
        # Use MP4 format with 'mp4v' codec
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # Get frame dimensions from camera
        frame_width = int(camera.get(3))
        frame_height = int(camera.get(4))
        out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height))
        recording = True
        return "⏺️ Recording started!"
    else:
        # Stop recording
        out.release()
        recording = False
        return "⏹️ Video saved successfully!"

if __name__ == '__main__':
    # Create required directories if they don't exist
    os.makedirs('recordings', exist_ok=True)
    os.makedirs('snapshots', exist_ok=True)
    # Start Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)