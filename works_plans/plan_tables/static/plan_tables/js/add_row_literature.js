function add_row_literature() {
    i_literature = document.getElementById('tableId_literature').rows.length-1;
    var table = document.getElementById("tableId_literature");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_literature_"+i_literature+"' form='form_literature' value='"+i_literature+"' class='academNumP' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='litType_"+i_literature+"' class='academTextarea' form='form_literature'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='disc_literature_"+i_literature+"' form='form_literature' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='direction_literature_"+i_literature+"' form='form_literature' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='amount_literature_"+i_literature+"' form='form_literature' class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='edition_literature_"+i_literature+"' form='form_literature' class='academNumInput editionLit'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='mark_literature_"+i_literature+"' form='form_literature' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_literature_"+i_literature+"' name='plan_literature_"+i_literature+"' class='sum_plan_literature academNumInput'  form='form_literature' class='academTextarea'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_literature_"+i_literature+"' name='fact_literature_"+i_literature+"' class='fact_work_literature academNumInput' form='form_literature' class='academTextarea'>";

    document.getElementById('del_btn_literature').disabled = false;

    $(".fact_work_literature").on('input change', function(){
      calcHourly(['fact_literature_'], ['.sumFact_literature']);
    });

    $(".sum_plan_literature").on('input change', function(){
      calcHourly(['count_literature_'], ['.sumPlan_literature']);
    });
}
