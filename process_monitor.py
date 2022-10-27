import time as t
import psutil


p = psutil.Process()

for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        Ram = proc.cpu_percent(interval=2)
        print(f" {processID}  {processName} {Ram}")


    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass