(function($, window) {

$(function(){
    $("#select-g-monomer .dropdown-menu li a").click(function() {
    	$("#select-g-monomer .btn:first-child").html($(this).text() + " <span class='caret'></span>");
    	$("#select-g-monomer .btn:first-child").val($(this).text());
    });

    function show_error(error) {
    	$("#target-input-form").addClass("has-error");
    	$("#error-text").removeClass("hidden");
    	$("#error-text").text(error);
    }

    function hide_error() {
    	$("#target-input-form").removeClass("has-error");
    	$("#error-text").addClass("hidden");
    }

    $("#download-gb-vector").click(function() {
    	var params = {
    		sequence: $("#target-sequence").val().toUpperCase(),
    		g_monomer: $("#select-g-monomer .btn").text().trim(),
    		backbone: $("#TALE-type .active").data("backbone").replace('-','')
    	};

    	// validation
    	if (params.sequence[0] != 'T') {
    		show_error("Target must begin with a thymine base.");
    	} else if (params.sequence.length < 2) {
    		show_error("Target must be at least 2 bases in length.");
    	} else if (params.sequence.length > 26) {
    		show_error("Target cannot be longer than 26 bases.");
    	} else if (!(/^([ATGC]*)$/.test(params.sequence))) {
    		show_error("Target must consist of nucleotides {A,G,T,C}.")
    	} else {
    		hide_error();
    		window.location.href = "/generate?" + $.param(params);
    	}
    });
});

}).call(this, jQuery, window);
