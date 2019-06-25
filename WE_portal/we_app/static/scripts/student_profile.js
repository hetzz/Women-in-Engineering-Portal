$(document).ready(function(){
    $(".dropdown-trigger").dropdown({ hover: false });
});

$(document).ready(function() {
    $('textarea#About').characterCounter();
  });

$('#About').val('New Text');
  M.textareaAutoResize($('#About'));
    
$(document).ready(function(){
    $('select').formSelect();
  });