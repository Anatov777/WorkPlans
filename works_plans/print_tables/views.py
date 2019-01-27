from django.shortcuts import render
from plan_tables.models import *
from django.contrib import auth


def fall_table(request, plan_id, year_id):

    args = {}

    if request.GET.get('chooseTeacher'):
        s = request.GET.get('chooseTeacher')
        s = s.split(',')
        teacherId = s[2].replace(' ', '')
    args['selectTeacher'] = teacher.objects.filter(teacherID=teacherId)
    args['username'] = auth.get_user(request).username
    args['teacher'] = teacher.objects.filter(usern=auth.get_user(request).username)

    args['argSelectedPlanId'] = int(plan_id)
    args['argSelectedYear'] = year_id.replace('_','/')
    args['choosedTeacher'] = request.GET.get('chooseTeacher')

    teacherUsername = teacher.objects.get(teacherID=teacherId)
    teacherUsername = teacherUsername.usern

    teacherIdObject = teacher.objects.filter(usern=auth.get_user(request).username)
    for e in teacherIdObject:
        teacherIdObject = e.teacherID

    args['planYear'] = indPlan.objects.filter(teacherID=teacherIdObject)
    args['argPlanId'] = indPlan.objects.filter(teacherID=teacherIdObject).distinct('planID')

    indPlanObject = indPlan.objects.get(planID=int(plan_id), year=year_id.replace('_','/'))

    args['fallWorkQuerySet'] = plansFall.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['fallHourlyWorkQuerySet'] = plansFallHourly.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['springWorkQuerySet'] = plansSpring.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['springHourlyWorkQuerySet'] = plansSpringHourly.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['educMethodWorkQuerySet'] = educMethodPlan.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['sciWorkQuerySet'] = sciPlan.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['litWorkQuerySet'] = litPlan.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['otherWorkQuerySet'] = otherPlan.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
    args['trainingWorkQuerySet'] = trainingPlan.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')

    return render(request, 'print_tables/print_table.html', args)
