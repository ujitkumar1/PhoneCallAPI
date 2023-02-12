from call_report import call_report
from initiate_call import initiate_call
from src import app, api

# adding the api for /initiate-call endpoint
api.add_resource(initiate_call, "/initiate-call")
# adding the api for /call-report endpoint
api.add_resource(call_report, "/call-report")

if __name__ == "__main__":
    # running the flask app
    app.run(debug=True)
