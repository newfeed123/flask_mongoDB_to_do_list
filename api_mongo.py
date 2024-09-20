from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

database_name = "API"
mongodb_password = "2711Huy1"
DB_URI = "mongodb+srv://tranngochuy12ctm1:{}@cluster0.amvoe8u.mongodb.net/{}?retryWrites=true&w=majority&appName=Cluster0".format(mongodb_password, database_name)
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)

class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()

    def to_json(self):
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author,
        }
    
@app.route('/api/db_populate', methods=['POST'])
def db_populate():
    book1 = Book(book_id = 1, name = "A Game of Thrones", author = "George RR martin")
    book2 = Book(book_id = 2, name = "A Game of Thrones 2", author = "George RR martin 2")

    book1.save()
    book2.save()

@app.route('/api/books', methods=['GET', 'POST'])
def api_books():
    pass

@app.route('/api/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_book(book_id):
    pass


if __name__ == '__main__':
    app.run()