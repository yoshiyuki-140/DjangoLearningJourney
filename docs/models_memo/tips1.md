# Django ORM の学習メモ

## primary_keyの指定

- Djangoで1つのmodelクラスには1つしかprimary_keyを持つカラムがあってはならない.
    -> 複合主キーの禁止

## Metaオプション
- モデルのテーブル名は、Djangoアプリケーション名とクラス名をアンダースコアでつないだ物が使用される.
- モデル名のカスタマイズをしたかったらMetaインナークラスのdb_tableフィールドに指定したい名前を文字列型で与えればいい.
    Snippetsクラスを"snippets"という名前にしたい場合は
    ```python
    class Snippets(model.Model):
        class Meta:
            db_table="snippets"
    ```
    意図した型名として扱われるか心配な場合は
    ```powershell
    $ python manage.py sqlmigrate
    ```
    を実行する.




