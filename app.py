from flask import Flask
import utils

app = Flask(__name__)

path = "candidates.json"
candidates_list = utils.load_candidates(path)


@app.route("/")
def page_index():
    return f"<pre>{utils.get_all(candidates_list)}</pre>"


@app.route("/candidates/<int:x>/")
def page_candidate(x):
    candidate_data = utils.get_by_pk(candidates_list, x)
    url = candidate_data[0]
    data = candidate_data[1]
    print(url)
    return f"<img src='{url}'>" \
           f"<pre>{data}</pre>"


@app.route("/skills/<x>")
def page_skilled_candidates(x):
    return f"<pre>{utils.get_by_skill(candidates_list, x)}</pre>"


app.run()
