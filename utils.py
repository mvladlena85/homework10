import json


def load_candidates() -> list[dict]:
    """
    Загружает данные кандидатов из candidates.json
    :return: list[dict]
            список кандидатов
    """
    with open("candidates.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data


def format_data(candidates: list) -> str:
    """
    Подготавливает данные для вставки в html код
    :param candidates: list
            список кандидатов
    :return: str
            Отформатированные данные
    """
    candidate_data = "<pre>"
    for candidate in candidates:
        candidate_data += f'Имя кандидата - {candidate["name"]}\n' \
                          f'Позиция кандидата - {candidate["position"]}\n' \
                          f'Навыки - {candidate["skills"]}\n\n'
    candidate_data += "</pre>"
    return candidate_data


def get_all() -> list[dict]:
    """
    Загружает всех кандидатов из json
    :return: list[dict]
    """
    return load_candidates()


def get_by_pk(pk: int) -> dict:
    """
    Находит кандидата по его pk
    :param pk: int
            идентификатор кандидата
    :return: dict
            данные по кандидату
    """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["pk"] == pk:
            return candidate
    return None


def get_by_skill(skill_name: str) -> list[dict]:
    """
    Находит всех кандидатов по заданному навыку
    :param skill_name: str
            навык
    :return: list[dict]
            список кандидатов
    """
    candidate_data = []
    candidates = load_candidates()
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            candidate_data.append(candidate)
    return candidate_data
