from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "Daniel"
    letters = list(name)
    pup_dictionary = {'pup_name': 'Sammy'}
    # templates 폴더에 있는 html을 가져오기
    # 이렇게 templates에 내용을 보내는 것을 "Jinja 템플릿"이라고 하는 것 같다.
    # name은 바로 앞에 지정된 base.html에 변수로 보내져서 더블 컬리 브레이스로 사용 가능하다.
    # render_template에서 사용될때 첫번째 인자로 들어오는 html 파일에 뒤에 오는 변수들을 보내주는 개념
    # 이라고 생각하면 된다.
    return render_template('base.html', name=name, letters=letters,
                           pup_dictionary=pup_dictionary)


if __name__ == '__main__':
    app.run(debug=True)
