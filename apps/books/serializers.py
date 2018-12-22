from rest_framework import serializers
from .models import BookCategory, BookAuthor, Books, BookDetail, PublishInformation


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = "__all__"


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = "__all__"


class PublishInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishInformation
        fields = "__all__"
