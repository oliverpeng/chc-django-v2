$(document).ready( function() {
	$('#moreways article').click( function() {
		var href = $(this).find('a').attr('href');
		console.log(href);
		window.location.href = href;
	});

});