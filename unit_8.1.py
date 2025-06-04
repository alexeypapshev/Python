# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Привет, мир!'

# if __name__ == '__main__':
#     app.run(debug=True)


#############################################


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f'Привет, {name}!'
    return '''
        <form method="POST">
            Имя: <input type="text" name="name">
            <input type="submit" value="Отправить">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
