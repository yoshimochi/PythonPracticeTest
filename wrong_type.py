# 型ヒント
# 可読性の向上やIDEを使用した開発の効率を上げる補助的役割
# 型ヒントがあっても型チェックは行われない
message: str = 12345
print(f"{message}")


# 　関数の引数や戻り値への型付け
def five_years_later(age: int) -> int:
    return age + 5


def five_years_later_students(age: int = 7) -> int:
    return age + 5


def say_hello(name: str) -> None:
    print(f"こんにちは {name} さん")


# コンテナの型付け
# リストや辞書の各要素に対しても型ヒントを設定できる
# タプルについては全ての要素に型ヒントを設定する必要がある
hobby: list = ["ゲーム", "漫画"]
favorite: dict[str, str] = {"study": "プログラミング"}

# 複数の型を許可する型 - Union・Optional
from typing import Union


# Unionは複数の方を指定できる
def address_code(number: Union[int, str]) -> int:
    pass


your_code: int = address_code(1000001)
my_code: str = address_code('100111')

from typing import Optional

# Optionalは指定した型とNoneを許可する
price: Optional[int]

# Python3.10からはUnionとOptionalが簡素に記述できるように
from __future__ import annotations


def address_code(number: int | str) -> int:
    pass


price: int | None

# 特定の型のみを許可する型 - Literal
from typing import Literal

FILETYPE = Literal['csv', 'json', 'xml']


def access_file(file: str, file_type: FILETYPE):
    pass


access_file('wheather.csv', 'csv')
access_file('wheather.html', 'html')

"""
mypy：静的型チェックツール

'mypy ファイル名'でチェックを実行できる
'mypy.ini'ファイルを作成し、オプションを指定することができる
"""
