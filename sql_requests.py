def getScore(username):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT score FROM [dbo].[Users] WHERE username = '"+username+"';")
    rows = result.fetchall()
    return rows

def getPW(username):
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 18 for SQL Server};Server=tcp:boschhackathon.database.windows.net,1433;Database=HyperMilingDB;Uid=bosch-hackathon;Pwd={aEVcmVBt2mfvRLZKh3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    with engine.connect() as connection:
    result = connection.execute("SELECT password FROM [dbo].[Users] WHERE username = '"+username+"';")
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
