import time

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


def run_reminder(title, message, interval_minutes):
    """Send notifications at the selected interval."""
    interval_seconds = interval_minutes * 60

    print("\nDesktop Notification App is running.")
    print(f"Notifications will appear every {interval_minutes} minute(s).")
    print("Press Ctrl+C to stop the application.\n")

    try:
        while True:
            show_notification(title, message)
            print("Notification sent.")

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nNotification app stopped.")


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
    