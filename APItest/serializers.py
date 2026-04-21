from rest_framework.serializers import ModelSerializer
from .models import Author, Brand, Category, City, Country, Currency, Department, Genre, Language,\
Manufacturer, Publisher, Role, Skill, Subject, Tag, Book, Article, Employee, Product, Course

from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author 
        fields = "__all__"

    def validate_first_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Ism kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_last_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Familiya kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Brand nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 3:
            raise ValidationError("Kategoriya nomi kamida 3 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_slug(self, obj):
        if len(obj) < 2:
            raise ValidationError("Slug kamida 2 ta belgidan iborat bo'lishi kerak!")
        return obj


class CitySerializer(ModelSerializer):

    class Meta:
        model = City 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Shahar nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_population(self, obj):
        if obj < 0:
            raise ValidationError("Aholisi manfiy bo'lishi mumkin emas!")
        return obj


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Mamlakat nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_code(self, obj):
        if len(obj) != 2 and len(obj) != 3:
            raise ValidationError("Mamlakat kodi 2 yoki 3 ta harfdan iborat bo'lishi kerak!")
        return obj


class CurrencySerializer(ModelSerializer):

    class Meta:
        model = Currency 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Valyuta nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_code(self, obj):
        if len(obj) != 3:
            raise ValidationError("Valyuta kodi 3 ta harfdan iborat bo'lishi kerak!")
        return obj


class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 3:
            raise ValidationError("Bo'lim nomi kamida 3 ta harfdan iborat bo'lishi kerak!")
        return obj


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Janr nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Til nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_iso_code(self, obj):
        if len(obj) < 2:
            raise ValidationError("ISO kod kamida 2 ta belgidan iborat bo'lishi kerak!")
        return obj


class ManufacturerSerializer(ModelSerializer):

    class Meta:
        model = Manufacturer 
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Ishlab chiqaruvchi nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj


class PublisherSerializer(ModelSerializer):

    class Meta:
        model = Publisher
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Nashriyot nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_founded(self, obj):
        if obj and obj > date.today().year:
            raise ValidationError("Tashkil etilgan yil kelajakda bo'lishi mumkin emas!")
        return obj


class RoleSerializer(ModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"

    def validate_title(self, obj):
        if len(obj) < 3:
            raise ValidationError("Lavozim nomi kamida 3 ta harfdan iborat bo'lishi kerak!")
        return obj


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Ko'nikma nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj


class SubjectSerializer(ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Fan nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_code(self, obj):
        if len(obj) < 2:
            raise ValidationError("Fan kodi kamida 2 ta belgidan iborat bo'lishi kerak!")
        return obj


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Teg nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, obj):
        if len(obj) < 2:
            raise ValidationError("Kitob nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_published_year(self, obj):
        if obj > date.today().year:
            raise ValidationError("Nashr yili kelajakda bo'lishi mumkin emas!")
        return obj


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, obj):
        if len(obj) < 5:
            raise ValidationError("Maqola sarlavhasi kamida 5 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_body(self, obj):
        if len(obj) < 20:
            raise ValidationError("Maqola matni kamida 20 ta harfdan iborat bo'lishi kerak!")
        return obj


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_first_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Ism kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_last_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Familiya kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_hired_on(self, obj):
        if obj > date.today():
            raise ValidationError("Ishga qabul qilingan sana kelajakda bo'lishi mumkin emas!")
        return obj


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

    def validate_name(self, obj):
        if len(obj) < 2:
            raise ValidationError("Mahsulot nomi kamida 2 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_price(self, obj):
        if obj <= 0:
            raise ValidationError("Narx 0 dan katta bo'lishi kerak!")
        return obj


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def validate_title(self, obj):
        if len(obj) < 3:
            raise ValidationError("Kurs nomi kamida 3 ta harfdan iborat bo'lishi kerak!")
        return obj
    
    def validate_credits(self, obj):
        if obj < 1:
            raise ValidationError("Kredit kamida 1 bo'lishi kerak!")
        return obj