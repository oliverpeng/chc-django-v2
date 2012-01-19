$(document).ready( function() {
	$('#signup-form').validate({
		rules: {
			fname: "required",
			lname: "required",
			email: {
				required: true,
				email: true
			},
			church_name: {
				required: function(element) {
					return $('#id_is_pastor').is(':checked')
				}
			}
		},
		messages: {
			fname: "",
			lname: "",
			email: {
				required: "",
				email: "Please enter a valid email address"
			},
			church_name: "Please enter a church name if you are a pastor"
		}
	});

	function is_church_required() {
		var $required_star = $('label[for="id_church_name"] .highlight');
		console.log(this);
		if ( $(this).is(':checked') ) {
			$required_star.show();
		} else {
			$required_star.hide();
		}
	}
	$('#id_is_pastor').click( is_church_required );
	is_church_required();

});