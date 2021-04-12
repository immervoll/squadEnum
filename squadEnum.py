from lib import cli
import os
import sys
cli.log("                           _ _____                      ", 5)
cli.log("                          | |  ___|                     ", 5)
cli.log(" ___  __ _ _   _  __ _  __| | |__ _ __  _   _ _ __ ___  ", 5)
cli.log("/ __|/ _` | | | |/ _` |/ _` |  __| '_ \| | | | '_ ` _ \ ", 5)
cli.log("\__ \ (_| | |_| | (_| | (_| | |__| | | | |_| | | | | | |", 5)
cli.log("|___/\__, |\__,_|\__,_|\__,_\____/_| |_|\__,_|_| |_| |_|", 5)
cli.log("        | |                                             ", 5)
cli.log("        |_|                                             ", 5)
cli.log("by Immervoll : https://github.com/immervoll/squadEnum",5)

sdk_path: str = input("Please Enter file Path to SquadEditor/Squad :") or "D:/GameDev/SquadEditor/Squad"

def getVehicleWeapons():
    
    vehicles_path = sdk_path + "/Content/Vehicles"
    if os.path.isdir(vehicles_path):
        vehicles = os.listdir(vehicles_path)
        cli.log("attempting to find classes")
        for vehicle in vehicles:
            if os.path.isdir(f"{vehicles_path}/{vehicle}/Weapons"):
                cli.log(vehicle, 4)
                weapons =  os.listdir(f"{vehicles_path}/{vehicle}/Weapons")
                for weapon in weapons:
                    cli.log(f"""found {str(weapon).replace(".uasset", "")} for vehicle {vehicle}""", 4)
                    cli.export(str(weapon).replace(".uasset", ""))
            else:
                cli.log(f"{vehicle} has no weapons", 2 )
def getInfWeapons():
    
    inf_path = sdk_path + "\Content\Blueprints\Items"
    if os.path.isdir(inf_path):
        infweapons = os.listdir(inf_path)
        cli.log("attempting to find classes")
        for infweapon in infweapons:
            if os.path.isdir(f"{inf_path}/{infweapon}"):
                cli.log(infweapon, 4)
                weapons =  os.listdir(f"{inf_path}/{infweapon}")
                for weapon in weapons:
                    cli.log(f"""found {str(weapon).replace(".uasset", "")} for weapon class {infweapon}""", 4)
                    cli.export(str(weapon).replace(".uasset", ""))
            else:
                cli.log(f"{infweapon} has no weapons", 2 )



if os.path.isdir(sdk_path):
    cli.log("ENUMERATING VEHICLES",5)
    getVehicleWeapons()
    cli.log("ENUMERATING INFANTRY WEAPONS",5)
    getInfWeapons()
else:
    cli.log("the provided path is invalid!", 3)
    cli.log(f"provided path: {sdk_path}")
    cli.log("exiting")
    sys.exit(0)