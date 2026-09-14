"Is this order usable?"


def is_valid_order(order):
    "True if the order passes every rule."

    # Check 1: distance must be greater than 0
    if order["distance_km"] <= 0:
        return False

    # Check 2: preparation time must be greater than 0
    if order["prep_time_min"] <= 0:
        return False

    # Check 3: traffic level must be between 1 and 5
    if order["traffic_level"] < 1 or order["traffic_level"] > 5:
        return False

    # Check 4: rain must be either 0 or 1
    if order["rain"] not in [0, 1]:
        return False

    return True
