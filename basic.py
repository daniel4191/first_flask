from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000
def index():
    return "<h1>hello puppy!</h1>"


@app.route('/information')  # 127.0.0.1:5000/information
def info():
    return "<h1>puppies are cute!</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>100th letter: {}</h1>".format(name[100])


# 문제 name에 입력된 인자의 끝 값이 "y"라면 그것을 라틴 표기법에 의하여
# iful로 변경해주는 것을 만들어라.

# 내 코드
# 해결자체는 했는데, 음... 뭔가 그렇게 적합한 방법은 아닌것같다.
# 이유는 연산이 내가 원하는것보다 2회정도 더 하게 된 것같다.
@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        name = name.rstrip('y') + 'iful'

    return f"puppy name is {name}"


# 정답 코드
@app.route('/puppy_name/<name>')
def puppylatin(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    return "<h1>Your puppy latin name is: {}</h1>".format(pupname)

# 흠.. 결과적으로는 정답코드보단 내 코드가 나은 것 같다.
# 왜냐하면 정답코드는 첫번째 if문에서 만약 끝에 오는 문자가 y인 경우에 처음부터 맨끝의 바로 전까지 슬라이싱 하는데,
# 그것도 하나하나가 연산으로 알고있고, 입력값이 길어질수록 그만큼 연산이 많아지기 때문이다.


if __name__ == '__main__':
    app.run(debug=True)
