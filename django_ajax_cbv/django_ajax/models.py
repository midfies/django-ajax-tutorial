"""A basic class for a posting of some kind. For example: A message, a link, a question."""
from django.db import models


class Post(models.Model):
    """A base class for all types of posts."""

    content = models.CharField(max_length=200)
