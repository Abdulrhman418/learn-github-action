import os
import sys
import time
import requests
import validators
import socket
from urllib.parse import urlparse

def valid_hostname(hostname):
    """تحقق من وجود الدومين عبر DNS"""
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False

def ping_url(url: str, delay: int, max_trials: int) -> bool:
    """Ping URL حتى يصبح reachable أو تنتهي المحاولات"""
    for trial in range(1, max_trials + 1):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[SUCCESS] Trial {trial}: URL {url} is reachable!")
                return True
            else:
                print(f"[WARN] Trial {trial}: Received status code {response.status_code}")
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

    # تحقق من صحة URL وصحة الدومين
    if not url or not validators.url(url):
        print(f"[ERROR] Invalid URL format: {url}")
        sys.exit(1)

    hostname = urlparse(url).hostname
    if not valid_hostname(hostname):
        print(f"[ERROR] Hostname does not exist: {hostname}")
        sys.exit(1)

    success = ping_url(url, delay, max_trials)

    if not success:
        print(f"[ERROR] URL {url} is unreachable after {max_trials} trials.")
        sys.exit(1)

if __name__ == "__main__":
    run()
