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
        params = {"d": 170, "D": 260, "B": 160, "r": 3.5}
        d = params["d"]
        D = params["D"]
        B = params["B"]
        r = params["r"]

        _d = B/12 + d

        protochkParams = gost7634_75K.run(d,"16200")

        CylCount = round((d+D)*math.pi/((D-d)/5)/4)

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
        sketches = component.sketches[0]
        sketchDimensions = sketches.sketchDimensions
        # Получаем коллекцию скруглений
        # filletFeatures = occurence.component.features.filletFeatures
        filletFeatures = component.features.filletFeatures
        revolveFeatures = component.features.revolveFeatures
        holeFeature = component.features.holeFeatures[0]
        # combineFeatures.targetBody
        i = 0
        # extrudeFeatures = component.features.extrudeFeatures
        _params = {"d": 100, "D": 140, "B": 40, "r": 2}

        boolean = True
        i = 0
        num = -1
        while(boolean):
            num = -1
            for dim in sketchDimensions:
                _dim = dim.parameter.expression
                num = num + 1
            i = i+1
            if (i == 5):
                boolean = False

        # Вносим новые параметры
        # sketchDimensions[0].parameter.expression = str(D) + " mm"
        # sketchDimensions[1].parameter.expression = str(d) + " mm"
        # sketchDimensions[2].parameter.expression = str(B/7) + " mm"
        # sketchDimensions[3].parameter.expression = str(B*2/7) + " mm"
        # sketchDimensions[4].parameter.expression = str(B) + " mm"
        # sketchDimensions[5].parameter.expression = str((D-d)/4) + " mm"
        # sketchDimensions[6].parameter.expression = str(B*2/7) + " mm"
        # sketchDimensions[7].parameter.expression = str((D-d)/16) + " mm"
        # sketchDimensions[8].parameter.expression = str(_d) + " mm"
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

        # combineFeature = component.features.combineFeatures[0]

        # toolBodies = adsk.core.ObjectCollection.create()
        # for body in revolveFeatures[1].bodies:
        #     toolBodies.add(body)
        # for body in patternFeature.bodies:
        #     toolBodies.add(body)
        
        # combineFeature.timelineObject.rollTo(True)
        # combineFeature.toolBodies = toolBodies
        # combineFeature.timelineObject.rollTo(False)

        u = 0
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
