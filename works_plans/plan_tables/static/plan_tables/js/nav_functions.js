function getSelectValue(id) {
  select = document.getElementById(id);
  value = select.value;
  return value;
}

function toPlanId(id) {
  var url = "/plan_tables/plan_"+getSelectValue(id);
  if (document.getElementById('chooseTeacherId').getAttribute('value')){
      url += "?chooseTeacher=" + document.getElementById('chooseTeacherId').getAttribute('value');
  }
  return url;
}

function toYear(id) {
  url = location.href;
  if (url.split('/')[5]){
    url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2] + '/' + url.split('/')[3] + '/' + url.split('/')[4];
    url += "/" + getSelectValue(id).replace('/','_');
    url += "?chooseTeacher=" + document.getElementById('chooseTeacherId').getAttribute('value');
  }
  else{
    url = url.split('?')[0];
    url += "/" + getSelectValue(id).replace('/','_');
    url += "?chooseTeacher=" + document.getElementById('chooseTeacherId').getAttribute('value');
  }
  return url;
}

function toPrint() {
  url = location.href;
  if (!url.split('print_tables')[1]) {
    url = url.split('plan_tables')[0] + 'plan_tables/print_tables' + url.split('plan_tables')[1];
  }
  return url;
}

function toFill() {
  url = location.href;
  if (url.split('print_tables')[1]) {
    url = url.split('plan_tables')[0] + 'plan_tables' + url.split('print_tables')[1];
  }
  return url;
}

function showDate() {
  var date = new Date();
  date = (date.getFullYear()-1)+'/'+date.getFullYear()+' - '+ (date.getFullYear()+3) + '/' + (date.getFullYear()+4);
  return date;
}

function printData() {
   var divToPrint=document.getElementById("printTable");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();
   newWin.close();
}

function setSelected(optionId) {
   document.getElementById(optionId).selected = 'selected';
}
