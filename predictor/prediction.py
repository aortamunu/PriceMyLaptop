# predictor/prediction.py

# Example function, you will replace this with actual prediction logic or model inference
def predict_laptop_price(brand, model, purchase_price, years_used, condition, defects):
    # You can use your trained machine learning model here, or any logic you use
    # For example, this is a mock function just for demonstration:

    depreciation_rate = 0.15  # Assume 15% depreciation for simplicity
    if brand == "Apple":
        depreciation_rate = 0.20  # Apple laptops depreciate faster, for example

    # Calculate depreciation
    depreciation_amount = purchase_price * (depreciation_rate * years_used)
    predicted_price = purchase_price - depreciation_amount

    # Further adjust based on condition or defects
    if condition == "Poor":
        predicted_price *= 0.7
    elif condition == "Fair":
        predicted_price *= 0.8
    elif defects:
        predicted_price *= 0.9

    return max(predicted_price, 0)  # Ensure price doesn't go negative
