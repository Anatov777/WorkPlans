function add_row_springHourly() {
    i_springHourly = document.getElementById('table_springHourly').rows.length-2;
    var table = document.getElementById("table_springHourly");
    var newrow = table.insertRow(table.rows.length-1);
    newrow.insertCell(-1).innerHTML = "<input type='text' name='num_p_springHourly_"+i_springHourly+"' class='academNumP' form='form_springHourly' value='"+i_springHourly+"' size='3' readonly>";
    newrow.insertCell(-1).innerHTML = "<input type='text' name='flow_springHourly_"+i_springHourly+"' class='academTextarea' form='form_springHourly'>"
    newrow.insertCell(-1).innerHTML = "<input type='text' name='disc_springHourly_"+i_springHourly+"' class='academTextarea' form='form_springHourly'>"
    newrow.insertCell(-1).innerHTML = "<input type='text' name='worktype_springHourly_"+i_springHourly+"' class='academTextarea' form='form_springHourly'>"
    newrow.insertCell(-1).innerHTML = "<input type='number' name='feb_springHourly_"+i_springHourly+"' id='feb_springHourly_"+i_springHourly+"' class='feb_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='mar_springHourly_"+i_springHourly+"' id='mar_springHourly_"+i_springHourly+"' class='mar_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='apr_springHourly_"+i_springHourly+"' id='apr_springHourly_"+i_springHourly+"' class='apr_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='may_springHourly_"+i_springHourly+"' id='may_springHourly_"+i_springHourly+"' class='may_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='jun_springHourly_"+i_springHourly+"' id='jun_springHourly_"+i_springHourly+"' class='jun_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='jul_springHourly_"+i_springHourly+"' id='jul_springHourly_"+i_springHourly+"' class='jul_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' name='aug_springHourly_"+i_springHourly+"' id='aug_springHourly_"+i_springHourly+"' class='aug_springHourly academNumInput' form='form_springHourly'class='academNumInput'>";
    newrow.insertCell(-1).innerHTML = "<input type='number' id='count_springHourly_"+i_springHourly+"' name='sumplan_springHourly_"+i_springHourly+"' class='sum_plan_springHourly academNumInput'  form='form_springHourly'class='academNumInput' readonly>";

    document.getElementById('del_btn_springHourly').disabled = false;

    $(".feb_springHourly, .mar_springHourly, .apr_springHourly, .may_springHourly, .jun_springHourly, .jul_springHourly, .aug_springHourly").on('input change', function(){

      calculateSum('table_springHourly', ['.feb_springHourly', '.mar_springHourly', '.apr_springHourly', '.may_springHourly', '.jun_springHourly', '.jul_springHourly', '.aug_springHourly'], '.sum_plan_springHourly', 'count_springHourly_', '.sumfact_all_springHourly');

      calcHourly(
        ['feb_springHourly_', 'mar_springHourly_', 'apr_springHourly_', 'may_springHourly_', 'jun_springHourly_', 'jul_springHourly_', 'aug_springHourly_'],
        ['.feb_all_springHourly', '.mar_all_springHourly', '.apr_all_springHourly', '.may_all_springHourly', '.jun_all_springHourly', '.jul_all_springHourly', '.aug_all_springHourly']
      );
    });
}
