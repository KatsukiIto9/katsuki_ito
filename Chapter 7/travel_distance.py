def calculate_total_distance(distances):
    total_distance = sum(distances)
    return total_distance

distances = [100, 200, 500]

total_distance = calculate_total_distance(distances)

print(f"総距離: {total_distance} km")