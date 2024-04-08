

from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {'id':1,'title':"Book 1","author":"author 1"},
    {'id':2,'title':"Book 2","author":"author 2"},
    {'id':3,'title':"Book 3","author":"author 3"},
    {'id':4,'title':"Book 4","author":"author 4"},
    {'id':5,'title':"Book 5","author":"author 5"},
]


@app.route('/',methods=['GET'])
def home_page():
    return 'Home page'

# route to get all books
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

# route to get books by id
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
     for book in books:
        if book['id'] == book_id:
            return jsonify(book)
     return jsonify({"eror":"book not found"})

@app.route('/books',methods=['POST'])
# route to add new book
def add_book():
    new_book = {
        "id":request.json['id'],
        "title":request.json['title'],
        "author":request.json['author'],
    }
    books.append(new_book)
    return jsonify({'message':'book added succesfully'})

# route to update existing gbook
@app.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return jsonify({'message':'book updated  succefully'})
    return jsonify({'message':'book not found'})

# route to delte book
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message':'book deleted successfully'})
    return jsonify({'message':'book not found'})

if __name__ =="__main__":
    app.run(debug=True)
