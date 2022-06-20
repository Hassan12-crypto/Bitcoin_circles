# %% [markdown]
# ## BITCOIN CIRLCES

# %%
import pandas as pd
import json
import requests
from datetime import datetime
from datetime import timedelta
import pytz
import numpy as np
from math import pi, sqrt
from PIL import Image, ImageDraw, ImageEnhance
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import turtle
import time
from random import randrange

image_list = ['imge2.gif']
pos = [0, 240 , 0, 120, 240 , 80, 240]
pos1 = [120, 0, 240, 120, 240, 160, 120]
rpos = [(200, 90), (-200, -300), (100, 100), (200, -200), (-180, 120), (120, 120), (-200, -300)]

UTC = pytz.UTC
now = datetime.now(UTC) - timedelta(minutes=3000)
start = now - timedelta(minutes=2985)
# dd/mm/YY H:M:S
end_time = now.strftime("%Y-%m-%dT%H:%M:%S")
start_time = start.strftime("%Y-%m-%dT%H:%M:%S")
print("start_time=", (start + timedelta(minutes=1425)))
print("end_time=", (now  + timedelta(minutes=1440)))


url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=1MIN&time_start='+start_time+'&time_end='+end_time
headers = {'X-CoinAPI-Key' : 'D194CD0F-18D3-4777-8141-0EC4D87A88D8'}
response = requests.get(url, headers=headers)

# Open the input image as numpy array, convert to RGB

Highest_price = 61378.28
print(Highest_price)
rposc = 0
poscounter = -1
for j in range(10000000):
    print(response.text)
    df_current = pd.read_json(response.text)
    df_current
    Current_price = df_current["rate_high"].max()
    print(Current_price)

    if Current_price > Highest_price:
        Highest_price = Current_price
    else:
        pass

    cv = Current_price / 100000
    print(cv)

    cv1 = (Highest_price - Current_price)/100000
    print(cv1)

    counter = 1
    poscounter += 1
    for i in image_list:
        if rposc == 7 and poscounter == 7:
            rposc = 0
            poscounter = 0
        else:
            pass
        img=Image.open(i).convert("RGB")
        npImage=np.array(img)
        h,w=img.size
        x = round(sqrt((cv * 300 * 300 )) * 2)
        #print(x)

        # Create same size alpha layer with circle
        alpha = Image.new('L', img.size,0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([pos[poscounter], pos1[poscounter],  pos[poscounter] + x , pos1[poscounter]  + x],0,360,fill=255)


        # Convert alpha Image to numpy array
        npAlpha=np.array(alpha)

        # Add alpha layer to RGB
        npImage=np.dstack((npImage,npAlpha))

        # Save with alpha
        img = ImageEnhance.Color(img)
        img.enhance(1.5)
        Image.fromarray(npImage).save('result'+str(counter)+'.gif')

        #img = mpimg.imread('result'+str(counter)+'.gif')
        #imgplot = plt.imshow(img)
        #plt.show()
        #plt.close()
        counter += 1

    tur1 = turtle.Turtle()
    tr1 = turtle.Turtle()
    #tr2 = turtle.Turtle()
    #tur2 = turtle.Turtle()

    tur1.hideturtle()
    #tur2.hideturtle()
    wn = turtle.Screen()
    wn.tracer(2, 2)
    wn.setup(width=400,height=400)
    wn.bgcolor("black")

    tr1.goto(0, 0)
    #tr2.goto( 0 , 0)
    tur1.goto(rpos[rposc])
    #tur2.goto(60, -182)

    tur1.fillcolor('red')
    tur1.begin_fill()
    tur1.circle(round(sqrt((cv1 * 300 * 300 ))))
    tur1.end_fill()


    wn.addshape('result1.gif')
    #wn.addshape('result2.gif')
    tr1.shape('result1.gif')
    #tr2.shape('result2.gif')

    '''for i in range(50):
        if i % 2 != 0:
            tur2.fillcolor('black')
            tur2.begin_fill()
            tur2.circle((i*4)+50)
            tur2.end_fill()
        else:
            tur2.circle((i*4)+100)'''

    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=1MIN&time_start='+start_time+'&time_end='+end_time
    headers = {'X-CoinAPI-Key' : 'D194CD0F-18D3-4777-8141-0EC4D87A88D8'}
    response = requests.get(url, headers=headers)
    print(response.text)
    time.sleep(0.5)
    tur1.clear()
    tr1.hideturtle()
    tr1.clear()
    #tr2.hideturtle()
    rposc += 1

wn.mainloop()
turtle.bye()


