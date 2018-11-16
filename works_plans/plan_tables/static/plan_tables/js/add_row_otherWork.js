function add_row_otherWork() {
    i_otherWork = document.getElementById('tableId_otherWork').rows.length-1;
    var table = document.getElementById("tableId_otherWork");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_otherWork_"+i_otherWork+"' form='form_otherWork' value='"+i_otherWork+"' class='academNumP' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='nameWork_otherWork_"+i_otherWork+"' form='form_otherWork' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='date_otherWork_"+i_otherWork+"' form='form_otherWork' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_otherWork_"+i_otherWork+"' name='plan_otherWork_"+i_otherWork+"' class='sum_plan_otherWork academNumInput'  form='form_otherWork'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_otherWork_"+i_otherWork+"' name='fact_otherWork_"+i_otherWork+"' class='fact_work_otherWork academNumInput' form='form_otherWork'>";

    document.getElementById('del_btn_otherWork').disabled = false;

    $(".fact_work_otherWork").on('input change', function(){
      calcHourly(['fact_otherWork_'], ['.sumFact_otherWork']);
    });

    $(".sum_plan_otherWork").on('input change', function(){
      calcHourly(['count_otherWork_'], ['.sumPlan_otherWork']);
    });
}
