''' Executing this function initiates the application of emotion detection''' 
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_decting():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. 
        The output returnedas scores of the emotions and the dominant emotion.
    '''
    text_to_analyze=request.args.get('textToAnalyze')
    if len(text_to_analyze)==0:
        return "The string is empty"
    response=emotion_detector(text_to_analyze)
    return f"""For the given statement, the system response is 
        'anger': {response['anger']}, 
        'disgust': {response['disgust']}, 
        'fear': {response['fear']}, 
        'joy': {response['joy']} and 
        'sadness': {response['sadness']}. 
        The dominant emotion is <strong>{response['dominant_emotion']}<strong>."""
        

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)