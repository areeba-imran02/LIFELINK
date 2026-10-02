def build(need, matches, checks):
    steps = []
    if not matches:
        return ["Expand the provider directory or connect a live service API."]
    top = matches[0]["name"]
    steps.append(f"Review the top candidate: {top}.")
    steps.append("Confirm exact availability, service scope, timing, and pickup/delivery details.")
    steps.append("Confirm final price and cancellation/refund terms before committing.")
    if any("not confirmed" in c["finding"].lower() or "not established" in c["finding"].lower() for c in checks):
        steps.append("Complete outstanding verification checks before payment or handover.")
    steps.append("Confirm the final arrangement with the provider and keep a record of the agreed details.")
    return steps
