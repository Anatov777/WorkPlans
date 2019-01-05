from django.shortcuts import render
from plan_tables.models import *
from django.contrib import auth
from django.db.models import Max

def create_plan(request):

    args = {}
    args['username'] = auth.get_user(request).username
    args['teacher'] = teacher.objects.filter(usern=auth.get_user(request).username)

    if request.method == "POST":
        selectDate = request.POST.get('selectYearCreate')[0:4]
        teacherIden = teacher.objects.get(usern=auth.get_user(request).username)
        maxPlanID = indPlan.objects.all().aggregate(Max('planID'))
        if maxPlanID['planID__max'] == None:
            maxPlanID['planID__max'] = 0
        print(maxPlanID['planID__max'])

        for i in range(4):
            indPlanObject = indPlan(
                planID = maxPlanID['planID__max']+1,
                year = str(int(selectDate)+i)+'/'+(str(int(selectDate)+i+1)),
                approval = 0,
                teacherID = teacherIden)

            indPlanObject.save()


    return render(request, 'create_plan/create_plan.html', args)
