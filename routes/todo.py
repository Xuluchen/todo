from models.todo import Todo
from routes import *


main = Blueprint('todo', __name__)


@main.route('/')
def index():
    ts = Todo.query.all()
    return render_template('todo_index.html', todo_list=ts)



@main.route('/edit/<id>')
def edit(id):
    t = Todo.query.filter_by(id=id).first()
    return render_template('todo_edit.html', todo=t)


@main.route('/add', methods=['POST'])
def add():
    # task=read%20a%20book
    # flask 自动转换格式的依据是 Content-Type 头
    # application/x-www-form-urlencoded
    # {
    #     'task': 'read a book'
    # }
    form = request.form
    t = Todo(form)
    t.save()
    # Todo.new(request.form)
    # url_for函数的功能:根据函数名返回一个字符串
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    t = Todo.query.filter_by(id=id).first()
    t.update(form)
    # Todo.update(id, request.form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    t = Todo.query.filter_by(id=id).first()
    # t.user.id == u.id 使用 session 实现权限控制
    t.delete()
    # Todo.delete(id)
    return redirect(url_for('.index'))
