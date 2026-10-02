def check(resource):
    if resource.verified:
        return "Provider/resource is marked verified in the demo registry."
    return "Verification is not established. Do not treat this resource as independently verified."
