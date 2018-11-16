function delRow(tableId, btnId, shift) {
  var table = document.getElementById(tableId);
  table.deleteRow(table.rows.length-shift);
  if (document.getElementById(tableId).rows.length-shift-1 == 1) document.getElementById(btnId).disabled = true;
}
