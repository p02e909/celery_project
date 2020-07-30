import sqlalchemy as db
from .celery import app

# Some examples of connecting to various databases can be found here:
# https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql
# Image we have sqlite database name rectangle, table rectangle


def calcular_rectangle(a, b):
    perimeter = 100000 * (a + b)
    area = a * b
    return perimeter, area


@app.task
def update_db():
    engine = db.create_engine('sqlite:///rectangle.db')
    metadata = db.MetaData()
    connection = engine.connect()
    rectangle = db.Table('rectangle', metadata, autoload=True, autoload_with=engine)
    query = db.select([rectangle.columns.rectangle_id, rectangle.columns.a, rectangle.columns.b])
    flag = True
    result_proxy = connection.execute(query)
    while flag:
        print(flag)
        result_list = result_proxy.fetchmany(3)
        if result_list == []:
            flag = False
            print(flag)
        else:
            for item in result_list:
                rectangle_id = item[0]
                a = item[1]
                b = item[2]
        
                # calcular perimeter and area
                perimeter, area = calcular_rectangle(a, b)
        
                # update database
                query_update = db.update(rectangle).values(
                        perimeter=perimeter,
                        area=area
                ).where(rectangle.columns.rectangle_id==rectangle_id)
                result = connection.execute(query_update)
    result_proxy.close()
    return ""


if __name__=="__main__":
    updatd_db()

