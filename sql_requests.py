def getScore(username):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT score FROM [dbo].[Users] WHERE username = "username";")
    rows = result.fetchall()

def getPW(username):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT password FROM [dbo].[Users] WHERE username = "username";")
    rows = result.fetchall()

def pushScore(username, newScore):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("UPDATE [dbo].[Users] SET score = " newScore " WHERE username = "username";")
    rows = result.fetchall()
