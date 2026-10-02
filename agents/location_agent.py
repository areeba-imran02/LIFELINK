def check(resource, need):
    target = need.location.split(",")[0].strip().lower()
    if resource.city.lower() == target:
        return "Local-area demo match."
    return "Different city/area; distance should be verified before fulfillment."
