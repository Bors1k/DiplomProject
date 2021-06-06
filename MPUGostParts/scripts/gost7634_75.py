import adsk.core
import adsk.fusion
import adsk.cam
import traceback
import math
from . import gost7634_75K

def run(occurence, Info):
    # Переменные
    gostType = Info["TYPE"]
    params = Info["PARAMS"].split("/") 
    d = float(params[0])
    D = float(params[1])
    B = float(params[2])
    r = float(params[3])

    if("k" in gostType):
        protochkParams = gost7634_75K.run(d,gostType)

    _d = B/12 + d #Диаметр для построения конусности
    CylCount = round((d+D)*math.pi/((D-d)/4)/4) #Кол-во цилиндров

    # Получаем массив
    patternFeature = occurence.component.features.circularPatternFeatures[0]
    # Получаем скетч и его размеры
    sketches = occurence.component.sketches[0]
    sketchDimensions = sketches.sketchDimensions
    # Получаем скругление
    filletFeature = occurence.component.features.filletFeatures[0]
    # получаем вращения
    revolveFeatures = occurence.component.features.revolveFeatures
    # получаем отверстие
    if("k" in gostType):
        holeFeature = occurence.component.features.holeFeatures[0]

    if(gostType=="162000" or gostType=="1 - 162000k" or gostType=="2 - 162000k"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(D) + " mm"
        sketchDimensions[1].parameter.expression = str(d) + " mm"
        sketchDimensions[2].parameter.expression = str(B/7) + " mm"
        sketchDimensions[3].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[4].parameter.expression = str(B) + " mm"
        sketchDimensions[5].parameter.expression = str((D-d)/4) + " mm"
        sketchDimensions[6].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[7].parameter.expression = str((D-d)/16) + " mm"
        sketchDimensions[8].parameter.expression = str(_d) + " mm"
        sketchDimensions[11].parameter.expression = str((D-d)/8) + " mm"
        sketchDimensions[12].parameter.expression = str((D-d)/8) + " mm"

        if ("1 -" in gostType):
            sketchDimensions[13].parameter.expression = str(protochkParams["R"]*2) + " mm"
            sketchDimensions[14].parameter.expression = str(protochkParams["t"]) + " mm"
        if ("2 -" in gostType):
            sketchDimensions[15].parameter.expression = str(protochkParams["b0"]) + " mm"

    elif(gostType=="182000" or gostType=="1 - 182000k" or gostType=="2 - 182000k"):
        # Вносим новые параметры
        sketchDimensions[2].parameter.expression = str(D) + " mm"
        sketchDimensions[3].parameter.expression = str(d) + " mm"
        sketchDimensions[4].parameter.expression = str(B/7) + " mm"
        sketchDimensions[5].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[6].parameter.expression = str(B) + " mm"
        sketchDimensions[7].parameter.expression = str((D-d)/4) + " mm"
        sketchDimensions[8].parameter.expression = str((D-d)/4) + " mm"
        sketchDimensions[9].parameter.expression = str((D-d)/8) + " mm"
        sketchDimensions[10].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[11].parameter.expression = str((D-d)/16) + " mm"
        sketchDimensions[12].parameter.expression = str(_d) + " mm"

        if ("1 -" in gostType):
            sketchDimensions[13].parameter.expression = str(protochkParams["R"]*2) + " mm"
            sketchDimensions[14].parameter.expression = str(protochkParams["t"]) + " mm"
        if ("2 -" in gostType):
            sketchDimensions[15].parameter.expression = str(protochkParams["b0"]) + " mm"

    elif(gostType=="262000" or gostType=="1 - 262000k" or gostType=="2 - 262000k"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(D) + " mm"
        sketchDimensions[1].parameter.expression = str(d) + " mm"
        sketchDimensions[2].parameter.expression = str(B/7) + " mm"
        sketchDimensions[3].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[4].parameter.expression = str(B) + " mm"
        sketchDimensions[5].parameter.expression = str((D-d)/4) + " mm"
        sketchDimensions[6].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[7].parameter.expression = str((D-d)/16) + " mm"
        sketchDimensions[10].parameter.expression = str((D-d)/8) + " mm"
        sketchDimensions[11].parameter.expression = str((D-d)/8) + " mm"

        if ("1 -" in gostType):
            sketchDimensions[12].parameter.expression = str(protochkParams["R"]*2) + " mm"
            sketchDimensions[13].parameter.expression = str(protochkParams["t"]) + " mm"
        if ("2 -" in gostType):
            sketchDimensions[14].parameter.expression = str(protochkParams["b0"]) + " mm"


    elif(gostType=="28200" or gostType=="1 - 282000k" or gostType=="2 - 282000k"):
        # Вносим новые параметры
        sketchDimensions[2].parameter.expression = str(D) + " mm"
        sketchDimensions[3].parameter.expression = str(d) + " mm"
        sketchDimensions[4].parameter.expression = str(B/7) + " mm"
        sketchDimensions[5].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[6].parameter.expression = str(B) + " mm"
        sketchDimensions[7].parameter.expression = str((D-d)/4) + " mm"
        sketchDimensions[8].parameter.expression = str((D-d)/4) + " mm"
        sketchDimensions[9].parameter.expression = str((D-d)/8) + " mm"
        sketchDimensions[10].parameter.expression = str(B*2/7) + " mm"
        sketchDimensions[11].parameter.expression = str((D-d)/16) + " mm"
    
        if ("1 -" in gostType):
            sketchDimensions[12].parameter.expression = str(protochkParams["t"]) + " mm"
            sketchDimensions[13].parameter.expression = str(protochkParams["R"]*2) + " mm"
        if ("2 -" in gostType):
            sketchDimensions[14].parameter.expression = str(protochkParams["b0"]) + " mm"

    elif(gostType=="452000" or gostType=="1 - 452000k" or gostType=="2 - 452000k"):
        CylCount = round((d+D)*math.pi/((D-d)/5)/4)
        # Вносим новые параметры
        sketchDimensions[3].parameter.expression = str(D) + " mm"
        sketchDimensions[0].parameter.expression = str(d) + " mm"
        sketchDimensions[4].parameter.expression = str(B) + " mm"
        sketchDimensions[5].parameter.expression = str((D-d)/5) + " mm"
        sketchDimensions[6].parameter.expression = str((B/9-0.5)/2+0.5) + " mm"
        sketchDimensions[7].parameter.expression = str((D-d)/5/2) + " mm"
        sketchDimensions[8].parameter.expression = str(B/9 - 0.5) + " mm"
        sketchDimensions[10].parameter.expression = str(B/9 - 0.5) + " mm"
        sketchDimensions[12].parameter.expression = str(B/9 - 0.5) + " mm"
        sketchDimensions[14].parameter.expression = str(B/9 - 0.5) + " mm"
        sketchDimensions[16].parameter.expression = str(B/9 - 0.5) + " mm"
        sketchDimensions[18].parameter.expression = str(B/9 - 0.5) + " mm"
        sketchDimensions[21].parameter.expression = str(B/9 - 0.5) + " mm"

        if ("1 -" in gostType):
            sketchDimensions[22].parameter.expression = str(protochkParams["t"]) + " mm"
            sketchDimensions[23].parameter.expression = str(protochkParams["R"]*2) + " mm"
        if ("2 -" in gostType):
            sketchDimensions[24].parameter.expression = str(protochkParams["b0"]) + " mm"
        
    # Изменяем количество цилиндров
    patternFeature.quantity.expression = str(CylCount)

    # Правим скругления
    filletFeature.edgeSets[0].radius.expression = str(r) + " mm"

    if ("k" in gostType):
        # Изменяем отверстие для смазки
        holeFeature.holeDiameter.expression = str(protochkParams["d0"]) + "mm"

    if(gostType!="452000" and gostType!="1 - 452000k" and gostType!="2 - 452000k"):
        # Создаем коллекцию объектов
        toolBodies = adsk.core.ObjectCollection.create()
        # Получаем из вращения 2 базовых тела качения(ролика)
        for body in revolveFeatures[1].bodies:
            toolBodies.add(body)
        # Получаем из кругового массива оставшиеся тела качения(ролики)
        for body in patternFeature.bodies:
            toolBodies.add(body)

        # Получаем targetBody
        targetBody = revolveFeatures[2].bodies[0]

        # Получаем combineFeatures для компонента
        combineFeatures = occurence.component.features.combineFeatures
        # Создаем combineInput для создания комбайна
        combineInput = combineFeatures.createInput(targetBody,toolBodies)
        # Сохранить toolsBodies после операции
        combineInput.isKeepToolBodies = True
        # Установка типа операции cut
        combineInput.operation = 1
        # Добавляем комбинирование
        combineFeature = combineFeatures.add(combineInput)