def calculate_total_duration(track_lengths):
    total_duration = sum(track_lengths)
    return total_duration

track_lengths = [3.5, 4.2, 5.0]
total_duration = calculate_total_duration(track_lengths)
print(f"総再生時間: {total_duration} 分")