(function($, window) {

$(function(){
    $("#select-g-monomer .dropdown-menu li a").click(function(){
      $("#select-g-monomer .btn:first-child").html($(this).text() + " <span class='caret'></span>");
      $("#select-g-monomer .btn:first-child").val($(this).text());
   });
});

}).call(this, jQuery, window);
