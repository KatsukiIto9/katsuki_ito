total_pages = int(input("本の総ページ数を入力してください: "))

break_page = int(input("休憩するページ数を入力してください: "))

print("読書を開始します")


for p in range(1, total_pages + 1):
    
    print(f"{p} ページ目を読みました")

    
    if p == break_page:
        print("休憩します。")
        break