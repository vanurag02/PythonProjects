import os
import sys
import shutil
from datetime import datetime

SNAPSHOT_DIR = "snapshots"
CONFIG_FILE = "appConfig.json"
LOG_FILE = "deploy.log"


def log(message):
    """Write a message to the log file with a timestamp."""
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def create_snapshot():
    """Copy the current config file into a timestamped snapshot folder."""
    if not os.path.exists(CONFIG_FILE):
        print(f"[ERROR] Config file '{CONFIG_FILE}' not found.")
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_path = os.path.join(SNAPSHOT_DIR, timestamp)
    os.makedirs(snapshot_path, exist_ok=True)

    shutil.copy2(CONFIG_FILE, snapshot_path)
    log(f"Snapshot created at {snapshot_path}")
    return snapshot_path


def apply_changes(new_config_path):
    """Apply changes from a given config file."""
    if not os.path.exists(new_config_path):
        print(f"[ERROR] New config file '{new_config_path}' not found.")
        sys.exit(1)

    snapshot_path = create_snapshot()

    # Replace current config with the new one
    shutil.copy2(new_config_path, CONFIG_FILE)

    log(f"Applied config from '{new_config_path}' - Snapshot saved at {snapshot_path}")
    print(f"[INFO] Config applied. Snapshot saved at: {snapshot_path}")


def rollback(snapshot_path):
    """Restore the config file from a snapshot."""
    if not os.path.exists(snapshot_path):
        print(f"[ERROR] Snapshot '{snapshot_path}' not found.")
        sys.exit(1)

    snapshot_file = os.path.join(snapshot_path, CONFIG_FILE)
    if not os.path.exists(snapshot_file):
        print(f"[ERROR] No config file found in snapshot '{snapshot_path}'.")
        sys.exit(1)

    shutil.copy2(snapshot_file, CONFIG_FILE)
    log(f"Rolled back config from snapshot '{snapshot_path}'")
    print(f"[INFO] Rolled back to snapshot: {snapshot_path}")


def show_usage():
    print("Usage:")
    print("  python deploy.py apply <new_config.json>")
    print("  python deploy.py rollback <snapshot_folder>")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        show_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "apply":
        apply_changes(sys.argv[2])
    elif command == "rollback":
        rollback(sys.argv[2])
    else:
        show_usage()
