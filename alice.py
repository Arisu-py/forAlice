from flask import Flask, request, jsonify , url_for
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

sessionStorage = {}


@app.route('/')
def f():
    return "<title>hello</title><h1>Миссия Колонизация Марса<h1>"


@app.route('/index')
def my_func():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def motto():
    return '''Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!'''


@app.route('/image_mars')
def image():
    return f'''<title>Привет, Марс!</title><h1>Жди нас, Марс!</h1><img src="{url_for('static', filename='img/mars.jpeg')}"
           alt="здесь должна была быть картинка, но не нашлась"><br>Вот она какая, красная планета.'''


@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}"
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="text-center">Анкета претендента</h1>
                            <h2 class="text-center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="name">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password"><br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <label>Какие у вас есть профессии?</label>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="injenerissl" name="accept">
                                        <label class="form-check-label" for="injenerissl">Инженер-исследователь</label><br>
                                        <input type="checkbox" class="form-check-input" id="injenerstr" name="accept">
                                        <label class="form-check-label" for="injenerstr">Инженер-строитель</label><br>
                                        <input type="checkbox" class="form-check-input" id="pilot" name="accept">
                                        <label class="form-check-label" for="pilot">Пилот</label><br>
                                        <input type="checkbox" class="form-check-input" id="met" name="accept">
                                        <label class="form-check-label" for="met">Метеоролог</label><br>
                                        <input type="checkbox" class="form-check-input" id="dok" name="accept">
                                        <label class="form-check-label" for="dok">Врач</label>
                                    </div>
                                    <label>Укажите пол</label>
                                    <div class="form-group">
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <h3>Эта планета близка к Земле;</h3>
                        <div class="alert alert-primary" role="alert">
                          <h4>На ней много необходимых ресурсов;</h4></div>
                        <div class="alert alert-primary" role="alert">
                          <h4>На ней есть вода и атмосфера;</h4></div>
                        <div class="alert alert-primary" role="alert">
                          <h4>На ней есть небольшое магнитное поле;</h4></div>
                        <div class="alert alert-primary" role="alert">
                          <h4>Наконец, она просто красива!</h4></div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h4>Претендента на участие в миссии {nickname}:</h4>
                            <div class="alert alert-primary" role="alert">
                              <h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4></div>
                            <h4>составляет {rating}!</h4>
                            <div class="alert alert-primary" role="alert">
                              <h3>Желаем удачи!</h3></div>
                          </body>
                        </html>'''


@app.route('/post', methods=['GET', 'POST'])
def alice_main():
    print(2)
    if request.method == 'GET':
        return "post"
    print(3)
    logging.info(f'Request: {request.json!r}')

    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    print(1)
    handle_dialog(request.json, response)

    logging.info(f'Response:  {response!r}')
    return jsonify(response)


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        sessionStorage[user_id] = {
            'suggests': [
                "Не хочу.",
                "Не буду.",
                "Отстань!",
            ]
        }
        res['response']['text'] = f'Привет! Купи слона!'
        res['response']['buttons'] = get_suggests(user_id)
        return

    if req['request']['original_utterance'].lower() in [
        'ладно',
        'куплю',
        'покупаю',
        'хорошо'
    ]:
        res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
        res['response']['end_session'] = True
        return

    res['response']['text'] = \
        f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
    res['response']['buttons'] = get_suggests(user_id)


def get_suggests(user_id):
    session = sessionStorage[user_id]

    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=слон",
            "hide": True
        })

    return suggests


if __name__ == '__main__':
    app.run()