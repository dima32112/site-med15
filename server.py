from random import randint
from flask import Flask, session, redirect, url_for, request, render_template
from main_db_controll import db
def index():
   return render_template('main.html')
# f'''<a href="/test">Тест №{session['quiz']}</a>'''



def result():
   data = tuple(request.form.values())
   print(data)
   db.add_data(data)
   info = db.get_data()
   return render_template('answer.html', data=info)



# Створюємо об'єкт веб-програми:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
app.add_url_rule('/result', 'result', result, methods=['POST']) # створює правило для URL '/test'

if __name__ == '__main__':
   # Запускаємо веб-сервер:
   app.run(debug=True)
