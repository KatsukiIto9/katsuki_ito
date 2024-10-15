def create_profile(**kwargs):
    # プロフィールを表示
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# メインプログラム
# ユーザーにプロフィール情報を入力させる
name = input("名前を入力してください: ")
age = input("年齢を入力してください: ")
hobby = input("趣味を入力してください: ")
city = input("住んでいる都市を入力してください: ")

# 関数を呼び出してプロフィールを表示
create_profile(名前=name, 年齢=age, 趣味=hobby, 都市=city)