from core.registry import load_resources

def discover(need):
    resources = load_resources()
    matches = []
    for r in resources:
        score = 0
        if r.category == need.category:
            score += 45
        text = (r.name + " " + r.description + " " + " ".join(r.services)).lower()
        score += min(30, sum(k.lower() in text for k in need.keywords) * 6)
        if r.city.lower() == need.location.split(",")[0].lower():
            score += 15
        if need.country.lower() == r.country.lower():
            score += 5
        if any(c.lower() in " ".join(r.accessibility).lower() for c in need.constraints):
            score += 10
        if score >= 25:
            matches.append((r, min(99, score)))
    return sorted(matches, key=lambda x: x[1], reverse=True)[:6]
