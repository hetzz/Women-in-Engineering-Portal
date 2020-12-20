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

  function search(){
    var e = document.getElementById("field");
    var input = e.options[e.selectedIndex].text;
    var  filter, ul, li, a, i;
    filter = input
    console.log(filter);
    li = document.getElementsByClassName("student");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByClassName("interest");
        for ( j = 0; j < a.length; j++)
        {
          console.log(a[j].innerHTML.search(filter))
          if (a[j].innerHTML.indexOf(filter) > -1) {
              li[i].style.display = "";
              break;
          } else {
              li[i].style.display = "none";
          }
        }
    }
}

$(document).ready(function(){
  $('select').formSelect();
});


  var TxtType = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};

TxtType.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

    var that = this;
    var delta = 200 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
    }

    setTimeout(function() {
    that.tick();
    }, delta);
};

window.onload = function() {
    var elements = document.getElementsByClassName('typewrite');
    for (var i=0; i<elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');
        if (toRotate) {
          new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
    document.body.appendChild(css);
};




      