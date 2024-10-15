# コレクションに関するクイズプログラム

def quiz():
    score = 0
    total_questions = 20

    questions = [
        ("問題1: Pythonのリストはどのような特性を持っていますか？\n a) 順序付きで、変更可能\n b) 順序なしで、変更可能\n c) 順序付きで、変更不可能\n", 'a'),
        ("問題2: Pythonのセットの特性は何ですか？\n a) 順序付きで、重複を許可\n b) 順序なしで、重複を許可しない\n c) 順序付きで、重複を許可しない\n", 'b'),
        ("問題3: 辞書のキーの特性は何ですか？\n a) 重複を許可\n b) 一意でなければならない\n c) 任意のデータ型を使用できる\n", 'b'),
        ("問題4: リストに要素を追加するためのメソッドはどれですか？\n a) append()\n b) add()\n c) insert()\n", 'a'),
        ("問題5: セットに要素を追加するためのメソッドはどれですか？\n a) append()\n b) add()\n c) insert()\n", 'b'),
        ("問題6: 辞書から値を取得するために使うメソッドはどれですか？\n a) get()\n b) retrieve()\n c) fetch()\n", 'a'),
        ("問題7: リストはどのように作成しますか？\n a) []\n b) {}\n c) ()\n", 'a'),
        ("問題8: セットはどのように作成しますか？\n a) []\n b) {}\n c) set()\n", 'c'),
        ("問題9: 辞書の構文はどのようになりますか？\n a) [key: value]\n b) {key: value}\n c) (key, value)\n", 'b'),
        ("問題10: リストの長さを取得するにはどのメソッドを使いますか？\n a) size()\n b) count()\n c) len()\n", 'c'),
        ("問題11: セットの要素を削除するためのメソッドはどれですか？\n a) remove()\n b) discard()\n c) both a and b\n", 'c'),
        ("問題12: 辞書内のすべての値を取得するにはどのメソッドを使いますか？\n a) values()\n b) get_values()\n c) all_values()\n", 'a'),
        ("問題13: リストの特性は何ですか？\n a) 重複を許可\n b) 一意でなければならない\n c) 順序なし\n", 'a'),
        ("問題14: セットの長さを取得するにはどのメソッドを使いますか？\n a) len()\n b) size()\n c) count()\n", 'a'),
        ("問題15: 辞書に新しいキーと値を追加するにはどうしますか？\n a) dict.add()\n b) dict[key] = value\n c) dict.append()\n", 'b'),
        ("問題16: リストを逆順にするにはどのメソッドを使用しますか？\n a) reverse()\n b) flip()\n c) back()\n", 'a'),
        ("問題17: セットの要素の共通部分を取得するために使うメソッドはどれですか？\n a) intersection()\n b) union()\n c) difference()\n", 'a'),
        ("問題18: リストをソートするにはどのメソッドを使いますか？\n a) order()\n b) sort()\n c) arrange()\n", 'b'),
        ("問題19: 辞書の全てのキーを取得するにはどのメソッドを使いますか？\n a) keys()\n b) get_keys()\n c) all_keys()\n", 'a'),
        ("問題20: セットの要素をランダムに取得するにはどのメソッドを使いますか？\n a) random()\n b) sample()\n c) choice()\n", 'b'),
    ]

    print("コレクションに関するクイズへようこそ！")

    for question, answer in questions:
        user_answer = input(question)
        if user_answer.lower() == answer:
            print("正解です！")
            score += 1
        else:
            print(f"残念！正解は {answer} です。")

    # 結果表示
    print(f"\nあなたのスコアは {score} / {total_questions} です。")

# クイズを開始
quiz()
