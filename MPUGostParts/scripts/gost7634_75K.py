# Вспомогательная функция для создания проточек и отверстия для смазки
def run(d,gosttype):
    params = {}
    if(gosttype=="1 - 182000k" or gosttype=="1 - 282000k" or gosttype=="1 - 452000k" or gosttype=="2 - 182000k" or gosttype=="2 - 282000k" or gosttype=="2 - 452000k"):
        if(d<65):
            params = {'d0':2,"R":4,"t":0.8,"b0":4.5}
        elif(d>=65 and d<=120):
            params = {'d0':3.2,"R":6.4,"t":1.2,"b0":6.4}
        elif(d>=120 and d<=170):
            params = {'d0':4.8,"R":9.6,"t":1.8,"b0":9.5}
        elif(d>=170 and d<=200):
            params = {'d0':6.3,"R":12.6,"t":2.4,"b0":12.2}
        elif(d>=200 and d<=280):
            params = {'d0':8.0,"R":16,"t":3.0,"b0":15}
        elif(d>=280 and d<=420):
            params = {'d0':9.5,"R":19,"t":3.2,"b0":17.7}
        elif(d>=420 and d<=500):
            params = {'d0':12.7,"R":24,"t":4.8,"b0":23.5}

    elif(gosttype=="1 - 162000k" or gosttype=="1 - 262000k" or gosttype=="2 - 162000k" or gosttype=="2 - 262000k"):
        if(d>=100 and d<=170):
            params = {'d0':3.2,"R":6.4,"t":1.2,"b0":6.4}
        elif(d>=170 and d<=190):
            params = {'d0':4.8,"R":9.6,"t":1.8,"b0":9.5}
        elif(d>=190 and d<=240):
            params = {'d0':6.3,"R":12.6,"t":2.4,"b0":12.2}
        elif(d>=240 and d<=280):
            params = {'d0':8.0,"R":16,"t":3.0,"b0":15}
        elif(d>=280 and d<=460):
            params = {'d0':9.5,"R":19,"t":3.2,"b0":17.7}

    return params