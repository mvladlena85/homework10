from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страница. Отображается список всех кандидатов и их навыки."""
    data = utils.get_all()
    return utils.format_data(data)


@app.route("/candidates/<int:x>/")
def page_candidate(x):
    """Страница отображения кандидата по его Id"""
    candidate_data = utils.get_by_pk(x)
    url = candidate_data['picture']
    data = utils.format_data([candidate_data])
    return f'''<img src='{url}'>'
                {data}'''


@app.route("/skills/<x>")
def page_skilled_candidates(x):
    """Страница поиска кандидата по навыку"""
    candidates = utils.get_by_skill(x)
    return utils.format_data(candidates)


# Запуск сервера
app.run()
