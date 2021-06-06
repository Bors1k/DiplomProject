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
    H = float(params[2])
    D1 = float(params[3])
    d1 = float(params[4])
    r = float(params[5])

    CylCount = round((d+D)*math.pi/((D-d)/4)/4) #Кол-во цилиндров

    # Получаем массив
    patternFeature = occurence.component.features.circularPatternFeatures[0]
    # Получаем скетч и его размеры
    sketches = occurence.component.sketches
    sketchDimensions = sketches[0].sketchDimensions
    sketchDimensions1 = sketches[1].sketchDimensions
    # Получаем скругление
    filletFeature = occurence.component.features.filletFeatures[0]

    if(gostType=="9000"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(H) + " mm"
        sketchDimensions[1].parameter.expression = str(d) + " mm"
        sketchDimensions[2].parameter.expression = str(d1) + " mm"
        sketchDimensions[3].parameter.expression = str(D) + " mm"
        sketchDimensions[4].parameter.expression = str(D1) + " mm"
        sketchDimensions[5].parameter.expression = str(H/5) + " mm"
        sketchDimensions[6].parameter.expression = str((D-d1)/2.5) + " mm"
        sketchDimensions[7].parameter.expression = str((D-d1)/4) + " mm"
        sketchDimensions[8].parameter.expression = str(H/3) + " mm"

    elif(gostType=="889000"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(H) + " mm"
        sketchDimensions[1].parameter.expression = str(d1) + " mm"
        sketchDimensions[2].parameter.expression = str(d) + " mm"
        sketchDimensions[3].parameter.expression = str(D1) + " mm"
        sketchDimensions[4].parameter.expression = str(D) + " mm"
        sketchDimensions[5].parameter.expression = str(H/5) + " mm"
        sketchDimensions[6].parameter.expression = str((D-d1)/2.5) + " mm"
        sketchDimensions[7].parameter.expression = str(H/3) + " mm"
        sketchDimensions[8].parameter.expression = str((D-d1)/60) + " mm"
        sketchDimensions[9].parameter.expression = str((D-d1)/6) + " mm"

        sketchDimensions1[0].parameter.expression = str(D/12+5*d1/12) + " mm"
        sketchDimensions1[1].parameter.expression = str(3*(D-d1)/20) + " mm"
        sketchDimensions1[2].parameter.expression = str(H/3) + " mm"

        occurence.component.constructionPlanes[0].definition.angle.expression = str(360/(round(9*d/H)*2)) + "deg"

    # Изменяем количество цилиндров
    patternFeature.quantity.expression = str(CylCount)

    # Правим скругления
    filletFeature.edgeSets[0].radius.expression = str(r) + " mm"