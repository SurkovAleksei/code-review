from flask import Flask, render_template
from parser import cur

app = Flask(__name__)


@app.route('/')
def index():
    cur.execute("SELECT product, cost FROM shop")
    product_from_database = cur.fetchall()
    return render_template('site.html', data=product_from_database)


if __name__ == "__main__":
    app.run(debug=True)
