import azure.functions as func
import logging
import json
import random
import string
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    surname = ''.join(random.choices(string.ascii_lowercase, k=5))
    return func.HttpResponse(
            #body=json.dumps([{"name": name, "surname": surname}]),
            body=json.dumps({
                "status": "OK",
                "items" : [{"name": name, "surname": surname}]
                }
            ),
            status_code=200,
            mimetype="application/json"
    )
