from flask import Flask,request,jsonify,json
import artifects

from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

@app.route('/',methods=['POST'])
def hello():
    json_data = request.get_json()
    return json_data["name"]


@app.route('/houselocations',methods=['GET'])
def GetHouselocations():
    
        
    response = jsonify(
        {
            "locations":artifects.getLocations()
        }
    )
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/predicPrice',methods=['POST'])
def predicPrice():
    json_data = request.get_json()
    
    location = json_data["location"]
    sqft = json_data["sqft"]
    bhk = json_data["bhk"]
    bath = json_data["bath"]
    
    result = jsonify(
        {
            "estimated_price":str(artifects.predictPrice(location,sqft,bhk,bath))+" Lakhs"
        }
    )
    
    result.headers.add('Access-Control-Allow-Origin','*')
    
    
    
    return result
        
    

if __name__ == "__main__":
    app.run(debug=True)