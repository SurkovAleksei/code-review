import requests
from bs4 import BeautifulSoup
import sqlite3
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    cur.execute("SELECT product, cost FROM shop")
    qw = cur.fetchall()
    print(qw)
    return render_template('site.html', data=qw)


def create_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS shop')

    cur.execute('''
        CREATE TABLE shop (
            id INTEGER PRIMARY KEY,
            product VARCHAR(255),
            cost VARCHAR(255)
        )
    ''')
    conn.commit()

def add_product(cur, product, cost):
    cur.execute('''INSERT INTO shop(product, cost) VALUES(?, ?)''', (name, price))


with sqlite3.connect('sate.db', check_same_thread=False) as conn:
    cur = conn.cursor()
    create_table(cur, conn)
    header = {'User Agent':
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    for count in range(1, 6):
        url = f'https://фабрика-мяса.рф/catalog/15a9cfb3-8d4d-47b8-9823-944abb7a4f7d?page={count}'
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.text, 'lxml')
        a = soup.find_all('div', class_="product-wrapper col-sm-6 col-md-4 col-lg-6 col-xl-4")
        for card in a:
            name = card.find('div', class_="product__title").text
            price = card.find('div', class_="product__price-default").text
            add_product(cur, name, price)
            conn.commit()


if __name__ == "__main__":
    app.run(debug=True)
