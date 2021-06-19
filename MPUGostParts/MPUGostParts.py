#Author-MPU
#Description-

import adsk.core 
from urllib.parse import urlparse
from .utils import addHandler, handleError, clearHandlers, ui
import traceback, re
from .scripts import gost8328_75,gost7634_75,gost23526_79

# необходимо все еще править
COMMANDID = 'MPUGostParts_insert'
COMMANDNAME = 'Insert MPUGostParts Supplier Components'
COMMANDDESCRIPTION = 'With MPUGostParts, boost your design productivity and access millions of GOST models from hundreds of supplier catalogs.'
# URL = 'http://localhost:4200/'
URL = 'https://fusion-gost-library.web.app/'
PALETTEID = 'MPUGostParts_browser'
PALETTENAME = 'Autodesk Fusion 360 GOST Library - powered by MPU'
DOCKINGSTATE = adsk.core.PaletteDockingStates.PaletteDockStateRight
APP_UID = '3854bc50-bbcc-11eb-8529-0242ac130003'

handlers = []

def formatMsg(args):
    webArgs = adsk.core.WebRequestEventArgs.cast(args)
    Info = {}
    try:
        Info["PARAMS"] = webArgs.privateInfo
        Info["AppUID"] = (re.search('"AppUID":"\w*\-\w*\-\w*\-\w*\-\w*"', webArgs.properties)).group(0)
        Info["AppUID"] = re.findall('\w*\-\w*\-\w*\-\w*\-\w*',Info["AppUID"])[0]

        Info["GOST"] = (re.search('"GOST":"[^"]*"',webArgs.properties)).group(0)
        Info["GOST"] = re.findall('"[^"]*"',Info["GOST"])[1]
        Info["GOST"] = str(Info["GOST"]).replace("\"","")

        Info["TYPE"] = (re.search('"TYPE":"[^"]*"',webArgs.properties)).group(0)
        Info["TYPE"] = re.findall('"[^"]*"',Info["TYPE"])[1] 
        Info["TYPE"] = str(Info["TYPE"]).replace("\"","") 

        return Info
    except:
        return {}

class InsertedFromURLEventHandler(adsk.core.WebRequestEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        ui = None
        try:
            Info = formatMsg(args)
            if(Info != {}):
                if(Info["AppUID"]==APP_UID):
                    app = adsk.core.Application.get()
                    ui = app.userInterface
                    design = app.activeProduct
                    rootComp = design.rootComponent
                    occurence = rootComp.occurrences.item(rootComp.occurrences.count-1)

                    if(Info["GOST"]=="8328-75"):
                        gost8328_75.run(occurence,Info)
                    elif(Info["GOST"]=="7634-75"):
                        gost7634_75.run(occurence,Info)
                    elif(Info["GOST"]=="23526-79"):
                        gost23526_79.run(occurence,Info)
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run(context):
    try:
        createCommand()
    except:
        handleError('run')

def stop(context):
    try:
        clearHandlers()
        removeCommand()
    except:
        handleError('stop')

def createCommand():
    removeCommand()

    cmdDef = ui.commandDefinitions.addButtonDefinition(COMMANDID, COMMANDNAME, COMMANDDESCRIPTION, 'resources/insert')
    cmdDef.toolClipFilename = 'resources/insert/logo.png'
    addHandler(cmdDef.commandCreated, onCommandCreated)

    controls = toolbarPanelControls()
    controls.addCommand(cmdDef)

def removeCommand():
    cmdDef = ui.commandDefinitions.itemById(COMMANDID)
    if cmdDef:
        cmdDef.deleteMe()

    controls = toolbarPanelControls()
    control = controls.itemById(COMMANDID)
    if control:
        control.deleteMe()

def toolbarPanelControls():
    workspace = ui.workspaces.itemById('FusionSolidEnvironment')
    return workspace.toolbarPanels.itemById('InsertPanel').controls

def onCommandCreated(args: adsk.core.CommandCreatedEventArgs):
    addHandler(args.command.execute, onExecute)

def onExecute(args: adsk.core.CommandEventArgs):
    # display the legal prompt
    # import neu_dev
    # neu_dev.run_text_command('Fusion.ShowLegalNotice MPUGostParts')

    createPalette()

def createPalette():
    palettes = ui.palettes
    palette = palettes.itemById(PALETTEID)
    if palette:
        palette.deleteMe()
    palette = palettes.add(
        id=PALETTEID,
        name=PALETTENAME,
        htmlFileURL=URL,
        isVisible=True,
        showCloseButton=True,
        isResizable=True,
        width=1500,
        height=600,
        useNewWebBrowser=True
    )
    palette.dockingState = DOCKINGSTATE
    addHandler(palette.closed, onClosed)
    onInsertedFromURL = InsertedFromURLEventHandler()
    app = adsk.core.Application.get()
    app.insertedFromURL.add(onInsertedFromURL)
    handlers.append(onInsertedFromURL)

def onClosed(args: adsk.core.UserInterfaceGeneralEventArgs):
    palette = ui.palettes.itemById(PALETTEID)
    if palette:
        palette.deleteMe()