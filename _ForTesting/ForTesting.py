# Author-
# Description-

import adsk.core
import adsk.fusion
import adsk.cam
import traceback
import math
from . import gost7634_75K


def run(context):
    ui = None
    try:
        # Переменные
        params = {"d": 15, "D": 28, "H": 9, "D1": 28,"d1": 16,"r":0.5}
        d = params["d"]
        D = params["D"]
        H = params["H"]
        D1 = params["D1"]
        d1 = params["d1"]
        r = params["r"]

        protochkParams = gost7634_75K.run(d,"16200")

        CylCount = round(9*d/H)

        # Стандартные получалки
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        components = design.allComponents
        rootComp = design.rootComponent
        component = rootComp

        # Получаем ссылку на нужный компонент
        # occurence = rootComp.occurrences.item(rootComp.occurrences.count-1)
        # Получаем массив
        # patternFeature = occurence.component.features.circularPatternFeatures[0]
        patternFeature = component.features.circularPatternFeatures[0]
        # Получаем скетч и его размеры
        # sketches = occurence.component.sketches[0]
        sketches = component.sketches
        sketchDimensions = sketches[0].sketchDimensions
        # sketchDimensions2 = sketches[1].sketchDimensions
        # Получаем коллекцию скруглений
        # filletFeatures = occurence.component.features.filletFeatures
        filletFeatures = component.features.filletFeatures
        revolveFeatures = component.features.revolveFeatures
        # holeFeature = component.features.holeFeatures[0]
        # combineFeatures.targetBody
        i = 0
        # extrudeFeatures = component.features.extrudeFeatures
        _params = {"d": 100, "D": 140, "B": 40, "r": 2}

        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        component = rootComp
        sketches = component.sketches
        sketchDimensions = sketches[0].sketchDimensions

        boolean = True
        i = 0
        num = -1
        for dim in sketchDimensions:
            _dim = dim.parameter.expression
            num = num + 1
            print("Размер:" + str(_dim) + " | ID: "+ str(num))


        # component.constructionPlanes[0].definition.angle.expression = str(360/(round(9*d/H)*2)) + "deg"

        # Вносим новые параметры
        # sketchDimensions[0].parameter.expression = str(H) + " mm"
        # sketchDimensions[1].parameter.expression = str(d1) + " mm"
        # sketchDimensions[2].parameter.expression = str(d) + " mm"
        # sketchDimensions[3].parameter.expression = str(D1) + " mm"
        # sketchDimensions[4].parameter.expression = str(D) + " mm"
        # sketchDimensions[5].parameter.expression = str(H/5) + " mm"
        # sketchDimensions[6].parameter.expression = str((D-d1)/2.5) + " mm"
        # sketchDimensions[7].parameter.expression = str(H/3) + " mm"
        # sketchDimensions[8].parameter.expression = str(D-d1)/60) + " mm"
        # sketchDimensions[9].parameter.expression = str(D-d1)/6) + " mm"

        # sketchDimensions2[0].parameter.expression = str(D/12+5*d1/12) + " mm"
        # sketchDimensions2[1].parameter.expression = str(3*(D-d1)/20) + " mm"
        # sketchDimensions2[2].parameter.expression = str(H/3) + " mm"


        # sketchDimensions[11].parameter.expression = str((D-d)/8) + " mm"
        # sketchDimensions[12].parameter.expression = str((D-d)/8) + " mm"

        # sketchDimensions[13].parameter.expression = str(protochkParams["R"]*2) + " mm"
        # sketchDimensions[15].parameter.expression = str(protochkParams["b0"]) + " mm"

        # sketchDimensions[7].parameter.expression = str((D-d)/16) + " mm"
        # # sketchDimensions[8].parameter.expression = str(_d) + " mm"
        # sketchDimensions[10].parameter.expression = str((D-d)/8) + " mm"
        # sketchDimensions[11].parameter.expression = str((D-d)/8) + " mm"


        # Изменяем количество цилиндров
        # patternFeature.quantity.expression = str(CylCount)

        # Изменяем отверстие для смазки
        # holeFeature.holeDiameter.expression = str(protochkParams["d0"]) + "mm"

        # # Правим скругления
        # filletFeatures[0].edgeSets[0].radius.expression = str(r) + " mm"
        # # filletFeatures[1].edgeSets[0].radius.expression = str(r1) + " mm"

        # toolBodies = adsk.core.ObjectCollection.create()
        # for body in revolveFeatures[1].bodies:
        #     toolBodies.add(body)
        # for body in patternFeature.bodies:
        #     toolBodies.add(body)

        # targetBody = revolveFeatures[2].bodies[0]

        # combineFeatures = component.features.combineFeatures
        # combineInput = combineFeatures.createInput(targetBody,toolBodies)
        # combineInput.isKeepToolBodies = True
        # combineInput.operation = 1

        # combineFeature = combineFeatures.add(combineInput)
        # combineFeature.timelineObject.rollTo(True)
        # combineFeature.toolBodies = toolBodies
        # combineFeature.timelineObject.rollTo(False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
