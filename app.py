"""
Duplicate Finder Application

This script provides a graphical user interface (GUI) to find duplicate images and videos
within a specified folder. It utilizes PySimpleGUI for the interface and custom modules
for detecting duplicates.
"""
import sys
import os
import PySimpleGUI as sg
# Add the 'lib' directory to the system path for module imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from ImageDuplicateFinder import ImageDuplicateFinder
from VideoDuplicateFinder import VideoDuplicateFinder
# Define the theme for the PySimpleGUI window
sg.theme('DarkBlue13')
# Define the layout for the application window
layout = [
    [sg.Text("Duplicate Finder", font=("Helvetica", 25), justification='center', expand_x=True)],
    [sg.Text("Select Folder to Scan:", font=("Helvetica", 14))],
    [sg.In(size=(40, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse(button_text="Browse")],
    [sg.Text("Progress:"), sg.ProgressBar(max_value=100, orientation='h', size=(50, 20), key="-PROGRESS-")],
    [sg.Button("Find Duplicates", size=(15, 1)), sg.Button("Exit", size=(15, 1))],
    [sg.Text("Results:", font=("Helvetica", 14))],
    [sg.Multiline(size=(80, 20), key="-RESULTS-", disabled=True, autoscroll=True)]
]
# Create the window with the specified layout and size
window = sg.Window("Duplicate Finder", layout, size=(600, 500))
# Main event loop
while True:
    # Read events and values from the window
    event, values = window.read()
    # Exit the loop if the 'Exit' button is pressed or the window is closed
    if event in ("Exit", sg.WIN_CLOSED):
        break
    # Process the 'Find Duplicates' button click
    if event == "Find Duplicates":
        folder = values["-FOLDER-"]
        # Check if a folder has been selected
        if folder:
            # Update the progress bar and results area
            progress_bar = window['-PROGRESS-']
            progress_bar.update(current_count=0)
            window["-RESULTS-"].update("Scanning for duplicates...\n")
            window.refresh()
            # Create instances of the duplicate finder classes
            image_finder = ImageDuplicateFinder(folder, progress_bar)
            video_finder = VideoDuplicateFinder(folder, progress_bar)
            # Retrieve results from the finder instances
            image_results = image_finder.get_results()
            video_results = video_finder.get_results()
            # Format and display the results in the results area
            results = f"Image Duplicates:\n{image_results}\n\nVideo Duplicates:\n{video_results}\n"
            window["-RESULTS-"].update(results)
        else:
            # Show an error message if no folder is selected
            sg.popup("Please select a folder to scan.", title="Error")
# Close the window
window.close()
