def helper_convert(obra: dict) -> dict:
    """Altera o dicionário para aspas duplas.

    :param obra: dados da obra.
    :return: dict
    """
    return {
        "id": str(obra["_id"]),
        "title": obra["title"],
        "publishing_company": obra["publishing_company"],
        "photo": obra["photo"],
        "authors": obra["authors"],
    }
