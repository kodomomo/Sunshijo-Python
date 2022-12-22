from uvicorn import run
from mangum import Mangum

from app import create_app
from app.util.database.mysql import create_all_table

app = create_app()
handler = Mangum(app)

if __name__ == '__main__':
    run(app)  # , host='0.0.0.0')
