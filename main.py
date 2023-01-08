"""
**Задача 1 - две случайные части**

Создайте приложение из двух частей `bp_numeric` и `letteric`

- [ ]  `/bp_numeric/random` возврашает случайное число от `1 до 10`
- [ ]  `/letteric/random` возвращает случайную букву от `a до z`
"""



from flask import Flask, render_template
from bp_leteric.leteric import leteric
from bp_numeric.numeric import numeric


app = Flask(__name__)

app.register_blueprint(leteric, url_prefix='/leteric')
app.register_blueprint(numeric, url_prefix='/numeric')




if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


