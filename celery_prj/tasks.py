import sqlalchemy as db

from . import my_exception
from . import celery
from . import my_config


# Some examples of connecting to various databases can be found here:
# https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql
# Image we have sqlite database name rectangle, table rectangle

DB_PATH = my_config.DB_PATH
ENGINE = db.create_engine(DB_PATH)
METADATA = db.MetaData()
CONNECTION = ENGINE.connect()

rectangle = db.Table('rectangle',
                     METADATA,
                     autoload=True,
                     autoload_with=ENGINE)


def calcular_rectangle(a, b):
    if a is None or b is None:
        raise my_config.WrongInput("a and b must be greater than 0")

    if a > 0 and b > 0:
        perimeter = 2 * (a + b)
        area = a * b
    else:
        raise my_exception.WrongInput("a and b must be greater than 0")
    return perimeter, area


def query_rectangle(rectangle_id):
    query = db.select([
        rectangle.columns.a,
        rectangle.columns.b,
        rectangle.columns.perimeter,
        rectangle.columns.area
    ]).where(rectangle.columns.rectangle_id == rectangle_id)

    result_query = CONNECTION.execute(query).fetchone()
    if result_query is None:
        return None

    rectangle_info = {'a': result_query[0],
                      'b': result_query[1],
                      'perimeter': result_query[2],
                      'area': result_query[3]}

    return rectangle_info


@celery.app.task
def update_db(rectangle_id):
    try:
        status = "updating"
        rectangle_info = query_rectangle(rectangle_id)
        if rectangle_info is None:
            raise my_exception.WrongInput("rectangle id not found!")

        new_perimeter, new_area = calcular_rectangle(rectangle_info['a'],
                                                     rectangle_info['b'])

        # dont update database if perimeter and area not change
        if rectangle_info['perimeter'] == new_perimeter and rectangle_info['area'] == new_area:
            status = "not update"
            pass
        else:
            # update database
            query_update = db.update(rectangle).values(
                    perimeter=new_perimeter,
                    area=new_area
            ).where(rectangle.columns.rectangle_id==rectangle_id)
            result = CONNECTION.execute(query_update)
            status = "updated"
    except my_exception.WrongInput:
        status = "failed: wrong input"
        raise my_exception.WrongInput("wrong input!")
        pass # or write log
    except Exception as e:
        status = "failed: {}".format(e)
        pass # or write log

    return status


if __name__=="__main__":
    updatd_db()

