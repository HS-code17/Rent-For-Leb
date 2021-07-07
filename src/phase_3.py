# a function that purely deals with flask
from flask import Flask, render_template
from phase_2 import scrape_url


# scrape function should return results
# check out what other flask requirements
# maybe this needs to be included in the main
# final_result = scrape_url()

app = Flask(__name__,template_folder= "templates")
@app.route('/')
def hello():
	return render_template('index.html', result= final_result, name= length_1, along= length_2)
# app.run(host='localhost', port=5000)
if __name__ == '__main__':
    final_result = scrape_url()
    app.run(debug=False)