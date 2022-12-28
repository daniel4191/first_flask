from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():

    # 여기 나오는 조건 문에 대한 작성을 하지 못했었다.
    lower_letter = False
    upper_letter = False
    num_end = False

    # 인자로 들어가는 username은 html파일의 name에서 비롯되었다.
    username = request.args.get('username')

    # *매우중요 "문장에 c가 소문자로 들어가는지 안들어가는지 확인하는 반복문"
    lower_letter = any(c.islower() for c in username)

    # *매우중요 "문장에 c가 대문자로 들어가는지 안들어가는지 확인하는 반복문"
    upper_letter = any(c.isupper() for c in username)

    # *매우중요 "문장의 마지막이 숫자로 끝나는지 아닌지 판별해주는 것"
    num_end = username[-1].isdigit()

    # 이건 report에 하나의 AND 조건으로 True or False를 리턴하는 것이다.
    report = lower_letter and upper_letter and num_end

    return render_template('report.html', report=report, lower=lower_letter,
                           upper=upper_letter, num_end=num_end)


if __name__ == '__main__':
    app.run(debug=True)
