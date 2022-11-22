import os
from flask import Flask
import add_to_calendar

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    add_to_calendar.update()

    return ("", 204)

if __name__ == "__main__":

    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8090

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)




# import os
# import json
# from flask import Flask, request, jsonify
# from datetime import datetime, timedelta

# from teams import teams
# from games import games
# from officials import officials

# app = Flask(__name__)

# @app.route("/", methods=["POST", "OPTIONS"])
# def main(args=None):

#     if request.method == "OPTIONS":
#         print('options request')
#     # Allows GET requests from any origin with the Content-Type
#     # header and caches preflight response for an 3600s
#         headers = {
#             "Access-Control-Allow-Origin": "*",
#             "Access-Control-Allow-Methods": "GET, POST",
#             "Access-Control-Allow-Headers": "Content-Type, Authorization",
#             "Access-Control-Max-Age": "3600",
#         }

#         return ("", 204, headers)

#     if request.data:
#         request_json = json.loads(request.data)
#         result =  pipeline_entry(request_json['type'], request_json['gameID'])
#         if result:
#             response = jsonify(result)

#             response.headers.set("Content-Type","application/json")
#             response.headers.set("Access-Control-Allow-Origin", "*")
#             response.headers.set("Access-Control-Allow-Methods", "POST")

#             return response

#     else:
#         return ("ref-buddy-lagger", 204)

#     return ("", 204)


# def pipeline_entry(this_request_type, this_request_query):

#     module, function = this_request_type.split("-")
#     try:
#         function = getattr(globals()[module], function)
#     except Exception as e:
#         print(e)
#         print("Ensure the function exists")
#         return (f"Exception in calling function type {this_request_type}", 200)
#     return function(this_request_query)


# if __name__ == "__main__":

#     PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8083

#     # This is used wzhen running locally. Gunicorn is used to run the
#     # application on Cloud Run. See entrypoint in Dockerfile.
#     app.run(host="127.0.0.1", port=PORT, debug=True)
