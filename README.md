# ScreenScene

`ScreenScene` is a collection of Python scripts for tracking and visualizing screen time data on a Windows system. It includes two main components: `screenscene.py` for data collection and `screenscenegui.py` for data visualization.

## Features

- **Data Collection**: Tracks the active window and records the usage time for different applications.
- **Data Visualization**: Displays a summary of screen time, hourly usage, and app-specific usage in a graphical user interface (GUI).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ScreenScene.git

2. **Navigate to the source directory:**

   ```bash
   cd ScreenScene/source

3.**Install the required dependencies:**

   ```bash
   pip install customtkinter matplotlib psutil pywin32
   ```

## Usage

### Data Collection (`screenscene.py`)

1. **Run the script:**

   ```bash
   python screenscene.py

2. **Functionality:**
   - Continuously tracks the active window and records the usage time for each application.
   - Saves the collected data to daily text files named `YYYY-MM-DD.txt` and `YYYY-MM-DD-hour.txt`.

### Data Visualization (`screenscenegui.py`)

1. **Run the script:**

   ```bash
   python screenscenegui.py

2. **Functionality:**
   - Loads the screen time data from the text files.
   - Displays a summary of total screen time and time spent on specific projects.
   - Lists the top applications used during the day with their usage time and percentage

## Code Description

### `screenscene.py`

- **Data Collection**: Uses `psutil` and `win32gui` to track the active window and record usage time.
- **Data Storage**: Saves usage data to text files in a dictionary format.
  - `data`: Stores total usage time for each application.
  - `hour_data`: Stores usage time for each hour of the day.

### `screenscenegui.py`

- **Data Loading**: Reads screen time data from the generated text files.
  - `app_data`: Reads from `YYYY-MM-DD.txt` for total usage time per application.
  - `data`: Reads from `YYYY-MM-DD-hour.txt` for hourly usage data.
- **Data Visualization**: Utilizes `customtkinter` for the GUI and `matplotlib` for plotting.
  - **Summary Section**: Displays total project goal time and time limit.
  - **Hourly Usage**: Shows usage in 24-hour format with usage bars.
  - **App Usage**: Lists top applications with their usage time and percentage.
