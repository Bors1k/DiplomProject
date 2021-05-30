# Author-
# Description-

import adsk.core
import adsk.fusion
import adsk.cam
import traceback
import math


def run(context):
    ui = None
    try:
        # Переменные
        params = {"d": 300, "D": 540, "B": 85, "r": 1.5, "r1": 1.0}
        d = params["d"]
        D = params["D"]
        B = params["B"]
        r = params["r"]
        r1 = params["r1"]

        # ADA = B*0.25
        # KAD1 = round(0.7 * (D-d) + d,2)
        # BAD1 = round(KAD1 / 1.111111,2)
        # BID1 = round((D+d)*0.5 - (BAD1 - (D+d)*0.5) * 2 / 3, 2)
        # KID1 = round(d + 0.3 * (D-d),2)

        ADA = B * 0.25
        BID1 = round((D-d)/3 + d, 2)
        BAD1 = round(D-(D-d)/3, 2)
        KID1 = round((D-d)/4.4444+d, 2)
        KAD1 = round(d+D-KID1, 2)


        CylCount = round((math.pi * (D+d) / 2) /
                         ((D - (KID1 - d) - KID1) / 2) / 2)

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
        # patternFeature = component.features.circularPatternFeatures[0]
        # Получаем скетч и его размеры
        # sketches = occurence.component.sketches[0]
        sketches = component.sketches[0]
        sketchDimensions = sketches.sketchDimensions
        # Получаем коллекцию скруглений
        # filletFeatures = occurence.component.features.filletFeatures
        # filletFeatures = component.features.filletFeatures

        # extrudeFeatures = component.features.extrudeFeatures

        # for dim in sketchDimensions:
        #     _dim = dim.parameter.expression
        # ui = 0

        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(d) + " mm"
        sketchDimensions[1].parameter.expression = str(B) + " mm"
        sketchDimensions[2].parameter.expression = str(ADA) + " mm"
        sketchDimensions[3].parameter.expression = str(D) + " mm"
        sketchDimensions[4].parameter.expression = str(KAD1) + " mm"
        sketchDimensions[5].parameter.expression = str(BAD1) + " mm"
        sketchDimensions[6].parameter.expression = str(BID1) + " mm"
        sketchDimensions[7].parameter.expression = str(KID1) + " mm"

        # Изменяем количество цилиндров
        # patternFeature.quantity.expression = str(CylCount)

        # Правим скругления
        # filletFeatures[0].edgeSets[0].radius.expression = str(r) + " mm"
        # filletFeatures[1].edgeSets[0].radius.expression = str(r1) + " mm"

        u = 0
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
