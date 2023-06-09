# -*- coding: utf-8 -*-
"""Deploying_ML_model_as_public_API_ngrok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h2kai-ItSRIZ36rDsUbTkYxrYQ77frBA

Installing the dependencies
"""

!pip install fastapi
!pip install uvicorn
!pip install pickle5
!pip install pydantic
!pip install scikit-learn
!pip install requests
!pip install pypi-json
!pip install pyngrok
!pip install nest-asyncio

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    MDVPFo: float
    MDVPFhi: float
    MDVPFlo:float
    MDVPJitter: float
    MDVPJitter: float
    MDVPRAP: float
    MDVPPPQ: float
    JitterDDP:float
    MDVPShimmer: float
    MDVPShimmerDB: float
    ShimmerAPQ3: float
    ShimmerAPQ5:float
    MDVPAPQ:float
    DDA:float
    NHR:float
    HNR:float
    RPDE:float
    DFA:float
    spread1:float
    spread2:float
    D2:float
    PPE:float

diabetes_model = pickle.load(open('parkinsons_model.sav', 'rb'))

@app.post('/parkinsons_prediction')
def parkinsons_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    fo = input_dictionary('MDVPFo')
        
    fhi = input_dictionary('MDVPFhi')
        

    flo = input_dictionary('MDVPFlo')
        

    Jitter_percent = input_dictionary('MDVPJitter')
        

    Jitter_Abs = input_dictionary('MDVPJitter')
        

    RAP = input_dictionary('MDVPRAP')
        

    PPQ = input_dictionary('MDVPPPQ')
        

    DDP = input_dictionary('JitterDDP')
        

    Shimmer = input_dictionary('MDVPShimmer')
        
 
    Shimmer_dB = input_dictionary('MDVPShimmerDB')

    APQ3 = input_dictionary('ShimmerAPQ3')
        

    APQ5 = input_dictionary('ShimmerAPQ5')
        
 
    APQ = input_dictionary('MDVPAPQ')
        
   
    DDA = input_dictionary('DDA')
        

    NHR = input_dictionary('NHR')
        
  
    HNR = input_dictionary('HNR')
        
  
    RPDE = input_dictionary('RPDE')
        
   
    DFA = input_dictionary('DFA')
        

    spread1 = input_dictionary('spread1')
        

    spread2 = input_dictionary('spread2')
        
    
    D2 = input_dictionary('D2')
        
    PPE = input_dictionary('PPE')
    
    
    input_list = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
    
    prediction = parkinsons_model.predict(input_list)
    
    if (prediction[0] == 0):
        return "The person has perkinson's disease"
    else:
        return "The person doesn't has perkinson's disease"

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)

