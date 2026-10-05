# Desktop Notification Application

A Python desktop notification reminder application built with Plyer. It allows users to create custom notifications and receive them at a user-defined interval.

## Features

- Display desktop notifications using Plyer
- Custom notification title
- Custom notification message
- Custom notification interval
- Default settings for quick setup
- Input validation for notification interval
- Pause reminders temporarily
- Resume reminders when needed
- Quit the application safely
- Background notification thread
- Clean command-line interface
- Graceful shutdown with `Q` or `Ctrl+C`

## Requirements

- Python 3.8 or newer
- Plyer

## Installation

Clone the repository:

    git clone https://github.com/RaavanHrishi07/Desktop-Notification-Application.git

Move into the project directory:

    cd Desktop-Notification-Application

Install the required dependency:

    pip install -r requirements.txt

## Usage

Run the application:

    python main.py

The application will ask for the notification settings.

Example:

    Notification Settings
    ------------------------------
    Notification title [Break Reminder]:
    Notification message [Take a short break and rest your eyes.]:
    Interval in minutes [60]:

You can press `Enter` to use the default value.

After the settings are entered, the application starts sending notifications at the selected interval.

## Controls

While the application is running:

    P = Pause
    R = Resume
    Q = Quit

### Pause

Press `P` to temporarily pause future notifications.

### Resume

Press `R` to resume notifications after they have been paused.

### Quit

Press `Q` to safely stop the application.

You can also use `Ctrl+C` to stop the application from the terminal.

## Example

    =============================================
           DESKTOP NOTIFICATION APP
    =============================================

    Notification Settings
    ------------------------------
    Notification title [Break Reminder]:
    Notification message [Take a short break and rest your eyes.]:
    Interval in minutes [60]:

    Desktop Notification App is running.
    Notifications will appear every 60 minute(s).
    Commands: P = Pause | R = Resume | Q = Quit

    Enter command:

## How It Works

1. The application collects the notification title, message, and interval from the user.
2. The interval is validated to ensure it is a positive whole number.
3. A notification reminder runs in a background thread.
4. A desktop notification is displayed at the selected interval.
5. The user can pause or resume future notifications.
6. The application can be safely stopped using `Q` or `Ctrl+C`.

## Project Structure

    Desktop-Notification-Application/
    │
    ├── main.py
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    └── LICENSE

## Technologies Used

- Python
- Plyer
- Threading
- Command-line interface

## Error Handling

The application validates the notification interval and only accepts positive whole numbers.

If an invalid value is entered, the application asks the user to enter a valid interval.

## Author

**Hrishikesh Sharma**

GitHub: https://github.com/RaavanHrishi07

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.