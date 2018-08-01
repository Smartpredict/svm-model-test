from flask import Flask, jsonify, request
from sklearn.externals import joblib

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            body = request.get_json()
            data = [body["imdata"]]
            svm_model = joblib.load("./svm.pkl")
            prediction = svm_model.predict(data)
            y = str(prediction[0])
            print(y)

        except ValueError:
            return jsonify("Error")

        return jsonify({'Prediction venant du server': y})


if __name__ == '__main__':
    app.run(debug=True)


