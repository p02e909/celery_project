import sqlalchemy as db

from . import my_exception
from . import celery
from . import my_config


# Some examples of connecting to various databases can be found here:
# https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql
# Image we have sqlite database name rectangle, table rectangle

DB_PATH = my_config.DB_PATH


def calcular_rectangle(a, b):
    if a > 0 and b > 0:
        perimeter = 2 * (a + b)
        area = a * b
    else:
        raise my_exception.WrongInput("a and b must be greater than 0")
    return perimeter, area


@celery.app.task
def update_db():
    engine = db.create_engine(DB_PATH)
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

                try:
                    new_perimeter, new_area = calcular_rectangle(a, b)

                    # dont update database if perimeter and area not change
                    if perimeter == new_perimeter and area == new_area:
                        pass
                    else:
                        # update database
                        query_update = db.update(rectangle).values(
                                perimeter=new_perimeter,
                                area=new_area
                        ).where(rectangle.columns.rectangle_id==rectangle_id)
                        result = connection.execute(query_update)
                except my_exception.WrongInput:
                    pass # or write log
                except Exception as e:
                    pass # or write log

    result_proxy.close()
    return True


if __name__=="__main__":
    updatd_db()

