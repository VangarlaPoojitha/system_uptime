import os

def get_system_uptime():
    """Returns system uptime in seconds."""
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

if __name__ == "__main__":
    uptime = get_system_uptime()
    print(f"System uptime: {uptime:.2f} seconds")