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
        params = {"d": 15, "D": 42, "B": 13, "r": 1.5, "r1": 0.8}
        d = params["d"]
        D = params["D"]
        B = params["B"]
        r = params["r"]
        r1 = params["r1"]

        ADA = B*0.25
        KAD1 = 0.7 * (D-d) + d
        BAD1 = KAD1 / 1.111111
        BID1 = BAD1 - (BAD1 - (D+d)*0.5) * 2 / 3
        KID1 = d + 0.3 * (D-d)

        CylCount = round(
            math.pi * (KID1 + 0.5*(KAD1-KID1)) / ((KAD1-KID1)/2)/2)

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

        for dim in sketchDimensions:
            _dim = dim.parameter.expression
        ui = 0
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(d) + " mm"
        sketchDimensions[1].parameter.expression = str(B) + " mm"
        sketchDimensions[3].parameter.expression = str(D) + " mm"
        sketchDimensions[4].parameter.expression = str(ADA) + " mm"
        sketchDimensions[5].parameter.expression = str(BID1) + " mm"
        sketchDimensions[6].parameter.expression = str(KID1) + " mm"
        sketchDimensions[7].parameter.expression = str(BAD1) + " mm"
        sketchDimensions[8].parameter.expression = str(KAD1) + " mm"

        # Изменяем количество цилиндров
        # patternFeature.quantity.expression = str(CylCount)

        # Правим скругления
        # filletFeatures[0].edgeSets[0].radius.expression = str(r) + " mm"
        # filletFeatures[1].edgeSets[0].radius.expression = str(r1) + " mm"

        u = 0
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
