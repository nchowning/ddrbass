from django.db import models
from django.contrib.auth.models import User


class Difficulty(models.Model):
    """Difficulty rating - Beginner, Basic, Difficult, etc..."""
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=1)

    def __unicode__(self):
        return self.name


class Style(models.Model):
    """Play style - Single, Double, etc..."""
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name


class Grade(models.Model):
    """Score grade - AAA, AA, A, etc..."""
    name = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    """Generic Song information"""
    name = models.CharField(max_length=200)
    name_translation = models.CharField(max_length=200, null=True)
    artist = models.CharField(max_length=200)
    artist_translation = models.CharField(max_length=200, null=True)
    bpm = models.IntegerField()
    bpm_max = models.IntegerField(null=True)
    genre = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        if self.name_translation:
            return '%s (%s)' % (self.name, self.name_translation)
        return self.name


class Chart(models.Model):
    """Specific chart for a song"""
    song = models.ForeignKey(Song)
    style = models.ForeignKey(Style)
    difficulty = models.ForeignKey(Difficulty)

    difficulty_rating = models.IntegerField()
    difficulty_rating_old = models.IntegerField(null=True)

    step_count = models.IntegerField()
    freeze_count = models.IntegerField(default=0)
    shock_count = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s%s' % (self.song.name, self.difficulty.code, self.style.code)  #noqa

    @property
    def marvelous_value(self):
        """
        Return the score value for a single marvelous
        """
        return 1000000.0 / (self.step_count + self.freeze_count + self.shock_count)  #noqa

    @property
    def ok_count(self):
        """
        Return the total max OK count (shocks + freezes)
        """
        return self.freeze_count + self.shock_count


class Mix(models.Model):
    """Dance Dance Revolution Mix"""
    name = models.CharField(max_length=200)
    release = models.DateTimeField()
    region = models.CharField(max_length=100, default='Japan')
    songs = models.ManyToManyField(Song)

    def __unicode__(self):
        return self.name


class Score(models.Model):
    """User score for a chart"""
    user = models.ForeignKey(User)
    chart = models.ForeignKey(Chart)
    date_entered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    comment = models.TextField(blank=True)
    picture_url = models.URLField(max_length=500, blank=True)
    video_url = models.URLField(max_length=500, blank=True)

    minimaid_pfc = models.BooleanField("Minimaid PFC", default=False)
    minimaid_score = models.BooleanField(default=False)

    passing = models.BooleanField("Pass", default=True)
    marvelous = models.IntegerField(default=0)
    perfect = models.IntegerField(default=0)
    great = models.IntegerField(default=0)
    good = models.IntegerField(default=0)
    boo = models.IntegerField(default=0)
    miss = models.IntegerField(default=0)
    ok = models.IntegerField(default=0)

    @property
    def valid(self):
        """Check the validity of this score"""
        step_count = self.marvelous + self.perfect + self.great + self.good +\
            self.boo + self.miss

        if step_count != self.chart.step_count:
            return False

        if self.ok != self.chart.ok_count:
            return False

        return True

    @property
    def machine_score(self):
        """Calculate the machine score for this score"""
        if self.marvelous:
            step_score = self.song.marvelous_value

            score = ((self.marvelous + self.ok) * step_score) +\
                (self.perfect * (step_score - 10)) +\
                (self.great * ((step_score / 2.0) - 10))

            return int(score)
        else:
            return 0
