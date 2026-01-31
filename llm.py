import re

def understand_query(text):
    text = text.lower()

    category = None
    if "laptop" in text:
        category = "laptop"
    elif "phone" in text:
        category = "phone"
    elif "headphone" in text:
        category = "audio"

    budget = None
    match = re.search(r'(\d{4,6})', text)
    if match:
        budget = int(match.group(1))

    use_case = "general"
    if "programming" in text or "coding" in text:
        use_case = "programming"
    elif "gaming" in text:
        use_case = "gaming"

    return {
        "category": category,
        "budget": budget,
        "use_case": use_case
    }


def explain(product, reason):
    return f"""
Recommended because:
✔ {reason}
✔ Matches your price range
✔ Popular among similar users
"""
