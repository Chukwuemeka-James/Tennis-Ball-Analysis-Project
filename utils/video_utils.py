import cv2

def read_video(video_path):
    # Initialize video capture with the provided video file path
    cap = cv2.VideoCapture(video_path)
    # Create an empty list to store each frame of the video
    frames = []
    while True:
        # Read the next frame from the video
        ret, frame = cap.read()
        # If no more frames are returned, break the loop
        if not ret:
            break
        # Append the current frame to the list
        frames.append(frame)
    # Release the video capture object (free up resources)
    cap.release()
    # Return the list of captured frames
    return frames



def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    height, width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))
    for frame in output_video_frames:
        out.write(frame)
    out.release()