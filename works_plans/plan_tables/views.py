from django.shortcuts import render
from .models import *
from django.contrib import auth


def setArgsTables(querySetName, modelName, teacherUsername, indPlanObject, request, args):
    try:
        if teacherUsername != None:
            args[querySetName] = modelName.objects.filter(usern=teacherUsername, planID=indPlanObject).order_by('num_p')
            args['selectTeacher'] = teacher.objects.filter(usern=teacherUsername)
        else:
            args[querySetName] = modelName.objects.filter(usern=auth.get_user(request).username, planID=indPlanObject).order_by('num_p')
    except modelName.DoesNotExist:
        args[querySetName] = None

def setArgs(request, plan_id, year_id):
    args = {}
    teacherUsername = None
    args['username'] = auth.get_user(request).username
    args['teacher'] = teacher.objects.filter(usern=auth.get_user(request).username)
    args['allTeachers'] = teacher.objects.all()
    args['checkApproval'] = indPlan.objects.filter(planID=1)

    if request.POST.get('chooseTeacher') or request.GET.get('chooseTeacher'):
        if request.POST.get('chooseTeacher'):
            s = request.POST.get('chooseTeacher')
        else:
            s = request.GET.get('chooseTeacher')
        s = s[:s.find(',')]
        lastName = s[:s.find(' ')]
        firstName = s[s.find(' ')+1:]
        teacherUsername = teacher.objects.filter(name = firstName, surname = lastName)
        for e in teacherUsername:
            teacherUsername = e.usern

        teacherIdObject = teacher.objects.filter(usern=teacherUsername)
        for e in teacherIdObject:
            teacherIdObject = e.teacherID

        args['planYear'] = indPlan.objects.filter(teacherID=teacherIdObject)
        args['argPlanId'] = indPlan.objects.filter(teacherID=teacherIdObject).distinct('planID')

    else:
        teacherIdObject = teacher.objects.filter(usern=auth.get_user(request).username)
        for e in teacherIdObject:
            teacherIdObject = e.teacherID

        args['planYear'] = indPlan.objects.filter(teacherID=teacherIdObject)
        args['argPlanId'] = indPlan.objects.filter(teacherID=teacherIdObject).distinct('planID')

    try:
        indPlanObject = indPlan.objects.get(planID=int(plan_id), year=year_id)
    except indPlan.DoesNotExist:
        indPlanObject = None

    setArgsTables('fallWorkQuerySet', plansFall, teacherUsername, indPlanObject, request, args)
    setArgsTables('fallHourlyWorkQuerySet', plansFallHourly, teacherUsername, indPlanObject, request, args)
    setArgsTables('springWorkQuerySet', plansSpring, teacherUsername, indPlanObject, request, args)
    setArgsTables('springHourlyWorkQuerySet', plansSpringHourly, teacherUsername, indPlanObject, request, args)
    setArgsTables('educMethodWorkQuerySet', educMethodPlan, teacherUsername, indPlanObject, request, args)
    setArgsTables('sciWorkQuerySet', sciPlan, teacherUsername, indPlanObject, request, args)
    setArgsTables('litWorkQuerySet', litPlan, teacherUsername, indPlanObject, request, args)
    setArgsTables('otherWorkQuerySet', otherPlan, teacherUsername, indPlanObject, request, args)
    setArgsTables('trainingWorkQuerySet', trainingPlan, teacherUsername, indPlanObject, request, args)

    return args


def choosePlanId(request, plan_id):
    argsChoosePlan = {}
    if request.method == 'POST':
        argsChoosePlan['choosedTeacher'] = request.POST.get('chooseTeacher')
    if request.method == 'GET':
        argsChoosePlan['choosedTeacher'] = request.GET.get('chooseTeacher')
    year_id = '2017/2018'
    argsChoosePlan['argSelectedPlanId'] = int(plan_id)
    print(argsChoosePlan['argSelectedPlanId'])
    argsCompleted = {**argsChoosePlan, **setArgs(request, plan_id, year_id)}
    return render(request, 'plan_tables/tables_input.html', argsCompleted)

def chooseYear(request, plan_id, year_id):
    args = {}
    argsChooseYear = {}
    if request.method == 'GET':
        argsChooseYear['choosedTeacher'] = request.GET.get('chooseTeacher')
    argsChooseYear['argSelectedPlanId'] = int(plan_id)
    argsChooseYear['argSelectedYear'] = year_id.replace('_','/')

    year_id = year_id.replace('_','/')
    argsCompleted = {**argsChooseYear, **setArgs(request, plan_id, year_id)}

    if request.method == "POST":

        # Осень

        i = 1
        try:
            while request.POST.get('num_p_'+str(i)) != None or plansFall.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_'+str(i)) != None and plansFall.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    fallObject = plansFall.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    fallObject.num_p = request.POST['num_p_'+str(i)]
                    fallObject.group = request.POST.get('flow_'+str(i))
                    fallObject.discipline = request.POST.get('disc_'+str(i))
                    fallObject.workType = request.POST.get('worktype_'+str(i))
                    fallObject.september = request.POST['sep_'+str(i)]
                    fallObject.october = request.POST['oct_'+str(i)]
                    fallObject.november = request.POST['nov_'+str(i)]
                    fallObject.december = request.POST['dec_'+str(i)]
                    fallObject.januar = request.POST['jan_'+str(i)]
                    fallObject.fact = request.POST['fact_'+str(i)]
                    fallObject.usern = auth.get_user(request).username

                    fallObject.save()
                    i += 1
                elif request.POST.get('num_p_1') != None and plansFall.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    fallObject = plansFall.objects.get(num_p=i, usern=auth.get_user(request).username)
                    fallObject.delete()
                    i += 1
                else:
                    i += 1

        except plansFall.DoesNotExist:

            while request.POST.get('num_p_'+str(i)) != None:
                fallObject = plansFall(
                    num_p=request.POST['num_p_'+str(i)],
                    group=request.POST.get('flow_'+str(i)),
                    discipline=request.POST.get('disc_'+str(i)),
                    workType=request.POST.get('worktype_'+str(i)),
                    september=request.POST['sep_'+str(i)],
                    october=request.POST['oct_'+str(i)],
                    november=request.POST['nov_'+str(i)],
                    december=request.POST['dec_'+str(i)],
                    januar=request.POST['jan_'+str(i)],
                    fact=request.POST['fact_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)

                fallObject.save()
                i += 1

        # Осень почасовая

        i = 1
        try:
            while request.POST.get('num_p_fallHourly_'+str(i)) != None or plansFallHourly.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_fallHourly_'+str(i)) != None and plansFallHourly.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    fallHourlyObject = plansFallHourly.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    fallHourlyObject.num_p = request.POST['num_p_fallHourly_'+str(i)]
                    fallHourlyObject.group=request.POST.get('flow_fallHourly_'+str(i))
                    fallHourlyObject.discipline=request.POST.get('disc_fallHourly_'+str(i))
                    fallHourlyObject.workType=request.POST.get('worktype_fallHourly_'+str(i))
                    fallHourlyObject.september=request.POST['sep_fallHourly_'+str(i)]
                    fallHourlyObject.october=request.POST['oct_fallHourly_'+str(i)]
                    fallHourlyObject.november=request.POST['nov_fallHourly_'+str(i)]
                    fallHourlyObject.december=request.POST['dec_fallHourly_'+str(i)]
                    fallHourlyObject.januar=request.POST['jan_fallHourly_'+str(i)]
                    fallHourlyObject.usern=auth.get_user(request).username

                    fallHourlyObject.save()
                    i += 1
                elif request.POST.get('num_p_fallHourly_1') != None and plansFallHourly.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    fallHourlyObject = plansFallHourly.objects.get(num_p=i, usern=auth.get_user(request).username)
                    fallHourlyObject.delete()
                    i += 1
                else:
                    i += 1

        except plansFallHourly.DoesNotExist:

            while request.POST.get('num_p_fallHourly_'+str(i)) != None:
                fallHourlyObject = plansFallHourly(
                    num_p=request.POST['num_p_fallHourly_'+str(i)],
                    group=request.POST.get('flow_fallHourly_'+str(i)),
                    discipline=request.POST.get('disc_fallHourly_'+str(i)),
                    workType=request.POST.get('worktype_fallHourly_'+str(i)),
                    september=request.POST['sep_fallHourly_'+str(i)],
                    october=request.POST['oct_fallHourly_'+str(i)],
                    november=request.POST['nov_fallHourly_'+str(i)],
                    december=request.POST['dec_fallHourly_'+str(i)],
                    januar=request.POST['jan_fallHourly_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)
                fallHourlyObject.save()
                i += 1


        # Весна

        i = 1
        try:
            while request.POST.get('num_p_spring_'+str(i)) != None or plansSpring.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_spring_'+str(i)) != None and plansSpring.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    springObject = plansSpring.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    springObject.num_p = request.POST['num_p_spring_'+str(i)]
                    springObject.group=request.POST.get('flow_spring_'+str(i))
                    springObject.discipline=request.POST.get('disc_spring_'+str(i))
                    springObject.workType=request.POST.get('worktype_spring_'+str(i))
                    springObject.february=request.POST['feb_'+str(i)]
                    springObject.march=request.POST['mar_'+str(i)]
                    springObject.april=request.POST['apr_'+str(i)]
                    springObject.may=request.POST['may_'+str(i)]
                    springObject.june=request.POST['jun_'+str(i)]
                    springObject.july=request.POST['jul_'+str(i)]
                    springObject.august=request.POST['aug_'+str(i)]
                    springObject.fact=request.POST['fact_spring_'+str(i)]
                    springObject.usern=auth.get_user(request).username

                    springObject.save()
                    i += 1
                elif request.POST.get('num_p_spring_1') != None and plansSpring.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    springObject = plansSpring.objects.get(num_p=i, usern=auth.get_user(request).username)
                    springObject.delete()
                    i += 1
                else:
                    i += 1

        except plansSpring.DoesNotExist:

            while request.POST.get('num_p_spring_'+str(i)) != None:
                springObject = plansSpring(
                    num_p=request.POST['num_p_spring_'+str(i)],
                    group=request.POST.get('flow_spring_'+str(i)),
                    discipline=request.POST.get('disc_spring_'+str(i)),
                    workType=request.POST.get('worktype_spring_'+str(i)),
                    february=request.POST['feb_'+str(i)],
                    march=request.POST['mar_'+str(i)],
                    april=request.POST['apr_'+str(i)],
                    may=request.POST['may_'+str(i)],
                    june=request.POST['jun_'+str(i)],
                    july=request.POST['jul_'+str(i)],
                    august=request.POST['aug_'+str(i)],
                    fact=request.POST['fact_spring_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)

                springObject.save()
                i += 1

        # Весна почасовая

        i = 1
        try:
            while request.POST.get('num_p_springHourly_'+str(i)) != None or plansSpringHourly.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_springHourly_'+str(i)) != None and plansSpringHourly.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    springHourlyObject = plansSpringHourly.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    springHourlyObject.num_p = request.POST['num_p_springHourly_'+str(i)]
                    springHourlyObject.group=request.POST.get('flow_springHourly_'+str(i))
                    springHourlyObject.discipline=request.POST.get('disc_springHourly_'+str(i))
                    springHourlyObject.workType=request.POST.get('worktype_springHourly_'+str(i))
                    springHourlyObject.february=request.POST['feb_springHourly_'+str(i)]
                    springHourlyObject.march=request.POST['mar_springHourly_'+str(i)]
                    springHourlyObject.april=request.POST['apr_springHourly_'+str(i)]
                    springHourlyObject.may=request.POST['may_springHourly_'+str(i)]
                    springHourlyObject.june=request.POST['jun_springHourly_'+str(i)]
                    springHourlyObject.july=request.POST['jul_springHourly_'+str(i)]
                    springHourlyObject.august=request.POST['aug_springHourly_'+str(i)]
                    springHourlyObject.usern=auth.get_user(request).username

                    springHourlyObject.save()
                    i += 1
                elif request.POST.get('num_p_springHourly_1') != None and plansSpringHourly.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    springHourlyObject = plansSpringHourly.objects.get(num_p=i, usern=auth.get_user(request).username)
                    springHourlyObject.delete()
                    i += 1
                else:
                    i += 1

        except plansSpringHourly.DoesNotExist:

            while request.POST.get('num_p_springHourly_'+str(i)) != None:

                springHourlyObject = plansSpringHourly(
                    num_p=request.POST['num_p_springHourly_'+str(i)],
                    group=request.POST.get('flow_springHourly_'+str(i)),
                    discipline=request.POST.get('disc_springHourly_'+str(i)),
                    workType=request.POST.get('worktype_springHourly_'+str(i)),
                    february=request.POST['feb_springHourly_'+str(i)],
                    march=request.POST['mar_springHourly_'+str(i)],
                    april=request.POST['apr_springHourly_'+str(i)],
                    may=request.POST['may_springHourly_'+str(i)],
                    june=request.POST['jun_springHourly_'+str(i)],
                    july=request.POST['jul_springHourly_'+str(i)],
                    august=request.POST['aug_springHourly_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)
                springHourlyObject.save()
                i += 1

        # Учебно-методическая

        i = 1
        try:
            while request.POST.get('num_p_educMethodWork_'+str(i)) != None or educMethodPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_educMethodWork_'+str(i)) != None and educMethodPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    educMethodObject = educMethodPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    educMethodObject.num_p = request.POST['num_p_educMethodWork_'+str(i)]
                    educMethodObject.eventName=request.POST.get('eventName_educMethodWork_'+str(i))
                    educMethodObject.time=request.POST.get('time_educMethodWork_'+str(i))
                    educMethodObject.plan=request.POST['plan_educMethodWork_'+str(i)]
                    educMethodObject.fact=request.POST['fact_educMethodWork_'+str(i)]
                    educMethodObject.usern=auth.get_user(request).username

                    educMethodObject.save()
                    i += 1
                elif request.POST.get('num_p_educMethodWork_1') != None and educMethodPlan.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    educMethodObject = educMethodPlan.objects.get(num_p=i, usern=auth.get_user(request).username)
                    educMethodObject.delete()
                    i += 1
                else:
                    i += 1

        except educMethodPlan.DoesNotExist:

            while request.POST.get('num_p_educMethodWork_'+str(i)) != None:

                educMethodObject = educMethodPlan(
                    num_p = request.POST['num_p_educMethodWork_'+str(i)],
                    eventName=request.POST.get('eventName_educMethodWork_'+str(i)),
                    time=request.POST.get('time_educMethodWork_'+str(i)),
                    plan=request.POST['plan_educMethodWork_'+str(i)],
                    fact=request.POST['fact_educMethodWork_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)

                educMethodObject.save()
                i += 1

        # Научная

        i = 1
        try:
            while request.POST.get('num_p_sciWork_'+str(i)) != None or sciPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_sciWork_'+str(i)) != None and sciPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    sciWorkObject = sciPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    sciWorkObject.num_p = request.POST['num_p_sciWork_'+str(i)]
                    sciWorkObject.eventName=request.POST['eventName_sciWork_'+str(i)]
                    sciWorkObject.as_a=request.POST['performer_sciWork_'+str(i)]
                    sciWorkObject.time=request.POST['time_sciWork_'+str(i)]
                    sciWorkObject.plan=request.POST['plan_sciWork_'+str(i)]
                    sciWorkObject.fact=request.POST['fact_sciWork_'+str(i)]
                    sciWorkObject.usern=auth.get_user(request).username

                    sciWorkObject.save()
                    i += 1
                elif request.POST.get('num_p_sciWork_1') != None and sciPlan.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    sciWorkObject = sciPlan.objects.get(num_p=i, usern=auth.get_user(request).username)
                    sciWorkObject.delete()
                    i += 1
                else:
                    i += 1

        except sciPlan.DoesNotExist:

            while request.POST.get('num_p_sciWork_'+str(i)) != None:

                sciWorkObject = sciPlan(
                    num_p = request.POST['num_p_sciWork_'+str(i)],
                    eventName=request.POST['eventName_sciWork_'+str(i)],
                    as_a=request.POST['performer_sciWork_'+str(i)],
                    time=request.POST['time_sciWork_'+str(i)],
                    plan=request.POST['plan_sciWork_'+str(i)],
                    fact=request.POST['fact_sciWork_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)

                sciWorkObject.save()
                i += 1

        # Литература

        i = 1
        try:
            while request.POST.get('num_p_literature_'+str(i)) != None or litPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_literature_'+str(i)) != None and litPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    litWorkObject = litPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    litWorkObject.num_p = request.POST['num_p_literature_'+str(i)]
                    litWorkObject.pubType=request.POST['litType_'+str(i)]
                    litWorkObject.disc=request.POST['disc_literature_'+str(i)]
                    litWorkObject.direction=request.POST['direction_literature_'+str(i)]
                    litWorkObject.amount=request.POST['amount_literature_'+str(i)]
                    litWorkObject.edition=request.POST['edition_literature_'+str(i)]
                    litWorkObject.plan=request.POST['plan_literature_'+str(i)]
                    litWorkObject.fact=request.POST['fact_literature_'+str(i)]
                    litWorkObject.usern=auth.get_user(request).username

                    litWorkObject.save()
                    i += 1
                elif request.POST.get('num_p_literature_1') != None and litPlan.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    litWorkObject = litPlan.objects.get(num_p=i, usern=auth.get_user(request).username)
                    litWorkObject.delete()
                    i += 1
                else:
                    i += 1

        except litPlan.DoesNotExist:

            while request.POST.get('num_p_literature_'+str(i)) != None:

                litWorkObject = litPlan(
                    num_p = request.POST['num_p_literature_'+str(i)],
                    pubType=request.POST['litType_'+str(i)],
                    disc=request.POST['disc_literature_'+str(i)],
                    direction=request.POST['direction_literature_'+str(i)],
                    amount=request.POST['amount_literature_'+str(i)],
                    edition=request.POST['edition_literature_'+str(i)],
                    plan=request.POST['plan_literature_'+str(i)],
                    fact=request.POST['fact_literature_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)

                litWorkObject.save()
                i += 1

        # Другие виды работ

        i = 1
        try:

            while request.POST.get('num_p_otherWork_'+str(i)) != None or otherPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_otherWork_'+str(i)) != None and otherPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    otherWorkObject = otherPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    otherWorkObject.num_p = request.POST['num_p_otherWork_'+str(i)]
                    otherWorkObject.workName=request.POST['nameWork_otherWork_'+str(i)]
                    otherWorkObject.time=request.POST['date_otherWork_'+str(i)]
                    otherWorkObject.plan=request.POST['plan_otherWork_'+str(i)]
                    otherWorkObject.fact=request.POST['fact_otherWork_'+str(i)]
                    otherWorkObject.usern=auth.get_user(request).username

                    otherWorkObject.save()
                    i += 1
                elif request.POST.get('num_p_otherWork_1') != None and otherPlan.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    otherWorkObject = otherPlan.objects.get(num_p=i, usern=auth.get_user(request).username)
                    otherWorkObject.delete()
                    i += 1
                else:
                    i += 1

        except otherPlan.DoesNotExist:

            if request.POST.get('nameWork_otherWork_'+str(i)) != None:
                while request.POST.get('num_p_otherWork_'+str(i)) != None:

                    otherWorkObject = otherPlan(
                        num_p = request.POST['num_p_otherWork_'+str(i)],
                        workName=request.POST['nameWork_otherWork_'+str(i)],
                        time=request.POST['date_otherWork_'+str(i)],
                        plan=request.POST['plan_otherWork_'+str(i)],
                        fact=request.POST['fact_otherWork_'+str(i)],
                        planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                        usern=auth.get_user(request).username)

                    otherWorkObject.save()
                    i += 1
            else:
                args['input_error'] = "Не заполнено обязательное поле"
                i += 1

        # Повышение квалификации

        i = 1
        try:
            while request.POST.get('num_p_training_'+str(i)) != None or trainingPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:

                if request.POST.get('num_p_training_'+str(i)) != None and trainingPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id)) != None:
                    trainingObject = trainingPlan.objects.get(num_p=i, usern=auth.get_user(request).username, planID=indPlan.objects.get(planID=int(plan_id), year=year_id))

                    trainingObject.num_p = request.POST['num_p_training_'+str(i)]
                    trainingObject.time=request.POST['period_training_'+str(i)]
                    trainingObject.trainingType=request.POST['type_training_'+str(i)]
                    trainingObject.company=request.POST['company_training_'+str(i)]
                    trainingObject.plan=request.POST['plan_training_'+str(i)]
                    trainingObject.fact=request.POST['fact_training_'+str(i)]
                    trainingObject.usern=auth.get_user(request).username

                    trainingObject.save()
                    i += 1
                elif request.POST.get('num_p_training_1') != None and trainingPlan.objects.get(num_p=i, usern=auth.get_user(request).username) != None:
                    trainingObject = trainingPlan.objects.get(num_p=i, usern=auth.get_user(request).username)
                    trainingObject.delete()
                    i += 1
                else:
                    i += 1

        except trainingPlan.DoesNotExist:

            while request.POST.get('num_p_training_'+str(i)) != None:

                trainingObject = trainingPlan(
                    num_p = request.POST['num_p_training_'+str(i)],
                    time=request.POST['period_training_'+str(i)],
                    trainingType=request.POST['type_training_'+str(i)],
                    company=request.POST['company_training_'+str(i)],
                    plan=request.POST['plan_training_'+str(i)],
                    fact=request.POST['fact_training_'+str(i)],
                    planID=indPlan.objects.get(planID=int(plan_id), year=year_id),
                    usern=auth.get_user(request).username)

                trainingObject.save()
                i += 1

        if request.POST.get('chooseTeacher') != None:
            s = request.POST.get('chooseTeacher')
            s = s[:s.find(',')]
            lastName = s[:s.find(' ')]
            firstName = s[s.find(' ')+1:]

            teacherUsername = teacher.objects.filter(name = firstName, surname = lastName)
            for e in teacherUsername:
                teacherUsername = e.usern


        # Проверка отправки на утверждение

        # if float(request.POST.get('approvalSendValue')) == 1:
        #     indPlanObject = indPlan.objects.get(planID=1)
        #     indPlanObject.approval = 0.5
        #
        #     indPlanObject.save()

    return render(request, 'plan_tables/tables_input.html', argsCompleted)

def index(request):

    args = {}
    teacherUsername = None
    args['username'] = auth.get_user(request).username
    args['teacher'] = teacher.objects.filter(usern=auth.get_user(request).username)
    args['allTeachers'] = teacher.objects.all()
    args['checkApproval'] = indPlan.objects.filter(planID=1)

    if request.POST.get('chooseTeacher') != None:
        args['choosedTeacher'] = request.POST.get('chooseTeacher')
        s = request.POST.get('chooseTeacher')
        s = s[:s.find(',')]
        lastName = s[:s.find(' ')]
        firstName = s[s.find(' ')+1:]
        teacherUsername = teacher.objects.filter(name = firstName, surname = lastName)
        for e in teacherUsername:
            teacherUsername = e.usern

        teacherIdObject = teacher.objects.filter(usern=teacherUsername)
        for e in teacherIdObject:
            teacherIdObject = e.teacherID

        args['planYear'] = indPlan.objects.filter(teacherID=teacherIdObject)
        args['argPlanId'] = indPlan.objects.filter(teacherID=teacherIdObject).distinct('planID')

    else:
        teacherIdObject = teacher.objects.filter(usern=auth.get_user(request).username)
        for e in teacherIdObject:
            teacherIdObject = e.teacherID

        args['planYear'] = indPlan.objects.filter(teacherID=teacherIdObject)
        args['argPlanId'] = indPlan.objects.filter(teacherID=teacherIdObject).distinct('planID')

    argsCompleted = {**args, **setArgs(request, 0, 0)}


    return render(request, 'plan_tables/tables_input.html', argsCompleted)
