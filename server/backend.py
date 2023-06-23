from sagemaker import Model, serializers, deserializers
import pprint
import sagemaker
import boto3
import json
from time import sleep, perf_counter as pc
from pprint import pprint
from flask import Flask
from flask import request
import asyncio

app = Flask(__name__)

def getSuggestions(contact):

    t0 = pc()
    print(contact)
    
    sess = sagemaker.Session(boto3.session.Session(region_name="us-east-2"))
        
    predictor = sagemaker.Predictor(
        endpoint_name="csllmhackathon-vicuna-13b",
        sagemaker_session=sess,
        serializer=serializers.JSONSerializer(),
        deserializer=deserializers.JSONDeserializer(),
    )
        
    prompts = [
       contact,
    ]

    input_data = {
        "inputs": prompts,
        "parameters": {
            "max_new_tokens": 1024, # use 400 for falcon-7b/mpt-7b
            "do_sample": True,
            "temperature": 0.9,
            "top_k": 20, 
            "top_p": 0.99,
        },
    }

    result = predictor.predict(input_data)
    pprint(result)
    return result;

@app.route('/getResponse', methods=['POST'])
def login():
    contact = request.get_json()['contact']
    result = getSuggestions(contact)
    print(result['outputs'][0])
    return result
     