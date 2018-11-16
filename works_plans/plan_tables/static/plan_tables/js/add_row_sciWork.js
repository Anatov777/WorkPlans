function add_row_sciWork() {
    i_sciWork = document.getElementById('tableId_sciWork').rows.length-1;
    var table = document.getElementById("tableId_sciWork");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_sciWork_"+i_sciWork+"' form='form_sciWork' value='"+i_sciWork+"' class='academNumP' readonly>";
    newrow.insertCell(-1).innerHTML = "<textarea name='eventName_sciWork_"+i_sciWork+"' form='form_sciWork' cols='40' rows='1' class='academTextarea'></textarea>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='performer_sciWork_"+i_sciWork+"' form='form_sciWork' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='time_sciWork_"+i_sciWork+"' form='form_sciWork' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_sciWork_"+i_sciWork+"' name='plan_sciWork_"+i_sciWork+"' class='sum_plan_sciWork academNumInput'  form='form_sciWork'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_sciWork_"+i_sciWork+"' name='fact_sciWork_"+i_sciWork+"' class='fact_work_sciWork academNumInput' form='form_sciWork'>";

    document.getElementById('del_btn_sciWork').disabled = false;

    $(".fact_work_sciWork").on('input change', function(){
      calcHourly(['fact_sciWork_'], ['.sumFact_sciWork']);
    });

    $(".sum_plan_sciWork").on('input change', function(){
      calcHourly(['count_sciWork_'], ['.sumPlan_sciWork']);
    });
}
