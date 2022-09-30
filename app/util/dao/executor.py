from pymysql import connect


def execute_sql(sql: str):
    config = get_config()
    db = connect(host=config['host'], port=config['port'], user=config['user'], password=config['password'], database='sunshijo')
    cursor = db.cursor()

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def get_config():
    config_path = str(__file__).replace('executor.py', 'dao_config.json')
    return eval(open(config_path).read())
