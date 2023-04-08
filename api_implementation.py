import json
import requests


url = ' http://0486-35-237-10-36.ngrok.io/parkinsons_prediction'

input_data_for_model = {
    'MDVPFo':119.992,
    'MDVPFhi':157.302,
    'MDVPFlo':74.997,
    'MDVPJitter':0.007,
    'MDVPJitter':0.000007,
    'MDVPRAP':0.0037,
    'MDVPPPQ':0.00554,
    'JitterDDP':0.01109,
    'MDVPShimmer':0.043,
    'MDVPShimmerdB':0.426,
    'ShimmerAPQ3':0.0218,
    'ShimmerAPQ5':0.0313,
    'MDVPAPQ':0.029,
    'DDA':0.065,
    'NHR':0.022,
    'HNR':21.033,
    'RPDE':0.0414783,
    'DFA':0.815285,
    'spread1':-4.81303,
    'spread2':0.266482,
    'D2':2.301,
    'PPE':0.284654}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
print(response.text)

