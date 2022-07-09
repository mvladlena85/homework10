import json


def load_candidates(path: str):  # , которая загрузит данные из файла
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data


def get_all(candidates: list):  # которая покажет всех кандидатов
    candidate_data = ""
    for candidate in candidates:
        candidate_data += f'Имя кандидата - {candidate["name"]}\n' \
                          f'Позиция кандидата - {candidate["position"]}\n' \
                          f'Навыки - {candidate["skills"]}\n\n'
    return candidate_data


def get_by_pk(candidates: list, pk: int):  # которая вернет кандидата по pk
    for candidate in candidates:
        if candidate["pk"] == pk:
            return candidate["picture"], f'Имя кандидата - {candidate["name"]}\n' \
                    f'Позиция кандидата - {candidate["position"]}\n' \
                    f'Навыки - {candidate["skills"]}\n'
    return "Неверно указан pk"


def get_by_skill(candidates: list, skill_name: str):  # , которая вернет кандидатов по навыку
    candidate_data = ""
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            candidate_data += f'Имя кандидата - {candidate["name"]}\n' \
                              f'Позиция кандидата - {candidate["position"]}\n' \
                              f'Навыки - {candidate["skills"]}\n\n'
    return candidate_data


