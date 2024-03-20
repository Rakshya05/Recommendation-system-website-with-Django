def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def calculate_similarity(organization, products):
    organization_set = set(organization)
    max_match_count = 0
    similarities = []
    for product in products:
        product_set = set(product)
        match_count = len(organization_set.intersection(product_set))
        max_match_count = max(max_match_count, match_count)
        union_size = len(organization_set.union(product_set))
        similarity = jaccard_similarity(organization_set, product_set)
        similarities.append(similarity)
    return similarities

# Example data
organization = ["woman", "old"]
products = [
    ["woman", "old", "child", "woman"],
    ["woman", "child", "old"],
    ["child"]
]

similarities = calculate_similarity(organization, products)
print("Similarities:", similarities)
