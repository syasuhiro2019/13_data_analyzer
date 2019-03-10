from calculation import calculation_total, calculation_max, calculation_min

if __name__ == '__main__':
    # ユーザーからの入力を受け取る
    input_data = input('データを入力してください(スペース区切り) > ')

    # 文字列のリストに変換
    numbers_as_srt = input_data.split(' ')

    # 整数リストに変更
    numbers = []  # 空のリストを生成

    for numbers_as_srt in numbers_as_srt:
        int_num = int(numbers_as_srt)

        numbers.append(int_num)  # numbersというリストに要素を追加

    # 各統計量を計算する(合計、平均･･･)
    total = calculation_total(numbers)
    max = calculation_max(numbers)
    min = calculation_min(numbers)
    ave = total // len(numbers)
    # ユーザーに見やすいようにフォーマットする

    # 出力する
    print(f'合計: {total}')
    print(f'最大: {max}')
    print(f'最小: {min}')
    print(f'平均: {ave}')
