def calculate_price(base_price, freshness):
    # Logic: Fresh = full price, Ripe = 10% off, Rotten = 40% off
    if freshness == "Fresh":
        discount = 0
    elif freshness == "Ripe":
        discount = 10
    else:
        discount = 40
    
    final_price = base_price * (1 - discount/100)
    return final_price, discount

def profit_loss(cost_price, selling_price):
    return selling_price - cost_price

# --- NEW FEATURE: SHELF LIFE PREDICTION ---
def predict_shelf_life(freshness, item_type="General"):
    """
    Predicts remaining days based on the AI's freshness detection.
    """
    if freshness == "Fresh":
        return "7-10 Days"
    elif freshness == "Ripe":
        return "2-3 Days"
    elif freshness == "Rotten":
        return "0 Days (Expired)"
    else:
        return "Unknown"