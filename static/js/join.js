$(document).ready( function() {
	$('#bar article').click( function() {
		var href = $(this).find('a').attr('href');
		window.location.href = href;
	});

	$('form#subscribe').validate({
		rules: {
			email: {
				required: true,
				email: true
			}
		},
		messages: {
			email: {
				required: "",
				email: "Please enter a valid email address"
			}
		},
		errorLabelContainer: '#subscribe_error'
	});
});