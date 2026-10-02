from agents.orchestrator import orchestrate

def run_lifelink(request, city, country, budget=None, urgency="Normal", language="English"):
    return orchestrate(
        request=request,
        city=city,
        country=country,
        budget=budget,
        urgency=urgency,
        language=language,
    )
