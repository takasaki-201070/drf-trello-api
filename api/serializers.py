from rest_framework import serializers
from .models import Board , List , Card
from django.contrib.auth.models import User

## serializers.ModelSerializerを継承して、UserSerializerを作成する
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ## jsonファイルの項目定義
        fields = ('id', 'username', 'password')
        ## オプション指定
        ## パスワードはクライアントから受け取るのみ、
        ## required　必須入力
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    ## serializers.ModelSerializerにcreateやupdateが含まれているが、
    ## カスタマイズしたい部分のみオーバライドする
    def create(self, validated_data):
        ## パスワードはハッシュ化して保存する
        user = User.objects.create_user(**validated_data)
        return user

class BoardSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=50)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'title', 'created_at', 'updated_at')

class ListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=50)
    board_title = serializers.ReadOnlyField(source='board.title', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = List
        fields = ('id', 'title', 'boardId', 'board_title' , 'index', 'created_at', 'updated_at')

class CardSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=False, allow_blank=True, max_length=50)
    list_title = serializers.ReadOnlyField(source='list.title', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'text', 'listId', 'list_title' ,'boardId', 'index', 'created_at', 'updated_at')

