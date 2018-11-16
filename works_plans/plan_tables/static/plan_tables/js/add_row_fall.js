function add_row_Fall() {
    i_fall = document.getElementById('table_Fall').rows.length-3;
    var table = document.getElementById("table_Fall");
    var newrow = table.insertRow(table.rows.length-2);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_"+i_fall+"' class='academNumP' form='form_Fall' value='"+i_fall+"' size='3' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='flow_"+i_fall+"' class='academTextarea' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='disc_"+i_fall+"' class='academTextarea' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='worktype_"+i_fall+"' class='academTextarea' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='sep_"+i_fall+"' class='sep academNumInput' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='oct_"+i_fall+"' class='oct academNumInput' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='nov_"+i_fall+"' class='nov academNumInput' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='dec_"+i_fall+"' class='dec academNumInput' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='jan_"+i_fall+"' class='jan academNumInput' form='form_Fall'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_"+i_fall+"' name='sumplan_"+i_fall+"' class='sum_plan academNumInput'  form='form_Fall' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='fact_"+i_fall+"' name='fact_"+i_fall+"' class='fact_work academNumInput' form='form_Fall'>";

    document.getElementById('del_btn_Fall').disabled = false;

    $(".sep, .oct, .nov, .dec, .jan").on('input change', function(){
      calculateSum('table_Fall', ['.sep', '.oct', '.nov', '.dec', '.jan'], '.sum_plan', 'count_', '.all_plan');
    });

    $(".fact_work").on('input change', function(){
      calcSumFact('fact_', '.all_fact');
    });
}
