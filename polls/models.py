from django.db import models

# Create your models here.


class Question(models.Model):
    """
    A class representing a question.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date when the question was published.

    Methods:
        __str__(): Returns the string representation of the question.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    A class representing a choice for a question.

    Attributes:
        question (Question): The question to which this choice belongs.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received for this choice.

    Methods:
        __str__(): Returns the string representation of the choice.

    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
