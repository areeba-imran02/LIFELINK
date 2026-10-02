from agents.need_agent import analyze
from agents.service_agent import discover
from agents.availability_agent import check as availability_check
from agents.location_agent import check as location_check
from agents.cost_agent import check as cost_check
from agents.accessibility_agent import check as accessibility_check
from agents.trust_agent import check as trust_check
from agents.coordination_agent import build
from agents.followup_agent import create

def orchestrate(request, city, country, budget=None, urgency="Normal", language="English"):
    events = []
    need = analyze(request, city, country, budget, urgency)
    events.append({"agent": "Need Agent", "action": "Structured the request", "output": f"Category={need.category}; urgency={need.urgency}"})

    raw_matches = discover(need)
    events.append({"agent": "Service Agent", "action": "Matched resources", "output": f"{len(raw_matches)} demo candidates found"})

    checks = []
    match_objects = []

    for resource, score in raw_matches:
        findings = [
            ("Availability Agent", availability_check(resource, need)),
            ("Location Agent", location_check(resource, need)),
            ("Cost Agent", cost_check(resource, need)),
            ("Accessibility Agent", accessibility_check(resource, need)),
            ("Trust Agent", trust_check(resource)),
        ]
        for agent, finding in findings:
            checks.append({
                "agent": agent,
                "status": "pass" if any(x in finding.lower() for x in ["available", "local-area", "within", "listed", "verified", "no special"]) else "warning",
                "finding": f"{resource.name}: {finding}",
            })

        data_status = "Demo registry data — not live availability"
        match_objects.append({
            "name": resource.name,
            "type": resource.type,
            "description": resource.description,
            "estimated_cost": resource.estimated_cost,
            "distance": "Local demo match" if resource.city.lower() == city.lower() else "Area not confirmed",
            "match_score": score,
            "data_status": data_status,
        })

    events.extend([
        {"agent": "Availability Agent", "action": "Checked availability fields", "output": "Live confirmation requires an external provider integration."},
        {"agent": "Location Agent", "action": "Checked geographic fit", "output": f"Compared candidates against {city}, {country}."},
        {"agent": "Cost Agent", "action": "Checked price constraints", "output": "Compared demo estimates where available."},
        {"agent": "Accessibility Agent", "action": "Checked accessibility requirements", "output": "Compared request constraints against resource capabilities."},
        {"agent": "Trust Agent", "action": "Checked verification metadata", "output": "Distinguished registry verification from real-world verification."},
    ])

    action_plan = build(need, match_objects, checks)
    follow_up = create(need, match_objects)
    events.append({"agent": "Coordination Agent", "action": "Built next-step plan", "output": f"{len(action_plan)} actions"})
    events.append({"agent": "Follow-up Agent", "action": "Prepared continuation", "output": follow_up})

    return {
        "need": need.model_dump(),
        "matches": match_objects,
        "checks": checks,
        "action_plan": action_plan,
        "follow_up": follow_up,
        "trace": events,
    }
