from django.shortcuts import render
from plan_tables.models import *
from django.contrib import auth


def setArgsPrintTables(querySetName, modelName, teacherUsername, indPlanObject, request, args):
    try:
        if teacherUsername != None:
            args[querySetName+'QuerySet'] = modelName.objects.filter(usern=teacherUsername)
            args['selectTeacher'] = teacher.objects.filter(usern=teacherUsername)
        else:
            args[querySetName+'QuerySet'] = modelName.objects.filter(usern=auth.get_user(request).username, planID=indPlanObject).order_by('num_p')
    except modelName.DoesNotExist:
        args[querySetName+'QuerySet'] = None

def fall_table(request, plan_id, year_id):

    args = {}
    args['username'] = auth.get_user(request).username
    args['teacher'] = teacher.objects.filter(usern=auth.get_user(request).username)

    args['argSelectedPlanId'] = int(plan_id)
    args['argSelectedYear'] = year_id.replace('_','/')

    teacherUsername = None


    teacherIdObject = teacher.objects.filter(usern=auth.get_user(request).username)
    for e in teacherIdObject:
        teacherIdObject = e.teacherID

    args['planYear'] = indPlan.objects.filter(teacherID=teacherIdObject)
    args['argPlanId'] = indPlan.objects.filter(teacherID=teacherIdObject).distinct('planID')

    indPlanObject = indPlan.objects.get(planID=int(plan_id), year=year_id.replace('_','/'))

    setArgsPrintTables('fallWork', plansFall, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('fallHourlyWork', plansFallHourly, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('springWork', plansSpring, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('springHourlyWork', plansSpringHourly, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('educMethodWork', educMethodPlan, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('sciWork', sciPlan, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('litWork', litPlan, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('otherWork', otherPlan, teacherUsername, indPlanObject, request, args)
    setArgsPrintTables('trainingWork', trainingPlan, teacherUsername, indPlanObject, request, args)


    return render(request, 'print_tables/print_table.html', args)
