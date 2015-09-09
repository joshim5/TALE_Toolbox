(function($, window) {

$(function(){
    $("#select-g-monomer .dropdown-menu li a").click(function() {
    	$("#select-g-monomer .btn:first-child").html($(this).text() + " <span class='caret'></span>");
    	$("#select-g-monomer .btn:first-child").val($(this).text());
    });

    $("#download-gb-vector").click(function() {
    	var params = {
    		sequence: $("#target-sequence").val(),
    		g_monomer: $("#select-g-monomer .btn").text().trim(),
    		backbone: $("#TALE-type .active").data("backbone")
    	};
    	window.location.href = "/generate?" + $.param(params);
    });
});

}).call(this, jQuery, window);
