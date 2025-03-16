from ninja import  Router, Schema
from django.db.models import Model
from django.shortcuts import get_object_or_404
import json
from .models import Book, Genre
from datetime import datetime
from .serializers import (
    BookSchema
)


router = Router()

@router.get("/books",)
def get_books(request):
    books = Book.objects.all()
    return [BookSchema.from_orm(book) for book in books]