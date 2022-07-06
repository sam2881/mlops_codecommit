import logging
import pickle
import os
import gcp_model_pull as gcp
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/mlops-353417-0d6234ccd6b9.json'
bucket_name = "mlops_artifacts_1"
model_type = "artifacts"
model_filename = "0/07ce71e530e34d37803cfc1be8e4f9bc/artifacts/model/model.pkl"
name = "model.pkl"

app = Flask(__name__)


model_file = gcp.load_model(bucket_name, model_type, model_filename)

model_path = "model/model.pkl"
# loginfo('Loading model: {}'.format(model_path))
model = pickle.load(open(model_path, 'rb'))


# @app.before_first_request
# def load_trained_model():

@app.route('/')
def home():
    return "Hello World"


@app.route('/predict', methods=['POST'])
def predict():
    """Return a machine learning prediction."""
    input = request.get_json()
    print(input)
    # df2 = input.tolist()
    # df2 = pd.DataFrame.from_dict(input, orient="index").T
    # print(df2)
    predict1 = model.predict([np.array(list(input.values()))])
    output = predict1[0]
    return jsonify(output)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(port=9000, debug=True)
