def sort_books(reading_list):
    sorted_list = sorted(reading_list)
    
    for i in range(len(reading_list)):
        reading_list[i] = sorted_list[i]

reading_list = input("初期の読書リストをカンマ区切りで入力してください: ").split(',')
sort_books(reading_list)
print("並び替えた読書リスト:", reading_list)