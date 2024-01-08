import json, logging, pyodbc, os
import azure.functions as func


connection_string: str = os.environ["DATABASE_CONNECTION_STRING"]
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

    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [dbo].[Quotes]")
    
        quotes = cursor.fetchall()
        logging.info(quotes)
        quotesArr = []
        for quote in quotes:
          quotesArr.append({
            "name": quote.name,
            "text": quote.text
          })
        logging.info(quotesArr)
    return func.HttpResponse(json.dumps(quotesArr))
   