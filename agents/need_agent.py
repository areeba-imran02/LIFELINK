import re
from core.models import Need

CATEGORY_RULES = {
    "transport": ["transport", "ride", "vehicle", "pickup", "wheelchair", "mobility"],
    "business_supply": ["boxes", "packaging", "supplier", "bulk", "business", "custom"],
    "repair": ["repair", "fix", "laptop", "phone", "device", "technician"],
    "venue": ["venue", "hall", "event", "meeting", "accessible space"],
    "home_service": ["home", "cleaning", "plumber", "electrician", "installation"],
}

def analyze(request, city, country, budget=None, urgency="Normal"):
    text = request.lower()
    scores = {k: sum(word in text for word in words) for k, words in CATEGORY_RULES.items()}
    category = max(scores, key=scores.get) if max(scores.values()) else "general"

    constraints = []
    for phrase in ["wheelchair", "accessible", "elderly", "home collection", "pickup", "urgent", "tomorrow", "3 days"]:
        if phrase in text:
            constraints.append(phrase)

    keywords = [w for w in re.findall(r"[a-zA-Z]{4,}", text) if w not in {"need", "with", "that", "from", "this"}][:12]
    summary = request.strip()
    return Need(
        raw_request=request,
        category=category,
        summary=summary,
        location=f"{city}, {country}",
        urgency=urgency,
        budget=budget,
        constraints=constraints,
        keywords=keywords,
    )
