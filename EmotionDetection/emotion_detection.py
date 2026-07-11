''' function for the emotion detection '''
import json
import requests

def emotion_detector(text_to_analyze):
    '''
    function that takes text_to_analyse 
    and returns text attribute of the response object
    '''
    url =(
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    #formatting to json
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        #extracting scores
        anger_score=formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score=formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score=formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score=formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score=formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]

        #calculate max value with attached to emotions
        dominant_score, dominant_emotion = max(zip(scores, emotions))
    
    # update for status code 400 
    elif response.status_code == 400:
        anger_score=None
        disgust_score=None
        fear_score=None
        joy_score=None
        sadness_score=None
        dominant_emotion=None

    #built the dict
    score_dict = {
    'anger': anger_score, 
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
    
    return score_dict
