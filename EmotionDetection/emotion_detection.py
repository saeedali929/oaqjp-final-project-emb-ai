import requests
from pprint import pprint
import json 
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_payload = { "raw_document": { "text": text_to_analyze }} 
    response = requests.post(URL, headers= headers, json = my_payload)
    text = response.text
    response_dict = json.loads(text)
    emotion_dict = response_dict["emotionPredictions"][0]["emotion"]
    return emotion_dict


def dominant_emotion(response_dict):
    
    emotion_dict_keys = list(emotion_dict.keys())
    dominant_emotion = list(emotion_dict.keys())[0]
    highest_score = emotion_dict[dominant_emotion]
    for key in emotion_dict_keys:
        if emotion_dict[key] > highest_score:
            highest_score = emotion_dict[key]
            dominant_emotion = key

    print(f"Dominant Emotion is {dominant_emotion}")
    








if __name__ == "main":
    emotion_dict = emotion_detector("I love Pizza")
    dominant_emotion(emotion_dict)
     