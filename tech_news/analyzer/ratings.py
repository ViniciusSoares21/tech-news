from tech_news.database import get_collection


# Requisito 10 Vj
def top_5_categories():
    result = (
        get_collection()
        .find(
            {},
            {"_id": False, "category": True},
        )
        .sort("category", 1)
    )

    categories_qty = {}
    for item in result:
        if item["category"] in categories_qty:
            categories_qty[item["category"]] += 1
        else:
            categories_qty[item["category"]] = 1
    return sorted(categories_qty, key=categories_qty.get, reverse=True)[:5]
