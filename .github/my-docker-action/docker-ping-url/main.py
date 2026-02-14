import os
import time
import sys
import requests

def ping_url(url: str, delay: int, max_trials: int) -> bool:
    for trial in range(1, max_trials + 1):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[INFO] Trial {trial}: URL is reachable!")
                return True
            else:
                print(f"[WARN] Trial {trial}: Received status {response.status_code}")
        except requests.RequestException as e:
            print(f"[ERROR] Trial {trial}: {e}")

        if trial < max_trials:
            print(f"[INFO] Waiting {delay}s before next trial...")
            time.sleep(delay)

    return False

def run():
    url = os.getenv("INPUT_URL")
    max_trials = int(os.getenv("INPUT_MAX_TRIALS", "10"))
    delay = int(os.getenv("INPUT_DELAY", "5"))

    if not url:
        print("[ERROR] URL input is required!")
        sys.exit(1)

    success = ping_url(url, delay, max_trials)

    if not success:
        print(f"[ERROR] URL {url} is unreachable after {max_trials} trials.")
        sys.exit(1)
    else:
        print(f"[SUCCESS] URL {url} is reachable!")

if __name__ == "__main__":
    run()
