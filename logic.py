def predict_shelf_life(item_name, freshness_status):
    # Standard shelf-life rules based on the video's example
    rules = {
        "apple": {"Fresh": "10-15 Days", "Rotten": "0 Days (Expired)"},
        "orange": {"Fresh": "12-18 Days", "Rotten": "0 Days (Expired)"},
        "tomato": {"Fresh": "7-10 Days", "Rotten": "0 Days (Expired)"}
    }
    
    # Get specific rule or provide a default
    item_rules = rules.get(item_name.lower(), {"Fresh": "5-7 Days", "Rotten": "0 Days"})
    return item_rules.get(freshness_status, "Unknown")