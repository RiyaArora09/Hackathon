from sagemaker import Model, serializers, deserializers
import pprint
import sagemaker
import boto3
import json
from time import sleep, perf_counter as pc
from pprint import pprint
from flask import Flask, jsonify
from flask import request
import asyncio
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    query = f"\"USER: If user requests for resetting password of Amazon Flex account, then send instructions to reset password from the Document:\"How to reset password?\". If user is experiencing issues with the Amazon Flex app, then send them the HMD 'amazon_flex_app_retry_sync_error'. If user asks payment is not received, then checkout the Doc: \"How to check if Amazon Flex pay is credited?\" and follow the instructions there. If the request is related to questions on onboarding to Amazon Flex, then refer them to the link: \" https://flex.amazon.com \". Based on the previous strategies. Say a request comes, \"{contact}.\", based on previous examples, what action will be taken?. If any document/HMD is there, make sure to mention it and do not add anything which is not speecified. Try to best match it to one of the cases, and give the corresponding suggestion. Do not mix and match. Also, suggestion should be less than 10 words.\n ASSISTANT: \""
    result = getSuggestions(query)
    print(result['outputs'][0])
    data = {
        'message': result['outputs'][0],
        'status': 'success'
    }
    return jsonify(data)
     
@app.route("/")
def hello_world():
    data = {
        'message': 'Hello, world!',
        'status': 'success'
    }
    return jsonify(data)