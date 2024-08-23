# Duplicate Finder

## Overview

Duplicate Finder is a Python application designed to identify and handle duplicate images and videos in a specified directory. The application uses the `difPy` library for image comparison and a custom `DuplicateFinder` class for video comparison. It provides a graphical user interface (GUI) built with PySimpleGUI to facilitate user interaction and display results.

## Features

- **Image Duplicate Finder**: Detects duplicate images in a specified folder and moves them to a dedicated directory.
- **Video Duplicate Finder**: Identifies duplicate videos and moves them to a separate directory.
- **Progress Bar**: Visual feedback of the scan progress through a progress bar in the GUI.
- **Results Display**: Shows a summary of found duplicates in the application window.

## Installation

To run the Duplicate Finder application, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/jsuyog2/duplicate-finder.git
    cd duplicate-finder
    ```

2. **Set Up a Virtual Environment (Optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    Ensure you have the following packages in your `requirements.txt`:

    ```
    PySimpleGUI
    difPy
    ```

## Usage

1. **Run the Application**

    ```bash
    python app.py
    ```

2. **Using the GUI**

    - Click on **"Browse"** to select the folder you want to scan for duplicates.
    - Click on **"Find Duplicates"** to start the scanning process.
    - The progress bar will update as the scan progresses.
    - The results will be displayed in the results area, showing duplicate images and videos.

## File Structure

- `app.py`: The main application file that initializes and runs the GUI.
- `lib/`
  - `ImageDuplicateFinder.py`: Contains the `ImageDuplicateFinder` class for finding duplicate images.
  - `VideoDuplicateFinder.py`: Contains the `VideoDuplicateFinder` class for finding duplicate videos.
  - `DuplicateFinder.py`: Custom class for finding duplicate videos (used by `VideoDuplicateFinder`).
- `requirements.txt`: Lists the required Python packages.

## Example

Here's how the output might look after scanning a folder:

```
Duplicate images found:
Original: /path/to/original/image1.jpg
Duplicates: /path/to/duplicate/image1_1.jpg, /path/to/duplicate/image1_2.jpg

Duplicate videos found:
Original: /path/to/original/video1.mp4
Duplicates: /path/to/duplicate/video1_1.mp4, /path/to/duplicate/video1_2.mp4
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. 

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [jsuyog2@gmail.com](mailto:jsuyog2@gmail.com).