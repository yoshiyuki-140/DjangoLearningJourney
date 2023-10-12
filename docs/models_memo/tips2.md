# モデル定義に関するメモ

> マイグレーションファイルから生成されるSQLを見るときは
> ```
> $ python manage.py <app_label(アプリ名)> <migration_name(マイグレーションファイルの数字)>
> ```

## 主なモデルフィールドを使用する時に気を付けるべきこと

- CharFiled(文字列が入る)
    - **文字数制限をかけないといけない**
    ```python
    # 例
    max_length=255
    ```

- TextField(改行ありの文章が入る)
    - **文字数制限をかけなくてもよい**(かけることはできる)

- ImageField(DBには写真のパスが入るが、写真オブジェクトとして扱うことができる)
    - **"upload_to"を指定しないといけない**
    ```
    upload_to="image"
    ```

    これを実行すると
    PROJECT_ROOT/media/image
    の中にアップロード写真が入る
    > jpg形式にしか対応していない -> Pillowモジュールを使うとpngが使えるようになる

- FileField
    - **"upload_to"を指定しないといけない**
    - ImageFieldとほぼ同じ

- IntegerField
    > **フィールド引数で下限や上限を決めることができる**
    > SmallIntegerField ,BigIntegerFieldというのもある
    - 2147483648 ~ -2147483647の数が入る

- BooleanField
    - TrueかFalseが入る

- DateField,DateTimeField
    - pythonのDate型として扱える.

- ForeignKey
    - **on_delete引数を指定しないといけない**
    - on_deleteに入る値に関して
        - on_delete=models.CASCADE
            -> 該当のテーブルは共に消される
        - on_delete=models.PROTECT
            -> 該当のテーブルは削除されなくなる

- ManyToManyField
    - **on_deleteは必要ない**

- OneToOneField
    - **複数紐づけをしようとするとエラーになる**
