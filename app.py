from flask import Flask, request, redirect, render_template, url_for
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient

app = Flask(__name__)
uri = 'mongodb+srv://dombarnett03:3SYrz9JsbamU6txd@cluster0.zvgijzx.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(uri)
db = client.ToDoDatabase
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)



@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['priority']
        db.ToDo.insert_one({'content': content, 'priority': degree})
        return redirect(url_for('index'))

    all_todos = db.ToDo.find() # Add this line outside the if block! 
    return render_template('index.html', todos=all_todos) # add todos here! 

@app.route('/delete/<id>', methods=["POST"])
def delete(id):
    db.ToDo.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
# @app.route('/<id>/delete/')
# def delete(id):
#     db.ToDo.delete_one({"_id": ObjectId(id)})
#     return redirect(url_for('index'))
# def delete(id):
#     if request.method == 'DELETE':
#         db.ToDo.delete_one({"_id": ObjectId(id)})
#         return redirect(url_for('index'))
#     else:
#         # Handle GET request here (e.g., display a confirmation page)
#         return render_template('delete_confirmation.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)