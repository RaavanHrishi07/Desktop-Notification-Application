import time
from threading import Event, Thread

from plyer import notification


DEFAULT_TITLE = "Break Reminder"
DEFAULT_MESSAGE = "Take a short break and rest your eyes."
DEFAULT_INTERVAL = 60


def show_notification(title, message, timeout=10):
    """Display a desktop notification."""
    notification.notify(
        title=title,
        message=message,
        timeout=timeout,
    )


def get_positive_integer(prompt, default):
    """Get a positive integer from the user."""
    while True:
        value = input(f"{prompt} [{default}]: ").strip()

        if not value:
            return default

        try:
            number = int(value)

            if number <= 0:
                raise ValueError

            return number

        except ValueError:
            print("Please enter a positive whole number.")


def get_settings():
    """Collect notification settings from the user."""
    print("\nNotification Settings")
    print("-" * 30)

    title = input(f"Notification title [{DEFAULT_TITLE}]: ").strip()
    if not title:
        title = DEFAULT_TITLE

    message = input(
        f"Notification message [{DEFAULT_MESSAGE}]: "
    ).strip()
    if not message:
        message = DEFAULT_MESSAGE

    interval = get_positive_integer(
        "Interval in minutes",
        DEFAULT_INTERVAL,
    )

    return title, message, interval


class NotificationReminder:
    """Manage repeated desktop notifications."""

    def __init__(self, title, message, interval_minutes):
        self.title = title
        self.message = message
        self.interval_seconds = interval_minutes * 60
        self.stop_event = Event()
        self.pause_event = Event()
        self.pause_event.set()
        self.thread = None

    def start(self):
        """Start the notification reminder."""
        self.thread = Thread(
            target=self._run,
            daemon=True,
        )
        self.thread.start()

    def _run(self):
        """Send notifications until the reminder is stopped."""
        while not self.stop_event.is_set():
            self.pause_event.wait()

            if self.stop_event.is_set():
                break

            show_notification(self.title, self.message)
            print("Notification sent.")

            if self.stop_event.wait(self.interval_seconds):
                break

    def pause(self):
        """Pause future notifications."""
        self.pause_event.clear()
        print("Reminder paused.")

    def resume(self):
        """Resume future notifications."""
        self.pause_event.set()
        print("Reminder resumed.")

    def stop(self):
        """Stop the reminder."""
        self.stop_event.set()
        self.pause_event.set()

        if self.thread is not None:
            self.thread.join(timeout=2)


def run_reminder(title, message, interval_minutes):
    """Run the reminder with pause and resume controls."""
    reminder = NotificationReminder(
        title,
        message,
        interval_minutes,
    )

    reminder.start()

    print("\nDesktop Notification App is running.")
    print(f"Notifications will appear every {interval_minutes} minute(s).")
    print("Commands: P = Pause | R = Resume | Q = Quit")

    try:
        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == "p":
                reminder.pause()

            elif command == "r":
                reminder.resume()

            elif command == "q":
                break

            else:
                print("Invalid command. Use P, R, or Q.")

    except KeyboardInterrupt:
        print("\nStopping notification app...")

    finally:
        reminder.stop()
        print("Notification app stopped.")


def main():
    """Run the desktop notification application."""
    print("=" * 45)
    print("       DESKTOP NOTIFICATION APP")
    print("=" * 45)

    title, message, interval = get_settings()

    run_reminder(
        title,
        message,
        interval,
    )


if __name__ == "__main__":
    main()
    