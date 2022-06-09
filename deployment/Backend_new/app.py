from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


results = ['Not Satisfied', 'Satisfied']
columns = ['Gender','Age','Customer_Type','Class', 'Type_Travel', 
'Inflight_wifi','Ease_booking', 'Online_boarding', 'On-board_service','Seat_comfort', 
'Inflight_entertainment', 'Leg_room', 'Checkin_service', 
'Cleanliness', 'Flight_distance','Baggage_handling', 'Inflight_service','Dep/Arv_time','Gate_location', 'Food_drink','Arrival_delay', 'Departure_delay']

@app.route("/")
def home():
    return "<h1>Welcome!</h1>"


@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try: 
            data= [content['Gender'],
                   content['Age'],
                   content['Customer_Type'],
                   content['Class'],
                   content['Type_Travel'],
                   content['Inflight_wifi'],
                   content['Ease_booking'],
                   content['Online_boarding'],
                   content['Seat_comfort'],
                   content['Inflight_entertainment'],
                   content['On-board_service'],
                   content['Leg_room'],
                   content['Checkin_service'],
                   content['Cleanliness'],
                   content['Flight_distance'],
                   content['Baggage_handling'],
                   content['Inflight_service'],
                   content['Dep/Arv_time'],
                   content['Gate_location'],
                   content['Food_drink'],
                   content['Arrival_delay'],
                   content['Departure_delay']]
            data = pd.DataFrame([data], columns = columns)
            res = model.predict(data)
            response = {'code' : 200, 'status' : 'OK', 'result' : {'description' : results[res[0]]}}
            return jsonify(response)
            
        except Exception as e :
                    response2 = {'code' : 400, 'status' : 'Error', 'result' : {'error_msg' : str(e)}}
                    return jsonify(response2)
    return "<p> Please Use Post Methods To Access The Prediction </p>"

#app.run(debug=True)