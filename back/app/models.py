from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    type = models.PositiveSmallIntegerField(default=0)  # 0=plain, 1=class, 2=instance

    def __str__(self):
        return str(self.id)


class Edge(models.Model):
    top = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')  # e.g. parent
    bot = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')  # e.g. child
    dist = models.PositiveSmallIntegerField()  # e.g. 1 in case of parent and child
    type = models.PositiveSmallIntegerField(default=0)  # 0 if dist != 1, 1=plain, 2=inherit

    def __str__(self):
        return '{top}-{bot} ({dist}) {type}'.format(
            top=self.top.id, bot=self.bot.id, dist=self.dist, type=self.type
        )


class Question(models.Model):
    node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')
    prop = models.ForeignKey('Prop', on_delete=models.CASCADE, related_name='+')


class EnteredAnswer(models.Model):
    node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')
    prop = models.ForeignKey('Prop', on_delete=models.CASCADE, related_name='+')
    value = models.CharField(max_length=120)


class ChosenAnswer(models.Model):
    node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')
    prop = models.ForeignKey('Prop', on_delete=models.CASCADE, related_name='+')
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name='+')


class Prop(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')
    type = models.PositiveSmallIntegerField(default=0)  # 0=enter, 1=choose


class Choice(models.Model):
    prop = models.ForeignKey('Prop', on_delete=models.CASCADE, related_name='+')
    value = models.CharField(max_length=120)
