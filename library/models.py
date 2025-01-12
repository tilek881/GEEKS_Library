from django.db import models


class Books(models.Model):
    GENRE_CHOICES = (
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
        ('Научная литература', 'Научная литература'),
    )

    image = models.ImageField(upload_to='books', verbose_name="Загрузите обложку книги")
    title = models.CharField(max_length=200, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги', blank=True)
    price = models.DecimalField(verbose_name='Цена' , default=400 , decimal_places=2, max_digits=10)
    release_date = models.DateField(verbose_name='Дата выхода', null=True, blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name='Жанр книги')
    email = models.EmailField(verbose_name='Почта автора', blank=True)
    author = models.CharField(max_length=100, verbose_name='Автор книги', default='Игорь Иванов')
    trailer = models.URLField(verbose_name='Ссылка на книгу YouTube', blank=True)

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Список книг'

    def __str__(self):
        return f'{self.title} - {self.price} руб.'


class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    comment = models.TextField(verbose_name='Комментарий')
    stars = models.CharField(choices=STARS , max_length=10 , verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='Дата создания')
    book = models.ForeignKey(Books, on_delete=models.CASCADE , related_name='reviews')

    def __str__(self):
        return f'{self.book} - {self.comment}'











