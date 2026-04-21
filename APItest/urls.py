from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    AuthorViewSet, BrandViewSet, CategoryViewSet, CityViewSet, CountryViewSet,
    CurrencyViewSet, DepartmentViewSet, GenreViewSet, LanguageViewSet,
    ManufacturerViewSet, PublisherViewSet, RoleViewSet, SkillViewSet,
    SubjectViewSet, TagViewSet, BookViewSet, ArticleViewSet, EmployeeViewSet,
    ProductViewSet, CourseViewSet,
)



r = DefaultRouter()
r.register(r"author", AuthorViewSet, basename="author")
r.register(r"brand", BrandViewSet, basename="brand")
r.register(r"category", CategoryViewSet, basename="category")
r.register(r"city", CityViewSet, basename="city")
r.register(r"country", CountryViewSet, basename="country")
r.register(r"currency", CurrencyViewSet, basename="currency")
r.register(r"department", DepartmentViewSet, basename="department")
r.register(r"genre", GenreViewSet, basename="genre")
r.register(r"language", LanguageViewSet, basename="language")
r.register(r"manufacturer", ManufacturerViewSet, basename="manufacturer")
r.register(r"publisher", PublisherViewSet, basename="publisher")
r.register(r"role", RoleViewSet, basename="role")
r.register(r"skill", SkillViewSet, basename="skill")
r.register(r"subject", SubjectViewSet, basename="subject")
r.register(r"tag", TagViewSet, basename="tag")
r.register(r"book", BookViewSet, basename="book")
r.register(r"article", ArticleViewSet, basename="article")
r.register(r"employee", EmployeeViewSet, basename="employee")
r.register(r"product", ProductViewSet, basename="product")
r.register(r"course", CourseViewSet, basename="course")



urlpatterns = [
    path('', include(r.urls)),
]
