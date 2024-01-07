import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

quotes = [{
  "name": "test 1 from api",
  "text": "quote text 1"
}, {
  "name": "test 2 from api",
  "text": "quote text 2"
}]

@app.route(route="getQuotes")
def getQuotes(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(json.dumps(quotes))
   