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
    query = db.select([
        rectangle.columns.rectangle_id,
        rectangle.columns.a,
        rectangle.columns.b,
        rectangle.columns.perimeter,
        rectangle.columns.area
    ])
    result_proxy = connection.execute(query)
    flag = True
    while flag:
        result_list = result_proxy.fetchmany(10)
        if result_list == []:
            flag = False
        else:
            for rectangle_info in result_list:
                rectangle_id = rectangle_info[0]
                a = rectangle_info[1]
                b = rectangle_info[2]
                perimeter = rectangle_info[3]
                area = rectangle_info[4]

                # calcular perimeter and area
                if a > 0 or b > 0:
                    new_perimeter, new_area = calcular_rectangle(a, b)

                # dont update database if a <= 0 or b <= 0
                if a <= 0 or b <=0:
                    pass
                # dont update database if perimeter and area not change
                elif perimeter == new_perimeter and area == new_area:
                    pass
                else:
                    # update database
                    query_update = db.update(rectangle).values(
                            perimeter=new_perimeter,
                            area=new_area
                    ).where(rectangle.columns.rectangle_id==rectangle_id)
                    result = connection.execute(query_update)
    result_proxy.close()
    return ""


if __name__=="__main__":
    updatd_db()

