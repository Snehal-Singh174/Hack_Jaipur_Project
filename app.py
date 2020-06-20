from flask import Flask,render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import nltk
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    if request.method == 'POST':
        comment = request.form['comment']
        ss = sid.polarity_scores(comment)
        ans=max(ss,key=ss.get)
        if ans=="pos":
            ans='Thanks for spending time with us you have a healthy mind.'
        if ans=="neg":
            ans='You have to do meditation and reach out to Doctor.'
        if ans=="neu" or ans=="compound":
            if abs(ss['pos']-ss['neg'])<0.21:
                ans='Spend time in Yoga no need to worry.'
            elif ss['pos']>ss['neg']:
                ans='Thanks for spending time with us you have a healthy mind.'
            else:
                ans='You have to do meditation and reach out to Doctor.'

    return render_template('index1.html',prediction = ans,prediction1 = comment)



if __name__ == '__main__':
	app.run(debug=True)