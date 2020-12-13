from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import  UserSerializer, BoardSerializer, ListSerializer, CardSerializer
from .models import Board, List, Card
import logging

# 新規アカウント作成時用
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # AllowAny : 誰でもアクセス可能
    permission_classes = (AllowAny,)

# ログインしているユーザのプロフィールを取得する
class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class BoardViewSet(viewsets.ModelViewSet):
    # データベースに定義されている項目を全てセットする
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # 新規作成時は、usernameをログインユーザに自動的に設定する
    def perform_create(self, serializer):
        # logging.info('★★★data=' + self.request.data)
        serializer.save(owner=self.request.user)

class ListViewSet(viewsets.ModelViewSet):
    # データベースに定義されている項目を全てセットする
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # 新規作成時は、usernameをログインユーザに自動的に設定する
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CardViewSet(viewsets.ModelViewSet):
    # データベースに定義されている項目を全てセットする
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # 新規作成時は、usernameをログインユーザに自動的に設定する
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
