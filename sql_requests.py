import azure.functions as func
import logging
import sqlalchemy

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

def getScore(username):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT score FROM [dbo].[Users] WHERE username = '"+username+"';")
    rows = result.fetchall()
    return rows

def pushScore(username, newScore):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("UPDATE [dbo].[Users] SET score = "+newScore+" WHERE username = '"+username+"';")
    rows = result.fetchall()
    return rows

def register(username, password):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("INSERT INTO [dbo].[Users] (username, password, score) VALUES ('"+username+"', '"+password+"', 0);")
    rows = result.fetchall()
    return rows

def verifypw(username, password):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT password FROM [dbo].[Users] WHERE username = '"+username+"';")
    rows = result.fetchall()
    if rows == password:
        return 1
    else:
        return 0

def getDashboard():
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT username, score FROM [dbo].[Users];")
    rows = result.fetchall()
    return rows

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    score = getScore(Mustermann)

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             score
             status_code=200
        )
