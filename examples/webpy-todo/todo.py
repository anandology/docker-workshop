import web
import os

urls = (
    "/", "index",
)
app = web.application(urls, globals())

db_url = os.getenv("DATABASE_URL")
db = web.database(db_url)

def get_todos():
    return db.select("todo", order="id")

class index:
    def GET(self):
        todos = get_todos()
        return render.index(todos)


if __name__ == "__main__":
    app.run()
