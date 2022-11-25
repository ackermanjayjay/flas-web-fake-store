from flask import *

import requests as req
app=Flask(__name__)



@app.route('/')
def index():
    crawl_text=req.get("https://fakestoreapi.com/products")
    data_crawl=crawl_text.json()
    keterangan_data=data_crawl
  
    return render_template('index.html',datas=keterangan_data)

@app.route('/data')
def ambil_data():
    crawl_text=req.get("https://fakestoreapi.com/products")
    data_crawl=crawl_text.json()
    keterangan_data=data_crawl
  
    return render_template('data.html',datas=keterangan_data)
    

if __name__=='__main__':
  
    app.run(debug = True)