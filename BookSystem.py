from flask import Flask
from flask import render_template, request
from Scripts import Configure
from Scripts.Models import BookModel
from Scripts.Forms import BookSystemForms

BookSystem = Flask(__name__, template_folder='Statics/', static_folder='Statics/')
BookSystem.config.from_object(Configure)
BookSystemForms.init_app(BookSystem)
BookSystemForms.drop_all(app=BookSystem)
BookSystemForms.create_all(app=BookSystem)


@BookSystem.route('/')
@BookSystem.route('/Books')
def Index():
    return render_template('Index/Index.html', Books=BookModel.query.all())


@BookSystem.route('/Book/Construction', methods=('POST', 'GET'))
def Construction():
    if request.method == 'GET':
        return render_template('Book/Construction/Construction.html')
    ConstructionJson = request.json
    if BookModel.query.filter_by(Code=ConstructionJson['Code']):
        Book = BookModel.Create(ConstructionJson)
        BookSystemForms.session.add(Book)
        BookSystemForms.session.commit()
        return 'Success'
    return '书本代码已存在，请重新检查输入！'


if __name__ == '__main__':
    BookSystem.run()
