from django.db import models


# Пользователи

class teacher(models.Model):
    teacherID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    usern = models.CharField(max_length=64, default='usr')
    post = models.CharField(max_length=64)

    def __str__(self):
        return self.surname

# План

class indPlan(models.Model):
    planID = models.IntegerField()
    year = models.CharField(max_length=64)
    startDate = models.DateField(auto_now=False, auto_now_add=True)
    changeDate = models.DateField(auto_now=True, auto_now_add=False)
    approval = models.FloatField()
    teacherID = models.ForeignKey(
        'teacher',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.planID)+'_'+self.year+'_'+str(self.teacherID)

# Осень

class plansFall(models.Model):
    num_p = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    discipline = models.CharField(max_length=256)
    workType = models.CharField(max_length=64)
    september = models.FloatField()
    october = models.FloatField()
    november = models.FloatField()
    december = models.FloatField()
    januar = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Plan_"+str(self.planID)+"_"+self.num_p

# Осень почасовая

class plansFallHourly(models.Model):
    num_p = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    discipline = models.CharField(max_length=256)
    workType = models.CharField(max_length=64)
    september = models.FloatField()
    october = models.FloatField()
    november = models.FloatField()
    december = models.FloatField()
    januar = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Весна

class plansSpring(models.Model):
    num_p = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    discipline = models.CharField(max_length=256)
    workType = models.CharField(max_length=64)
    february = models.FloatField()
    march = models.FloatField()
    april = models.FloatField()
    may = models.FloatField()
    june = models.FloatField()
    july = models.FloatField()
    august = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Весна почасовая

class plansSpringHourly(models.Model):
    num_p = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    discipline = models.CharField(max_length=256)
    workType = models.CharField(max_length=64)
    february = models.FloatField()
    march = models.FloatField()
    april = models.FloatField()
    may = models.FloatField()
    june = models.FloatField()
    july = models.FloatField()
    august = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Учебно-методическая

class educMethodPlan(models.Model):
    num_p = models.CharField(max_length=20)
    eventName = models.CharField(max_length=256)
    time = models.CharField(max_length=64)
    plan = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Научная

class sciPlan(models.Model):
    num_p = models.CharField(max_length=20)
    eventName = models.CharField(max_length=256)
    as_a = models.CharField(max_length=256)
    time = models.CharField(max_length=64)
    plan = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Литература

class litPlan(models.Model):
    num_p = models.CharField(max_length=20)
    pubType = models.CharField(max_length=256)
    disc = models.CharField(max_length=256)
    direction = models.CharField(max_length=256)
    amount = models.FloatField()
    edition = models.FloatField()
    plan = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Другие виды работ

class otherPlan(models.Model):
    num_p = models.CharField(max_length=20)
    workName = models.CharField(max_length=256)
    time = models.CharField(max_length=64)
    plan = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern

# Повышение квалификации

class trainingPlan(models.Model):
    num_p = models.CharField(max_length=20)
    time = models.CharField(max_length=64)
    trainingType = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    plan = models.FloatField()
    fact = models.FloatField()
    usern = models.CharField(max_length=64, default='usr')
    planID = models.ForeignKey(
        'indPlan',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_p+"_2017/2018_"+self.usern
