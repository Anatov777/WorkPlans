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
  if (url.length > 65) {
    url = url.split('?')[0];
    if (url.length > 55) {
      url = url.slice(0, -10);
      url += "/" + getSelectValue(id).replace('/','_') + "?chooseTeacher=" + document.getElementById('chooseTeacherId').getAttribute('value');
    }
    else url += "/" + getSelectValue(id).replace('/','_') + "?chooseTeacher=" + document.getElementById('chooseTeacherId').getAttribute('value');
  }
  else if (url.length > 52) {
    url = url.slice(-16, -10);
    url = "/plan_tables/"+url+"/"+getSelectValue(id).replace('/','_');
  }
  else {
    url = url.slice(-6);
    url = "/plan_tables/"+url+"/"+getSelectValue(id).replace('/','_');
  }
  return url;
}

function toPrint() {
  url = location.href;
  url = url.slice(-16);
  url = "/plan_tables/print_tables/"+url;
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
