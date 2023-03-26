from flask import Flask, url_for, request, redirect, render_template

from flask_sqlalchemy import SQLAlchemy

import json
from flask_bootstrap import Bootstrap5
from sqlalchemy.sql import func


app = Flask(__name__)
bootstrap = Bootstrap5(app)


# 设置数据库连接地址
DB_URI = 'mysql+pymysql://root:50803019@127.0.0.1:3306/forum'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# 是否追踪数据库修改，一般不开启, 会影响性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 是否显示底层执行的SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 开启热部署
app.config['DEBUG'] = True

# 创建数据库连接引擎
db = SQLAlchemy(app)

@app.route('/index')
def index():
    rows = Post.query.all()

    # 要把所有的数据转换Json形式
    data = []
    for row in rows:
        data.append(row) 

    # 做一个Json转换
    #print(data)
    return render_template("main.html", data=data)
    # return json.dumps(rows)

@app.route('/test')
def test():
    return json.dumps([1,2,3])

#ORM 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    sectionId = db.Column(db.Integer, nullable=False) # 游戏分区 1 原神区
    type = db.Column(db.Integer,nullable=False) # 帖子的类型，普通帖子，加精 1
    updateTime = db.Column(db.DateTime(timezone=False),
                           server_default=func.now())
    createTime = db.Column(db.DateTime(timezone=False),
                           server_default=func.now())
    poster = db.Column(db.Integer, nullable=False) # 1
    
    # debug用的
    def __repr__(self):
        return f'<Post {self.title}>'

@app.route('/post', methods=['POST'])
def post():
    if request.method=='POST':
        data = request.get_json()
        title = data['title']
        content = data['content']
        print(data)

   
    # # 要把所有的数据转换Json形式
    # data = []
    # for row in rows:
    #     data.append([x for x in row]) 

    # # 做一个Json转换
    # print(data)
    return render_template("main.html", data=[1,2,3])
    # return json.dumps(data)

# if __name__ == '__main__':
#     app.run(port=8000, debug=True)
   
   
