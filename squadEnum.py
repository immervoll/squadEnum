from lib import cli
import os
cli.log("                           _ _____                      ", 5)
cli.log("                          | |  ___|                     ", 5)
cli.log(" ___  __ _ _   _  __ _  __| | |__ _ __  _   _ _ __ ___  ", 5)
cli.log("/ __|/ _` | | | |/ _` |/ _` |  __| '_ \| | | | '_ ` _ \ ", 5)
cli.log("\__ \ (_| | |_| | (_| | (_| | |__| | | | |_| | | | | | |", 5)
cli.log("|___/\__, |\__,_|\__,_|\__,_\____/_| |_|\__,_|_| |_| |_|", 5)
cli.log("        | |                                             ", 5)
cli.log("        |_|                                             ", 5)
cli.log("by Immervoll : https://github.com/immervoll/squadEnum",5)

path_dir: str = input("Please Enter file Path to SquadEditor/Squad/Content/Vehicles :") or "D:/GameDev/SquadEditor/Squad/Content/Vehicles"
if os.path.isdir(path_dir):
    vehicles = os.listdir(path_dir)
    cli.log("attempting to find classes")
    for vehicle in vehicles:
        if os.path.isdir(f"{path_dir}/{vehicle}/Weapons"):
            cli.log(vehicle, 4)
            weapons =  os.listdir(f"{path_dir}/{vehicle}/Weapons")
            for weapon in weapons:
                cli.log(f"""found {str(weapon).replace(".uasset", "")} for vehicle {vehicle}""", 4)
                cli.export(str(weapon).replace(".uasset", ""))
        else:
            cli.log(f"{vehicle} has no weapons", 2 )
else:
    cli.log("the provided path is invalid!", 3)
    cli.log(f"provided path: {path_dir}")
    cli.log("exiting")
                