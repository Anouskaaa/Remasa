# 🕌 Remasa: Prayer Time Reminder
A simple yet powerful Python application designed to remind you of daily prayer times, ensuring you never miss a moment of spiritual reflection. "Remasa" stands for "Remaja Masjid Software" (Mosque Youth Software).

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT%20License-green) ![Stars](https://img.shields.io/github/stars/Remasa/Remasa?style=social) ![Forks](https://img.shields.io/github/forks/Remasa/Remasa?style=social)

<img src="/assets/remaja-masjid.png" width="250" height="auto">

## ✨ Features

*   ⏰ **Accurate Prayer Times**: Automatically calculates and displays prayer times based on your location.
*   🔔 **Customizable Notifications**: Set up timely reminders for each prayer, ensuring you stay connected.
*   🌍 **Location-Based Timing**: Utilizes your system's location (or a configured one) to provide precise timings.
*   💻 **Lightweight & Efficient**: A command-line Python application designed for minimal resource usage.
*   ⚙️ **Easy Configuration**: Simple setup to get your prayer reminders running quickly.


## 🚀 Installation Guide

Follow these steps to get Remasa up and running on your local machine.

### Prerequisites

Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Manual Installation

1.  **Clone the Repository**:
    First, clone the Remasa repository to your local machine using Git:
    ```bash
    git clone https://github.com/Remasa/Remasa.git
    cd Remasa
    ```

2.  **Create a Virtual Environment (Recommended)**:
    It's good practice to work within a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**:
    Install all required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration**:
    The application might require location data or specific API keys for prayer time calculation. These details might be configured through environment variables or a configuration file (refer to the `Usage Examples` section for details).


## 💡 Usage Examples

Once installed, you can run the `sholat-timer.py` script to start receiving prayer time reminders.

### Basic Usage

To run the prayer timer, simply execute the main script:

```bash
python sholat-timer.py
```

This will typically display the current prayer times and start the reminder service.

### Configuration

Remasa might offer configuration options for:
*   **Location**: Manually setting latitude and longitude if automatic detection is not preferred.
*   **Calculation Method**: Choosing different Islamic prayer time calculation methods (e.g., MWL, ISNA, Egypt).
*   **Notification Preferences**: Customizing reminder sounds or display methods.

These options can usually be set within the `sholat-timer.py` script or a separate configuration file.

_Example of configuration (conceptual):_
```python
# Inside sholat-timer.py or a config.py
LOCATION = {"latitude": -6.2088, "longitude": 106.8456} # Example: Jakarta
CALC_METHOD = "MWL" # Muslim World League
```



## 🗺️ Project TODO

- [ ] Make a clean code 
- [ ] Make the program run when system boot settings
- [ ] Adzan play when time matched with the pray time 
- [ ] Build a Graphical User Interface 
- [ ] Create a pray time table list 


### Code Style

*   Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
*   Use clear and concise variable/function names.
*   Include comments where necessary to explain complex logic.

### Pull Request Process

1.  **Fork** the repository and clone your fork.
2.  Create a new branch from `main` for your changes.
3.  Make your modifications and ensure they are well-tested.
4.  Commit your changes with clear, descriptive commit messages.
5.  Push your branch to your fork.
6.  Open a Pull Request (PR) to the `main` branch of the original Remasa repository.
7.  Provide a clear description of your changes in the PR, linking to any relevant issues.

## 📄 License Information

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software under the terms of the MIT License. A copy of the license can be found in the [LICENSE](LICENSE) file in the root of this repository.

