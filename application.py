import os
from time import sleep
from savanna.CreateBarcode import CreateBarcode
from savanna.FDARecall import FDARecall
from savanna.UPCLookup import UPCLookup
from savanna.SavannaAPI import SavannaAPI


def display_title_bar():
    os.system('cls' if os.name == 'nt' else 'clear')
    SavannaAPI.APIKey = ""
    print("\t**************************************************")
    print("\t*** Commandline Savanna-Python-SDK sample tool ***")
    print("\t**************************************************")
    print("\t[1] CreateBarcode")
    print("\t[2] FDARecall")
    print("\t[3] UPCLookup")

def run_CreateBarcode():
    print("\tCreateBarcode:")
    print("\tinput should follow:")
    print("\tsymbology, text (code39, HELLO-WORLD) or ")
    print("\tsymbology, text, scale, rotation, includeText (code39, HELLO-WORLD, 1, N, true) or")
    print("\tsymbology, text, scaleX, scaleY, rotation, includeText (code39, HELLO-WORLD, 1, 1, N, true)")
    command = input("\tcommand: ")
    params = command.split(', ')
    params_length = len(params)
    if(params_length == 2):
        fileBytes = CreateBarcode.create_symbology_text(params[0], params[1])
    if(params_length == 5):
        fileBytes = CreateBarcode.create_symbology_text_scale_rotation_includeText(params[0], params[1], params[2], params[3], params[4])
    if(params_length == 6):
        fileBytes = CreateBarcode.create_symbology_text_scaleX_scaleY_rotation_includeText(params[0], params[1], params[2], params[3], params[4], params[5])
    barcodeFile = open("barcode.png", "wb")
    barcodeFile.write(fileBytes)


def run_FDARecall():
    print("\tFDARecall:")
    print("\tinput should follow:")
    print("\tdeviceSearch, search (deviceSearch, Device) or ")
    print("\tdeviceSearch, search, limit (deviceSearch, Device, 1) or")
    print("\tdrugSearch, search (drugSearch, Food)")
    print("\tdrugSearch, search, limit (drugSearch, Food, 1)")
    print("\tfoodUpc, upc (foodUpc, 820267662041775209)")
    print("\tfoodUpc, upc, limit (foodUpc, 820267662041775209, 1)")
    print("\tdrugUpc, upc (drugUpc, 820267662041775209)")
    print("\tdrugUpc, upc, limit (drugUpc, 820267662041775209, 1)")
    command = input("\tcommand: ")
    params = command.split(', ')
    params_length = len(params)
    if(params_length == 2):
        if(params[0] == "deviceSearch"):
            FDARecall.deviceSearch(params[1])
        if(params[0] == "drugSearch"):
            FDARecall.drugSearch(params[1])
        if(params[0] == "foodUpc"):
            FDARecall.foodUpc(params[1])
        if(params[0] == "drugUpc"):
            FDARecall.drugUpc(params[1])
    if(params_length == 3):
        if(params[0] == "deviceSearch"):
            FDARecall.deviceSearch_limit(params[1], params[2])
        if(params[0] == "drugSearch"):
            FDARecall.drugSearch_limit(params[1], params[2])
        if(params[0] == "foodUpc"):
            FDARecall.foodUpc_limit(params[1], params[2])
        if(params[0] == "drugUpc"):
            FDARecall.drugUpc_limit(params[1], params[2])

def run_UPCLookup():
    print("\tUPCLookup:")
    print("\tinput should follow:")
    print("\t9781483922973")
    command = input("\tcommand: ")
    UPCLookup.lookup(command)

def main():
    display_title_bar()
    prompt = input("\tEnter number 1 through 3: ")
    if(prompt == '1'):
        run_CreateBarcode()
    if(prompt == '2'):
        run_FDARecall()
    if(prompt == '3'):
        run_UPCLookup()

main()