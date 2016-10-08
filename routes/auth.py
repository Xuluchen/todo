from models.user import User
from routes import *


main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        return User.query.get(int(uid))
    else:
        # 匿名用户
        # return User.niming()
        return None


@main.route('/')
def index():
    # sid = session.get('user_id', '不存在')
    # print('sid', sid)
    u = current_user()
    return render_template('login.html', sid=u)



@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    # 此处应有合法性验证
    u.save()
    return redirect(url_for('.index'))


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u1 = User(form)
    u2 = User.query.filter_by(username=u1.username).first()
    if u1.validate_login(u2):
        print('login success')
        # 登录成功后, 写入 session 中
        session['user_id'] = u2.id
    else:
        print('login failed')
    return redirect(url_for('.index'))
