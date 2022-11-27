from flask import Flask #pip install Flask
from flask import render_template

app = Flask(__name__)

# 使用python的裝飾器
# 根目錄
@app.route('/')
def index():
    return render_template("index.html", text="這是首頁")

@app.route('/page/Shilin')
def page_Shilin():
    return render_template("page_Shilin.html")

@app.route('/page/Beitou')
def page_Beitou():
    return render_template("page_Beitou.html")

@app.route('/page/Maokong')
def page_Maokong():
    return render_template("page_Maokong.html")



if __name__ == "__main__":
    # Flask的預設配置不允許外部訪問，若要配置在產品的伺服器中，要加上"0.0.0.0"
    # debug=True為開啟debug模式，程式碼的任何修改，儲存後會立即生效，又稱為熱部屬功能
    app.run("0.0.0.0",debug=True)