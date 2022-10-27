import psutil as ps
import platform

"""
Note you need to have psutil install to use this program

run:  env\Scripts\activite.bat  before running the python scripts

"""



def get_cpu():
    print("\n")
    print('checking cpu .......')
    print(f"CPU USAGE :  {ps.cpu_percent(interval=10)}%")
    print('done')
    print("\n")



def get_ram():
    print("\n")
    print(f"RAM USAGE: {ps.virtual_memory().used} GB")
    print("\n")


def os_info():
    print("\n")
    print(f"OS NAME: {platform.system()}")
    print(f"OS VERSION: {platform.version()}")
    print("\n")


def get_status():
    print("\n")
    print("Waiting for system to respond...")
    cpu = ps.cpu_percent(interval=10)
    ram = ps.virtual_memory().percent

    if int(cpu) >= 50 and int(ram) >= 50:
        print('System is  busy')
    else:
        print("System not busy")

    print("\n")




print("Task Menu".center(120))


while True:
  
  try:
        Options = int(input("""
    Command options from 1-5:

    1. Get CPU Usage
    2. Get RAM Usage
    3. Get operating system info
    4. Get system status
    5. Exit program

    Enter option: """))

        if Options==1:
            get_cpu()

        elif Options == 2:
            get_ram()

        elif Options == 3:
            os_info()
        
        elif Options == 4:
            get_status()

        elif Options == 5:
            break
        else:
            print(f"{Options} is not a command option ")

  except Exception:
    print("invailed command entered")

 

    