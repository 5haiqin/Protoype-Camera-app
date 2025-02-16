# Prototype Camera App

## Overview

The Prototype Camera App is a web-based application that enables users to capture images and record videos directly from their browser. It provides a simple interface for accessing and utilizing your device's camera.

## Features

- **Capture Photos**: Take snapshots using your device's camera.
- **Record Videos**: Record videos with audio support.
- **View Snapshots**: Access and view all captured images.
- **View Recordings**: Access and view all recorded videos.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/5haiqin/Protoype-Camera-app.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Protoype-Camera-app
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

- **Access the Application**: Open your web browser and navigate to `http://localhost:5000/`.
- **Capture a Photo**: Click on the "Capture Photo" button to take a snapshot.
- **Record a Video**: Click on the "Start Recording" button to begin recording and "Stop Recording" to end.
- **View Captured Media**: Use the "View Snapshots" and "View Recordings" links to see your saved media.

## Project Structure

```
Protoype-Camera-app/
│-- app.py               # Main Flask application file
│-- requirements.txt     # Dependencies list
│-- static/
│   └── style.css        # CSS file for styling
│-- templates/
│   └── index.html       # Main HTML template
│-- snapshots/           # Directory where captured images are stored
│-- recordings/          # Directory where recorded videos are stored
```

## Dependencies

- Flask
- OpenCV

Ensure all dependencies are installed by running the command in the Installation section.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please open an issue on the repository or contact the maintainer.
