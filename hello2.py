import numpy as np
import pandas as pd
from flask import Flask,render_template
import time

df=pd.read_csv('C:\\Users\\DELL\\Desktop\\600.csv')
pa=df['Pa'].values[0:100]
pb=df['Pa'].values[100:1000]
ua=df['ua'].values[0:100]
ub=df['ua'].values[0:1000]
ia=df['ia'].values[0:100]
ib=df['ia'].values[0:1000]
Pa=df['P'].values[0:100]
Pb=df['P'].values[0:1000]
PFa=df['PF'].values[0:100]
PFb=df['PF'].values[0:1000]
time1=df['time'].values[0:100]
time2=df['time'].values[0:1000]
timea=np.zeros(time1.shape[0])
timeb=np.zeros(time2.shape[0])
for i in range(time1.shape[0]):
    timea[i] = time.mktime(time.strptime(time1[i], "%Y-%m-%d %H:%M:%S.%f"))
for j in range(time2.shape[0]):
    timeb[j] = time.mktime(time.strptime(time2[j], "%Y-%m-%d %H:%M:%S.%f"))


app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('test.html',pa=pa,pb=pb,ua=ua,ub=ub,ia=ia,ib=ib,Pa=Pa,Pb=Pb,PFa=PFa,PFb=PFb,timea=timea,timeb=timeb)

if __name__ == '__main__':
    app.run()