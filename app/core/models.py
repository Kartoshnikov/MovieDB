from django.db import models


# Create your models here.


class PersonManager(models.Manager):
    def all_with_prefetch_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related(
            'directed',
            'writing_scripts',
            'role_set__movie', )


class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=120)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)

    objects = PersonManager()

    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        if self.died:
            return '{}, {} ({} - {})'.format(
                self.first_name,
                self.last_name,
                self.born,
                self.died, )
        return '{}, {} ({})'.format(
            self.first_name,
            self.last_name,
            self.born, )


class MovieManager(models.Manager):
    def all_with_related_persons(self):
        qs = self.get_queryset()
        qs = qs.select_related('director')
        qs = qs.prefetch_related('writers', 'actors')
        return qs


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G, 'G - General Audiences'),
        (RATED_PG, 'PG - Parent Guidance Suggested'),
        (RATED_R, 'R - Restricted'),
    )

    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    director = models.ForeignKey(
        to='Person',
        on_delete=models.SET_NULL,
        related_name='directed',
        null=True,
        blank=True,
    )

    writers = models.ManyToManyField(
        to='Person',
        related_name='writing_scripts',				# default 'model'_set, like movie_set
        #related_query_name='writing',				    # default 'model',     like movie
        blank=True,
    )

    actors = models.ManyToManyField(
        to='Person',
        through='Role',
        related_name='acting_in',
        blank=True,
    )

    objects = MovieManager()

    class Meta:
        ordering = ('-year', 'title')

    def __str__(self):
        return f'{self.title} ({self.year})'


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.movie_id} {self.person_id} {self.name}"

    class Meta:
        unique_together = ('movie', 'person', 'name')
