import adsk.core
import adsk.fusion
import adsk.cam
import traceback
import math
from .gost22696_2013 import ShortCylSizes

def run(occurence, Info):
    
    # Переменные
    gostType = Info["TYPE"]
    params = Info["PARAMS"].split("/")

    # выборка параметром в зависимости от кол-ва переменных
    # для подшипников с упорным кольцом, их будет больше
    if len(params) == 5:
        d = float(params[0])
        D = float(params[1])
        B = float(params[2])
        r = float(params[3])
        r1 = float(params[4])
    else:
        d = float(params[0])
        D = float(params[1])
        B = float(params[2])
        b = float(params[3])
        r = float(params[4])
        r1 = float(params[5])


    if(gostType == "2000"):
        ADA = B*0.25
        BID1 = d + (D-d)/3.33333333
        KAD1 = BID1 + 1.33333 * (D-d)/3.33333333
        KID1 = BID1 / 1.11111111111

        CylCount = round(
            math.pi * (KID1 + 0.5*(KAD1-KID1)) / ((KAD1-KID1)/2)/2)

    elif(gostType == "12000"):
        ADA = B*0.25
        KAD1 = round(0.7 * (D-d) + d, 2)
        BAD1 = round(KAD1 / 1.111111, 2)
        BID1 = round((D+d)*0.5 - (BAD1 - (D+d)*0.5) * 2 / 3, 2)
        KID1 = round(d + 0.3 * (D-d), 2)

        CylCount = round(math.pi * (KID1 + 0.5*(KAD1-KID1)) / ((KAD1-KID1)/2)/2)

    elif(gostType == "32000"):
        ADA = B * 0.25
        KID1 = round((D+d - (D-d)/2.5)/2, 2)
        KAD1 = round(D - (0.5*(KID1-d))*2, 2)
        BAD1 = round(KAD1/1.111111, 2)

        CylCount = round((math.pi * (D+d) / 2) /
                         ((D - (KID1 - d) - KID1) / 2) / 2)

    elif(gostType == "42000"):
        ADA = B * 0.25
        BAD1 = round((D-d)*0.2+(D+d)*0.5, 2)
        BID1 = round(BAD1-(D-d)*0.4, 2)
        KID1 = round(BID1/1.1111111111, 2)
        KAD1 = round(d+D-KID1, 2)


        CylCount = round((math.pi * (D+d) / 2) /
                         ((D - (KID1 - d) - KID1) / 2) / 2)

    elif(gostType == "92000"):
        ADA = B * 0.25
        BID1 = round((D-d)/3 + d, 2)
        BAD1 = round(D-(D-d)/3, 2)
        KID1 = round((D-d)/4.4444+d, 2)
        KAD1 = round(d+D-KID1, 2)


        CylCount = round((math.pi * (D+d) / 2) /
                         ((D - (KID1 - d) - KID1) / 2) / 2)

    # Получаем массив
    patternFeature = occurence.component.features.circularPatternFeatures[0]
    # Получаем скетч и его размеры
    sketches = occurence.component.sketches[0]
    sketchDimensions = sketches.sketchDimensions
    # Получаем коллекцию скруглений
    filletFeatures = occurence.component.features.filletFeatures

    if(gostType == "2000"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(B) + " mm"
        sketchDimensions[1].parameter.expression = str(d) + " mm"
        sketchDimensions[2].parameter.expression = str(ADA) + " mm"
        sketchDimensions[3].parameter.expression = str(KID1) + " mm"
        sketchDimensions[4].parameter.expression = str(BID1) + " mm"
        sketchDimensions[5].parameter.expression = str(KAD1) + " mm"
        sketchDimensions[8].parameter.expression = str(D) + " mm"

    elif(gostType == "12000"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(d) + " mm"
        sketchDimensions[1].parameter.expression = str(B) + " mm"
        sketchDimensions[3].parameter.expression = str(D) + " mm"
        sketchDimensions[4].parameter.expression = str(ADA) + " mm"
        sketchDimensions[5].parameter.expression = str(BID1) + " mm"
        sketchDimensions[6].parameter.expression = str(KID1) + " mm"
        sketchDimensions[7].parameter.expression = str(BAD1) + " mm"
        sketchDimensions[8].parameter.expression = str(KAD1) + " mm"

    elif(gostType == "32000"):
        # Вносим новые параметры
        sketchDimensions[1].parameter.expression = str(B) + " mm"
        sketchDimensions[2].parameter.expression = str(d) + " mm"
        sketchDimensions[3].parameter.expression = str(KID1) + " mm"
        sketchDimensions[4].parameter.expression = str(ADA) + " mm"
        sketchDimensions[5].parameter.expression = str(D) + " mm"
        sketchDimensions[6].parameter.expression = str(KAD1) + " mm"
        sketchDimensions[7].parameter.expression = str(BAD1) + " mm"

    elif(gostType == "42000"):
        # Вносим новые параметры
        sketchDimensions[0].parameter.expression = str(d) + " mm"
        sketchDimensions[2].parameter.expression = str(B) + " mm"
        sketchDimensions[3].parameter.expression = str(ADA) + " mm"
        sketchDimensions[4].parameter.expression = str(D) + " mm"
        sketchDimensions[5].parameter.expression = str(KAD1) + " mm"
        sketchDimensions[6].parameter.expression = str(BAD1) + " mm"
        sketchDimensions[7].parameter.expression = str(BID1) + " mm"
        sketchDimensions[8].parameter.expression = str(KID1) + " mm"

    elif(gostType == "92000"):
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
    patternFeature.quantity.expression = str(CylCount)

    # Правим скругления
    filletFeatures[0].edgeSets[0].radius.expression = str(r) + " mm"
    filletFeatures[1].edgeSets[0].radius.expression = str(r1) + " mm"
