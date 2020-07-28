import sqlalchemy as db
from .celery import app

# Some examples of connecting to various databases can be found here:
# https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql
# Image we have sqlite database name retangle, table retangle

@app.task
def calcular_retangle():
    engine = db.create_engine('sqlite:///retangle.sqlite')
    metadata = db.MetaData()
    connection = engine.connect()
    retangle = db.Table('retangle', metadata, autoload=True, autoload_with=engine)
    # query = db.select([retangle.columns.rectangle_id, retangle.columns.a, retangle.columns.b])
    query = db.select([retangle.columns.Id, retangle.columns.lenght, retangle.columns.width])
    result_proxy = connection.execute(query)
    result_list = result_proxy.fetchall()
    for item in result_list:
        rectangle_id = item[0]
        a = item[1]
        b = item[2]
        # calcular perimeter and area
        area = a * b
        perimeter = 2 * (a + b)
        # update database
        query = db.update(retangle).values(
                perimeter=perimeter,
                area=area
        )
        query = query.where(retangle.columns.Id==rectangle_id)
        # query = query.where(retangle.columns.rectangle_id==rectangle_id)
        result = connection.execute(query)
 
    return True

