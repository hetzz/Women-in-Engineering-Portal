function radiobuttons(checked)
{
    switch(checked)
    {
        case 1: document.getElementById('Student').checked=true;
        document.getElementById('Faculty').checked=false;
        document.getElementById('Company').checked=false;
        break;
        case 2: document.getElementById('Student').checked=false;
        document.getElementById('Faculty').checked=true;
        document.getElementById('Company').checked=false;
        break;
        case 3: document.getElementById('Student').checked=false;
        document.getElementById('Faculty').checked=false;
        document.getElementById('Company').checked=true;
        break;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      direction: 'left'
    });
  });

  $(document).ready(function(){
    $('.modal').modal();
    $('.modal-close').modal('close');
  });