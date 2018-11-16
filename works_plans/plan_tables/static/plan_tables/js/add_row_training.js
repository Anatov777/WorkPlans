function add_row_training() {
    i_training = document.getElementById('tableId_training').rows.length-1;
    var table = document.getElementById("tableId_training");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_training_"+i_training+"' form='form_training' value='"+i_training+"' class='academNumP' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='period_training_"+i_training+"' form='form_training' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='type_training_"+i_training+"' form='form_training' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='company_training_"+i_training+"' form='form_training' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_training_"+i_training+"' name='plan_training_"+i_training+"' class='sum_plan_training academNumInput'  form='form_training'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_training_"+i_training+"' name='fact_training_"+i_training+"' class='fact_work_training academNumInput' form='form_training'>";

    document.getElementById('del_btn_training').disabled = false;

    $(".fact_work_training").on('input change', function(){
      calcHourly(['fact_training_'], ['.sumFact_training']);
    });

    $(".sum_plan_training").on('input change', function(){
      calcHourly(['count_training_'], ['.sumPlan_training']);
    });
}
