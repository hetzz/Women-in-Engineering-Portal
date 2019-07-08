function search(){
    var e = document.getElementById("field");
    var input = e.options[e.selectedIndex].text;
    var  filter, ul, li, a, i;
    filter = input.value.toUpperCase();
    console.log(filter)
    li = document.getElementsByClassName("student");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByClassName("badge pink lighten-5");
        console.log(a)
        for ( j = 0; j < a.length; j++)
        {
            console.log(a[j].innerHTML.toUpperCase());  
        //   if (a[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
        //       li[i].style.display = "";                   
        //       break;
        //   } else {
        //       li[i].style.display = "none";
        //   }
        }
    }
}