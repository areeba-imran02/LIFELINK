def check(resource, need):
    if resource.available:
        return "Demo availability is marked available."
    return "Availability is not confirmed; contact/provider API verification is required."
