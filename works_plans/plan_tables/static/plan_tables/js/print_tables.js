function printData()
{
    var divToPrint=document.getElementById("printTable");
    newWin= window.open("");
    newWin.document.write('<link rel="stylesheet" type="text/css" href="/static/plan_tables/styles/style.css">');
    newWin.document.write(divToPrint.outerHTML);
    newWin.print();
    newWin.close();
}
