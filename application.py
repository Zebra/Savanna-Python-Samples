import os
from time import sleep
from CreateBarcode import CreateBarcode
from FDARecall import FDARecall
from UPCLookup import UPCLookup
from SavannaAPI import SavannaAPI

def display_title_bar():
    os.system('clear')
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
    command = input
    params = command.split(', ')
    params_length = params.len()
    if(params_length == 2):
        CreateBarcode.create(params[0], params[1])
    if(params_length == 5):
        CreateBarcode.create(params[0], params[1], params[2], params[3], params[4])
    if(params_length == 6):
        CreateBarcode.create(params[0], params[1], params[2], params[3], params[4], params[5])
    

def run_FDARecall():
    print("\tFDARecall:")
    print("\tinput should follow:")
    print("\tdeviceSearch, search (deviceSearch, Device) or ")
    print("\tdeviceSearch, search, limit (deviceSearch, Device, 1) or")
    print("\tdrugSearch, search (drugSearch, Food)")
    print("\tdrugSearch, search, limit (drugSearch, Food, 1)")
    print("\foodUpc, upc (foodUpc, 820267662041775209)")
    print("\foodUpc, upc, limit (foodUpc, 820267662041775209, 1)")
    print("\drugUpc, upc (drugUpc, 820267662041775209)")
    print("\drugUpc, upc, limit (drugUpc, 820267662041775209, 1)")
    command = input
    params = command.split(', ')
    params_length = params.len()
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
            FDARecall.deviceSearch(params[1], params[2])
        if(params[0] == "drugSearch"):
            FDARecall.deviceSearch(params[1], params[2])
        if(params[0] == "foodUpc"):
            FDARecall.deviceSearch(params[1], params[2])
        if(params[0] == "drugUpc"):
            FDARecall.deviceSearch(params[1], params[2])
    
def run_UPCLookup():
    print("\tUPCLookup:")
    print("\tinput should follow:")
    print("\tupc (9781483922973)")
    command = input
    UPCLookup.lookup(command)

def run_program():
    display_title_bar()
    prompt = input
    if(prompt == '1'):     
        run_CreateBarcode()
    if(prompt == '2'):
        run_FDARecall()
    if(prompt == '3'):
        run_UPCLookup()