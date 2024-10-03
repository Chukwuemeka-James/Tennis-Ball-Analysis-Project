# Tennis Ball Analysis Project

## Overview
The **Tennis Ball Analysis Project** is a computer vision and machine learning project aimed at analyzing tennis match videos. The project detects and tracks players and the ball during a match, calculates player and ball statistics such as shot speed, player movement, and visualizes this information in the video. This analysis is performed by detecting players and balls in video frames, identifying ball shots, measuring player speeds, and calculating key performance statistics.

## Features
- **Player and Ball Detection**: Utilizes pre-trained YOLO models to detect players and balls in video frames.
- **Ball Shot Detection**: Detects ball shots during the match and estimates the speed of each shot.
- **Player Statistics**: Calculates and tracks player speeds and shot statistics during the game.
- **Court Line Detection**: Identifies the keypoints of the tennis court and filters player detections accordingly.
- **Mini-Court Visualization**: Maps player and ball positions onto a mini court for enhanced visual analysis.
- **Frame-by-Frame Analysis**: Displays frame numbers and overlays statistics on the video for easy debugging and analysis.

## Project Structure

- **main.py**: Main file containing the pipeline for reading the video, detecting players and ball, calculating statistics, and saving the output video.
- **utils.py**: Contains helper functions for reading, saving videos, measuring distances, and converting pixel distances to meters.
- **trackers/**: Contains classes for tracking players (`PlayerTracker`) and balls (`BallTracker`) across video frames.
- **court_line_detector.py**: Detects and extracts keypoints of the tennis court.
- **mini_court.py**: Maps player and ball coordinates onto a mini court and draws these visualizations onto the output video.
- **constants.py**: Contains useful custom-made constants.
- **input_videos/**: Folder to store input videos for analysis.
- **output_videos/**: Folder to store the output videos after analysis.

## Key Components

### 1. **Player and Ball Detection**
   The project uses YOLO-based models for detecting players and the ball in each frame. The `PlayerTracker` and `BallTracker` classes handle the detection and tracking of players and balls throughout the video.

### 2. **Court Line Detection**
   The `CourtLineDetector` model identifies the keypoints of the tennis court, ensuring that only players within the court are detected.

### 3. **Shot and Speed Analysis**
   - **Ball Speed**: The speed of each shot is calculated by measuring the distance the ball travels between two consecutive frames where a shot is detected.
   - **Player Speed**: The speed of players is determined by tracking their movement between ball shots.

### 4. **Mini-Court Visualization**
   The project provides a visual representation of the player's and ball's positions on a smaller court. The positions are mapped and drawn on the output video, enhancing the understanding of player movement and shot dynamics.

### 5. **Statistics Calculation**
   - **Shot Speed**: Calculates shot speeds for both players.
   - **Player Speed**: Tracks player movement during the game, measuring how fast players move in response to ball shots.
   - **Average Speeds**: Calculates average shot speed and player speed for each player over the course of the game.

### 6. **Data Output**
   The project produces detailed player statistics for each frame, including:
   - Total shot speed
   - Last shot speed
   - Total player movement speed
   - Last player movement speed
   - Average shot and movement speeds

### 7. **What of the model?**
   - it is too heavy and i cant upload it. 
