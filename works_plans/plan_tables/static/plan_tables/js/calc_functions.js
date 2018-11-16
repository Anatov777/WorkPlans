function calculateSum(tableId, arrayOfClassesNames, sumTr, countSumTr, finalSum) {
  $('#'+tableId+' tr').each(function (i, tr) {
      var sumTrVal = 0;
      for (var i = 0; i < arrayOfClassesNames.length; i++) {
        sumTrVal +=  +$(arrayOfClassesNames[i], tr).val();
      }

      $(sumTr, tr).val(sumTrVal);
  });

  var i=1; sum=0;

  while (document.getElementById(countSumTr+i)){
    sum += +$('#'+countSumTr+i).val();
    i++;
  }

  $(finalSum).val(sum);
  $(finalSum).trigger('change');
}

function calcSumFact(factFieldsId, sumFactClassName) {
    var i=1; sum=0;
    while (document.getElementById(factFieldsId+i)){
      sum += +$('#'+factFieldsId+i).val();
      i++;
    }
    $(sumFactClassName).val(sum);
    $(sumFactClassName).trigger('change');
}

function calcHourly(arrayOfClassesNames, finalSumMonth) {
  for (var j = 0; j < arrayOfClassesNames.length; j++) {
    var i=1; sum=0;
    while (document.getElementById(arrayOfClassesNames[j]+i)){
      sum += +$('#'+arrayOfClassesNames[j]+i).val();
      i++;
    }
    $(finalSumMonth[j]).val(sum);
    $(finalSumMonth[j]).trigger('change');
  }
}

function showDate() {
  var date = new Date();
  date = (date.getFullYear()-1)+'/'+date.getFullYear()+' - '+ (date.getFullYear()+3) + '/' + (date.getFullYear()+4);
  return date;
}

$(function () {
    var calculate_plan_final = function () {
        $('#final_AcademicPlan').val(+$('.all_plan').val() + +$('.all_plan_spring').val() + +$('.sumfact_all_fallHourly').val() + +$('.sumfact_all_springHourly').val());
        $('#final_method').val(+$('.sumPlan_educMethodWork').val() + +$('.sumPlan_literature').val())
        $('#final_sci').val(+$('.sumPlan_sciWork').val())
        $('#final_other').val(+$('.sumPlan_otherWork').val())
        $('#final_qual').val(+$('.sumPlan_training').val())

        $('#final_sum').val(+$('#final_AcademicPlan').val() + +$('#final_method').val() + +$('#final_sci').val() + +$('#final_other').val() + +$('#final_qual').val());

        if ($('#final_AcademicPlan').val()){
          percent = parseFloat(($('#final_AcademicPlan').val()/900*100).toFixed(2));
          $('#final_AcademicPlan_percent').val(percent);
        }
        if ($('#final_method').val()){
          percent = parseFloat(($('#final_method').val()/720*100).toFixed(2));
          $('#final_methodPlan_percent').val(percent);
        }
        if ($('#final_sci').val()){
          percent = parseFloat(($('#final_sci').val()/720*100).toFixed(2));
          $('#final_sciPlan_percent').val(percent);
        }
        if ($('#final_other').val()){
          percent = parseFloat(($('#final_other').val()/360*100).toFixed(2));
          $('#final_otherPlan_percent').val(percent);
        }
        if ($('#final_qual').val()){
          percent = parseFloat(($('#final_qual').val()/360*100).toFixed(2));
          $('#final_qualPlan_percent').val(percent);
        }

        if ($('#final_sum').val()){
          percent = parseFloat(($('#final_sum').val()/1440*100).toFixed(2));
          $('#final_sumPlan_percent').val(percent);
        }

        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);

    };
    $('.all_plan, .all_plan_spring, .sumfact_all_fallHourly, .sumfact_all_springHourly').on('input change', calculate_plan_final);
    $('.sumPlan_educMethodWork, .sumPlan_literature').on('input change', calculate_plan_final);
    $('.sumPlan_sciWork, .sumPlan_otherWork, .sumPlan_training').on('input change', calculate_plan_final);

    if ($('.all_plan').val()){
      calculate_plan_final();
    }
});

$(function () {
    var calculate_fact_final = function () {
        $('#final_AcademicFact').val(+$('.all_fact').val() + +$('.all_fact_spring').val());
        $('#final_methodFact').val(+$('.sumFact_educMethodWork').val() + +$('.sumFact_literature').val())
        $('#final_sciFact').val(+$('.sumFact_sciWork').val())
        $('#final_otherFact').val(+$('.sumFact_otherWork').val())
        $('#final_qualFact').val(+$('.sumFact_training').val())

        $('#final_sumFact').val(+$('#final_AcademicFact').val() + +$('#final_methodFact').val() + +$('#final_sciFact').val() + +$('#final_otherFact').val() + +$('#final_qualFact').val());

        if ($('#final_AcademicFact').val()){
          percent = parseFloat(($('#final_AcademicFact').val()/900*100).toFixed(2));
          $('#final_AcademicFact_percent').val(percent);
        }
        if ($('#final_methodFact').val()){
          percent = parseFloat(($('#final_methodFact').val()/720*100).toFixed(2));
          $('#final_methodFact_percent').val(percent);
        }
        if ($('#final_sciFact').val()){
          percent = parseFloat(($('#final_sciFact').val()/720*100).toFixed(2));
          $('#final_sciFact_percent').val(percent);
        }
        if ($('#final_otherFact').val()){
          percent = parseFloat(($('#final_otherFact').val()/360*100).toFixed(2));
          $('#final_otherFact_percent').val(percent);
        }
        if ($('#final_qualFact').val()){
          percent = parseFloat(($('#final_qualFact').val()/360*100).toFixed(2));
          $('#final_qualFact_percent').val(percent);
        }

        if ($('#final_sumFact').val()){
          percent = parseFloat(($('#final_sumFact').val()/1440*100).toFixed(2));
          $('#final_sumFact_percent').val(percent);
        }
    };
    $(".all_fact, .all_fact_spring").on('input change', calculate_fact_final);
    $('.sumFact_educMethodWork, .sumFact_literature').on('input change', calculate_fact_final);
    $('.sumFact_sciWork, .sumFact_otherWork, .sumFact_training').on('input change', calculate_fact_final);

    if ($('.all_fact').val()){
      calculate_fact_final();
    }
});
