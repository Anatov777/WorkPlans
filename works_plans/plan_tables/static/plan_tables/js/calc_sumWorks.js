// Осень плановая

$(".sep, .oct, .nov, .dec, .jan").on('input change', function(){
  calculateSum('table_Fall', ['.sep', '.oct', '.nov', '.dec', '.jan'], '.sum_plan', 'count_', '.all_plan');
});

if ($('.sep').val()) {
  calculateSum('table_Fall', ['.sep', '.oct', '.nov', '.dec', '.jan'], '.sum_plan', 'count_', '.all_plan');
}

// Осень фактическая

$(".fact_work").on('input change', function(){
  calcSumFact('fact_', '.all_fact');
});
if ($('.fact_work').val())
{
  calcSumFact('fact_', '.all_fact');
}

// Весна плановая

$(".feb, .mar, .apr, .may, .jun, .jul, .aug").on('input change', function(){
  calculateSum('tableId_spring', ['.feb', '.mar', '.apr', '.may', '.jun', '.jul', '.aug'], '.sum_plan_spring', 'count_spring_', '.all_plan_spring');
});

if ($('.feb').val())
{
  calculateSum('tableId_spring', ['.feb', '.mar', '.apr', '.may', '.jun', '.jul', '.aug'], '.sum_plan_spring', 'count_spring_', '.all_plan_spring');
}

// Весна фактическая

$(".fact_work_spring").on('input change', function(){
  calcSumFact('fact_spring_', '.all_fact_spring');
});
if ($('.fact_work_spring').val())
{
  calcSumFact('fact_spring_', '.all_fact_spring');
}

// Осень почасовая

$(".sep_fallHourly, .oct_fallHourly, .nov_fallHourly, .dec_fallHourly, .jan_fallHourly").on('input change', function(){
  calculateSum('table_fallHourly', ['.sep_fallHourly', '.oct_fallHourly', '.nov_fallHourly', '.dec_fallHourly', '.jan_fallHourly'], '.sum_fact_fallHourly', 'count_fallHourly_', '.sumfact_all_fallHourly');

  calcHourly(['sep_fallHourly_', 'oct_fallHourly_', 'nov_fallHourly_', 'dec_fallHourly_', 'jan_fallHourly_'], ['.sep_all_fallHourly', '.oct_all_fallHourly', '.nov_all_fallHourly', '.dec_all_fallHourly', '.jan_all_fallHourly']);
});

if ($('.sep_fallHourly').val())
{
  calculateSum('table_fallHourly', ['.sep_fallHourly', '.oct_fallHourly', '.nov_fallHourly', '.dec_fallHourly', '.jan_fallHourly'], '.sum_fact_fallHourly', 'count_fallHourly_', '.sumfact_all_fallHourly');

  calcHourly(['sep_fallHourly_', 'oct_fallHourly_', 'nov_fallHourly_', 'dec_fallHourly_', 'jan_fallHourly_'], ['.sep_all_fallHourly', '.oct_all_fallHourly', '.nov_all_fallHourly', '.dec_all_fallHourly', '.jan_all_fallHourly']);
}

// Весна почасовая

$(".feb_springHourly, .mar_springHourly, .apr_springHourly, .may_springHourly, .jun_springHourly, .jul_springHourly, .aug_springHourly").on('input change', function(){

  calculateSum('table_springHourly', ['.feb_springHourly', '.mar_springHourly', '.apr_springHourly', '.may_springHourly', '.jun_springHourly', '.jul_springHourly', '.aug_springHourly'], '.sum_plan_springHourly', 'count_springHourly_', '.sumfact_all_springHourly');

  calcHourly(
    ['feb_springHourly_', 'mar_springHourly_', 'apr_springHourly_', 'may_springHourly_', 'jun_springHourly_', 'jul_springHourly_', 'aug_springHourly_'],
    ['.feb_all_springHourly', '.mar_all_springHourly', '.apr_all_springHourly', '.may_all_springHourly', '.jun_all_springHourly', '.jul_all_springHourly', '.aug_all_springHourly']
  );
});

if ($('.sep_fallHourly').val())
{
  calculateSum('table_springHourly', ['.feb_springHourly', '.mar_springHourly', '.apr_springHourly', '.may_springHourly', '.jun_springHourly', '.jul_springHourly', '.aug_springHourly'], '.sum_plan_springHourly', 'count_springHourly_', '.sumfact_all_springHourly');

  calcHourly(
    ['feb_springHourly_', 'mar_springHourly_', 'apr_springHourly_', 'may_springHourly_', 'jun_springHourly_', 'jul_springHourly_', 'aug_springHourly_'],
    ['.feb_all_springHourly', '.mar_all_springHourly', '.apr_all_springHourly', '.may_all_springHourly', '.jun_all_springHourly', '.jul_all_springHourly', '.aug_all_springHourly']
  );
}

// Учебно-методическая

$(".fact_work_educMethodWork").on('input change', function(){
  calcHourly(['fact_educMethodWork_'], ['.sumFact_educMethodWork']);
});

if ($('.fact_work_educMethodWork').val())
{
  calcHourly(['fact_educMethodWork_'], ['.sumFact_educMethodWork']);
}

$(".sum_plan_educMethodWork").on('input change', function(){
  calcHourly(['count_educMethodWork_'], ['.sumPlan_educMethodWork']);
});

if ($('.sum_plan_educMethodWork').val())
{
  calcHourly(['count_educMethodWork_'], ['.sumPlan_educMethodWork']);
}

// Научная

$(".fact_work_sciWork").on('input change', function(){
  calcHourly(['fact_sciWork_'], ['.sumFact_sciWork']);
});

if ($('.fact_work_sciWork').val())
{
  calcHourly(['fact_sciWork_'], ['.sumFact_sciWork']);
}

$(".sum_plan_sciWork").on('input change', function(){
  calcHourly(['count_sciWork_'], ['.sumPlan_sciWork']);
});

if ($('.sum_plan_sciWork').val())
{
  calcHourly(['count_sciWork_'], ['.sumPlan_sciWork']);
}

// Литература

$(".fact_work_literature").on('input change', function(){
  calcHourly(['fact_literature_'], ['.sumFact_literature']);
});

if ($('.fact_work_literature').val())
{
  calcHourly(['fact_literature_'], ['.sumFact_literature']);
}

$(".sum_plan_literature").on('input change', function(){
  calcHourly(['count_literature_'], ['.sumPlan_literature']);
});

if ($('.sum_plan_literature').val())
{
  calcHourly(['count_literature_'], ['.sumPlan_literature']);
}

// Другие виды работ

$(".fact_work_otherWork").on('input change', function(){
  calcHourly(['fact_otherWork_'], ['.sumFact_otherWork']);
});

if ($('.fact_work_otherWork').val())
{
  calcHourly(['fact_otherWork_'], ['.sumFact_otherWork']);
}

$(".sum_plan_otherWork").on('input change', function(){
  calcHourly(['count_otherWork_'], ['.sumPlan_otherWork']);
});

if ($('.sum_plan_otherWork').val())
{
  calcHourly(['count_otherWork_'], ['.sumPlan_otherWork']);
}

// Повышение квалификации

$(".fact_work_training").on('input change', function(){
  calcHourly(['fact_training_'], ['.sumFact_training']);
});

if ($('.fact_work_training').val())
{
  calcHourly(['fact_training_'], ['.sumFact_training']);
}

$(".sum_plan_training").on('input change', function(){
  calcHourly(['count_training_'], ['.sumPlan_training']);
});

if ($('.sum_plan_training').val())
{
  calcHourly(['count_training_'], ['.sumPlan_training']);
}
