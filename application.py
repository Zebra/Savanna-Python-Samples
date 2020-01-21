import os
from time import sleep
from CreateBarcode import create
from FDARecall import deviceSearch, drugSearch, foodUpc
from UPCLookup import lookup

def display_title_bar():
    os.system('clear')
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
        create(params[0], params[1])
    if(params_length == 5):
        create(params[0], params[1], params[2], params[3], params[4])
    if(params_length == 6):
        create(params[0], params[1], params[2], params[3], params[4], params[5])
    

def run_FDARecall():
    print("\FDARecall:")
    print("\tinput should follow:")
    print("\tdeviceSearch, search (deviceSearch, Device) or ")
    print("\tdeviceSearch, search, limit (deviceSearch, Device, 1) or")
    print("\tdrugSearch, search (drugSearch, Food)")
    print("\tdrugSearch, search, limit (drugSearch, Food, 1)")
    print("\foodUpc, upc (foodUpc, 820267662041775209)")
    print("\foodUpc, upc, limit (foodUpc, 820267662041775209, 1)")
    print("\drugUpc, upc (drugUpc, 820267662041775209)")
    print("\drugUpc, upc, limit (drugUpc, 820267662041775209, 1)")


def run_UPCLookup():


def run_program():
    display_title_bar()
    prompt = input
    if(prompt == '1'):     
        run_CreateBarcode()
    if(prompt == '2'):
        run_FDARecall()
    if(prompt == '3'):
        run_UPCLookup()

