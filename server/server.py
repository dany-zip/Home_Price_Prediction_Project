from flask import Flask, request, jsonify # flask write python service which serve http request
import util

# request call : whenever we will make http call from html application
# we will get all inputs in request.form

app=Flask(__name__)

@app.route('/get_location_names')
def get_location_names():           # first routine created is get_location_name using jsonify (serialize data)
   response = jsonify({
       'locations': util.get_location_names()
   })

   response.headers.add('Access-Control-Allow-Origin','*')
   return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])  #getting all inputs in request.form
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response=jsonify({      #response
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ =="__main__":
    print("Starting flask server for home prediction")
    app.run()
print("hello its working for now...........")

