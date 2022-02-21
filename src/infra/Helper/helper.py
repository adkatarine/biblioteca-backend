def helper_convert(obra: dict) -> dict:
    return {
        "id": str(obra["_id"]),
        "title": obra["title"],
        "publishing_company": obra["publishing_company"],
        "photo": obra["photo"],
        "authors": obra["authors"],
    }
