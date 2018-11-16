function unsetDisabled(tableId, btnId, nativeNumRows) {
  if (document.getElementById(tableId).rows.length > nativeNumRows) document.getElementById(btnId).disabled = false;
}

function disSaveBtn(){
  var btnSave = document.getElementsByClassName("btnSave");
  for (var i = 0; i < btnSave.length; i++) {
    btnSave[i].disabled = true;
  }
}

unsetDisabled('table_Fall', 'del_btn_Fall', 5);
unsetDisabled('table_fallHourly', 'del_btn_fallHourly', 4);
unsetDisabled('tableId_spring', 'del_btn_spring', 5);
unsetDisabled('table_springHourly', 'del_btn_springHourly', 4);
unsetDisabled('tableId_educMethodWork', 'del_btn_educMethodWork', 3);
unsetDisabled('tableId_literature', 'del_btn_literature', 3);
unsetDisabled('tableId_otherWork', 'del_btn_otherWork', 3);
unsetDisabled('tableId_sciWork', 'del_btn_sciWork', 3);
unsetDisabled('tableId_training', 'del_btn_training', 3);
