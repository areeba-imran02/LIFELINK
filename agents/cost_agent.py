def check(resource, need):
    if need.budget is None:
        return f"Estimated cost shown by demo resource: {resource.estimated_cost}."
    digits = "".join(c for c in resource.estimated_cost if c.isdigit())
    if digits and float(digits) <= need.budget:
        return f"Demo estimate appears within the stated budget ({need.budget:g})."
    if digits:
        return f"Demo estimate may exceed the stated budget ({need.budget:g}); confirm exact quote."
    return "Price is unknown; request a quote."
