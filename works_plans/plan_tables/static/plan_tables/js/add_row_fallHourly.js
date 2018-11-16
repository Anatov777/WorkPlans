function add_row_fallHourly() {
    i_fallHourly = document.getElementById('table_fallHourly').rows.length-2;
    var table = document.getElementById("table_fallHourly");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_fallHourly_"+i_fallHourly+"' class='academNumP' form='form_fallHourly' value='"+i_fallHourly+"' size='3' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='flow_fallHourly_"+i_fallHourly+"' class='academTextarea' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='disc_fallHourly_"+i_fallHourly+"' class='academTextarea' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='worktype_fallHourly_"+i_fallHourly+"' class='academTextarea' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='sep_fallHourly_"+i_fallHourly+"' id='sep_fallHourly_"+i_fallHourly+"' class='sep_fallHourly academNumInput' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='oct_fallHourly_"+i_fallHourly+"' id='oct_fallHourly_"+i_fallHourly+"' class='oct_fallHourly academNumInput' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='nov_fallHourly_"+i_fallHourly+"' id='nov_fallHourly_"+i_fallHourly+"' class='nov_fallHourly academNumInput' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='dec_fallHourly_"+i_fallHourly+"' id='dec_fallHourly_"+i_fallHourly+"' class='dec_fallHourly academNumInput' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='jan_fallHourly_"+i_fallHourly+"' id='jan_fallHourly_"+i_fallHourly+"' class='jan_fallHourly academNumInput' form='form_fallHourly'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_fallHourly_"+i_fallHourly+"' name='sumfact_fallHourly_"+i_fallHourly+"' class='sum_fact_fallHourly academNumInput'  form='form_fallHourly' readonly>";

    document.getElementById('del_btn_fallHourly').disabled = false;

    $(".sep_fallHourly, .oct_fallHourly, .nov_fallHourly, .dec_fallHourly, .jan_fallHourly").on('input change', function(){
      calculateSum('table_fallHourly', ['.sep_fallHourly', '.oct_fallHourly', '.nov_fallHourly', '.dec_fallHourly', '.jan_fallHourly'], '.sum_fact_fallHourly', 'count_fallHourly_', '.sumfact_all_fallHourly');

      calcHourly(['sep_fallHourly_', 'oct_fallHourly_', 'nov_fallHourly_', 'dec_fallHourly_', 'jan_fallHourly_'], ['.sep_all_fallHourly', '.oct_all_fallHourly', '.nov_all_fallHourly', '.dec_all_fallHourly', '.jan_all_fallHourly']);
    });
}
