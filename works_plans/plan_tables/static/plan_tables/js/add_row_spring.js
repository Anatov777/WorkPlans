function add_row_spring() {
    i_spring = document.getElementById('tableId_spring').rows.length-3;
    var table = document.getElementById("tableId_spring");
    var newrow = table.insertRow(table.rows.length-2);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_spring_"+i_spring+"' class='academNumP' form='form_spring' value='"+i_spring+"' size='3' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='flow_spring_"+i_spring+"' class='academTextarea' form='form_spring'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='disc_spring_"+i_spring+"' class='academTextarea' form='form_spring'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='worktype_spring_"+i_spring+"' class='academTextarea' form='form_spring'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='feb_"+i_spring+"' class='feb academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='mar_"+i_spring+"' class='mar academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='apr_"+i_spring+"' class='apr academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='may_"+i_spring+"' class='may academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='jun_"+i_spring+"' class='jun academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='jul_"+i_spring+"' class='jul academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='aug_"+i_spring+"' class='aug academNumInput' form='form_spring'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_spring_"+i_spring+"' name='sumplan_spring_"+i_spring+"' class='sum_plan_spring academNumInput'  form='form_spring'class='academNumInput' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_spring_"+i_spring+"' name='fact_spring_"+i_spring+"' class='fact_work_spring academNumInput' form='form_spring'class='academNumInput'>";

    document.getElementById('del_btn_spring').disabled = false;

    $(".feb, .mar, .apr, .may, .jun, .jul, .aug").on('input change', function(){
      calculateSum('tableId_spring', ['.feb', '.mar', '.apr', '.may', '.jun', '.jul', '.aug'], '.sum_plan_spring', 'count_spring_', '.all_plan_spring');
    });

    $(".fact_work_spring").on('input change', function(){
      calcSumFact('fact_spring_', '.all_fact_spring');
    });
}
