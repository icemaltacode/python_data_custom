def calculate_total_revenue(sales):
    total = 0

    for sale in sales:
        total += sale["quantity"] * sale["unit_price"]

    return total


def calculate_revenue_by_category(sales):
    revenue_by_category = {}

    for sale in sales:
        category = sale["category"]
        revenue = sale["quantity"] * sale["unit_price"]

        if category not in revenue_by_category:
            revenue_by_category[category] = 0

        revenue_by_category[category] += revenue

    return revenue_by_category


def find_best_selling_product(sales):
    quantities_by_product = {}

    for sale in sales:
        product = sale["product"]
        quantity = sale["quantity"]

        if product not in quantities_by_product:
            quantities_by_product[product] = 0

        quantities_by_product[product] += quantity

    best_product = max(quantities_by_product, key=quantities_by_product.get)

    return best_product, quantities_by_product[best_product]