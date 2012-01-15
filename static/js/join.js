$(document).ready( function() {
	$('#bar article').click( function() {
		var href = $(this).find('a').attr('href');
		window.location.href = href;
	});

});