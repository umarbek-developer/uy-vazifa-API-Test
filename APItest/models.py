from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return self.code


class Language(models.Model):
    name = models.CharField(max_length=50)
    iso_code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    founded = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hired_on = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    credits = models.PositiveSmallIntegerField(default=3)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.title
