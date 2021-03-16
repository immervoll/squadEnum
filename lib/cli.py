#core functions related to commandline interfaces
import time
from colorama import init, Fore

init(autoreset=True)
logfile = f"./logs/log {time.ctime()}.txt".replace(" ","-").replace(":", "-")


def log(payload:str, type:int = 1):     # -> formats & logs a payload based on type
    if type == 1:
        print(Fore.WHITE + f"{time.ctime()} | LOG ::: {payload}" + Fore.RESET)
        __write(payload, type)
    elif type == 2:
        print(Fore.YELLOW + f"{time.ctime()} | WAR ::: {payload}" + Fore.RESET)
        __write(payload, type)
    elif type == 3:
        print(Fore.RED + f"{time.ctime()} | ERR ::: {payload}" + Fore.RESET)
        __write(payload, type)
    elif type == 4:
        print(Fore.GREEN + f"{time.ctime()} | SUC ::: {payload}" + Fore.RESET)
        __write(payload, type)
    elif type == 5:
        print(Fore.BLUE + f"{time.ctime()} | INF ::: {payload}" + Fore.RESET)
        __write(payload, type)
    elif type == 6:
        print(Fore.PINK + f"{time.ctime()} | UTI ::: {payload}" + Fore.RESET)
        __write(payload, type)
    else:
        log(f"couldn't find log type {type}, falling back to tpye 2 instead", 3)
        __write(payload, 3)
        log(payload,2)
        __write(payload, 2)
        
def __write(payload:str, type:int):       # -> appends log to file
    with open(logfile, "a") as f:
        if type == 1:
            f.write(f"{time.ctime()} | LOG ::: {payload} \n")
        elif type == 2:
            f.write(f"{time.ctime()} | WAR ::: {payload} \n")
        elif type == 3:
            f.write(f"{time.ctime()} | ERR ::: {payload} \n")
        elif type == 4:
            f.write(f"{time.ctime()} | SUC ::: {payload} \n")
        elif type == 5:
            f.write(f"{time.ctime()} | INF ::: {payload} \n")
        elif type == 6:
            f.write(f"{time.ctime()} | UTI ::: {payload} \n")
        f.close()
        
def export(content:str):
    with open("./export.txt", "a") as e:
        e.write(f"{content}, \n ")