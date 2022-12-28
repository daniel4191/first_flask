from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')


@app.route('/thankyou')
def thank_you():
    # render_template('thanks.html')
    # 여기서의 get으로 받아오는 인자 first는 html파일에서 name으로 지정된 인자다
    # 즉, 이럴경우 name이 input태그를 통해서 전달이 될경우, 고객이 값을 입력하면
    # 해당input태그를 타고 여기로 값이 전달되게 된다.
    first = request.args.get('first')
    last = request.args.get('last')

    # 위에서 html에서 받아온 first와 last를 각각 first와 last라는 변수에 넣어주고
    # 다시금 이것을 통해서 thankyou.html에 first, last라는 인자로 전달을 한다.
    # 이렇게 함으로 인해서 for문이라든지 탬플릿 태그 사용이 가능하다
    return render_template('thankyou.html', first=first, last=last)


# 404에러 함수view + url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
