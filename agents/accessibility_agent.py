def check(resource, need):
    constraints = " ".join(need.constraints).lower()
    if not any(x in constraints for x in ["wheelchair", "accessible", "elderly", "mobility"]):
        return "No special accessibility constraint detected."
    acc = " ".join(resource.accessibility).lower()
    if "wheelchair" in constraints and "wheelchair" in acc:
        return "Wheelchair support is listed in demo resource data."
    if "accessible" in constraints and "accessible" in acc:
        return "Accessibility support is listed in demo resource data."
    return "Accessibility requirement is not confirmed."
