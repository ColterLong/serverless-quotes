import json, logging, pyodbc, os
import azure.functions as func


connection_string: str = os.environ["DATABASE_CONNECTION_STRING"]
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

hasContactedDatabase = False
quotesArr = []

@app.route(route="getQuotes")
def getQuotes(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    global hasContactedDatabase
    global quotesArr
    if not hasContactedDatabase:
      with pyodbc.connect(connection_string) as conn:
          logging.info('Contacting database')
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
          hasContactedDatabase = True
    return func.HttpResponse(json.dumps(quotesArr))
   