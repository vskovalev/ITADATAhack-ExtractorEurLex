import psutil


def kill_chrome_processes():
    for proc in psutil.process_iter():
        try:
            if proc.name() == "chrome.exe":
                proc.kill()
        except psutil.AccessDenied:
            # Handle cases where permission is denied to kill a process
            continue