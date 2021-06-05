import adsk.core
import adsk.fusion
import adsk.cam
import traceback
import math

def run(occurence, Info):
    # Переменные
    gostType = Info["TYPE"]
    params = Info["PARAMS"].split("/")
    d = float(params[0])
    D = float(params[1])
    B = float(params[2])
    r = float(params[3])

    _d = B/12 + d #Диаметр для построения конусности
    CylCount = round((d+D)*math.pi/((D-d)/4)/4) #Кол-во цилиндров

    # Получаем массив
    patternFeature = occurence.component.features.circularPatternFeatures[0]
    # Получаем скетч и его размеры
    sketches = occurence.component.sketches[0]
    sketchDimensions = sketches.sketchDimensions
    # Получаем скругление
    filletFeature = occurence.component.features.filletFeatures[0]
    # получаем вращение
    revolveFeature = occurence.component.features.revolveFeatures[1]

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

    # Изменяем количество цилиндров
    patternFeature.quantity.expression = str(CylCount)

    # Правим скругления
    filletFeature.edgeSets[0].radius.expression = str(r) + " mm"
    # Получаем combine
    combineFeature = occurence.component.features.combineFeatures[0]
    # Создаем коллекцию объектов
    toolBodies = adsk.core.ObjectCollection.create()
    # Получаем из вращения 2 базовых тела качения(ролика)
    for body in revolveFeature.bodies:
        toolBodies.add(body)
    # Получаем из кругового массива оставшиеся тела качения(ролики)
    for body in patternFeature.bodies:
        toolBodies.add(body)
    # Устанавливаем таймлайн на до combine
    combineFeature.timelineObject.rollTo(True)
    # Присваиваем toolBodies для combine
    combineFeature.toolBodies = toolBodies
    # Возвращаем таймлайн на после combine
    combineFeature.timelineObject.rollTo(False)