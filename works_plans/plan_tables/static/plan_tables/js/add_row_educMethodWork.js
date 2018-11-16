function add_row_educMethodWork() {
    i_educMethodWork = document.getElementById('tableId_educMethodWork').rows.length-1;
    var table = document.getElementById("tableId_educMethodWork");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_educMethodWork_"+i_educMethodWork+"' form='form_educMethodWork' value='"+i_educMethodWork+"' class='academNumP' readonly>";
    newrow.insertCell(-1).innerHTML = "<textarea name='eventName_educMethodWork_"+i_educMethodWork+"' form='form_educMethodWork' cols='40' rows='1' class='academTextarea'></textarea>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='time_educMethodWork_"+i_educMethodWork+"' form='form_educMethodWork' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='mark_educMethodWork_"+i_educMethodWork+"' form='form_educMethodWork'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_educMethodWork_"+i_educMethodWork+"' name='plan_educMethodWork_"+i_educMethodWork+"' class='sum_plan_educMethodWork academNumInput'  form='form_educMethodWork'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_educMethodWork_"+i_educMethodWork+"' name='fact_educMethodWork_"+i_educMethodWork+"' class='fact_work_educMethodWork academNumInput' form='form_educMethodWork'>";

    document.getElementById('del_btn_educMethodWork').disabled = false;

    $(".fact_work_educMethodWork").on('input change', function(){
      calcHourly(['fact_educMethodWork_'], ['.sumFact_educMethodWork']);
    });

    $(".sum_plan_educMethodWork").on('input change', function(){
      calcHourly(['count_educMethodWork_'], ['.sumPlan_educMethodWork']);
    });
}
