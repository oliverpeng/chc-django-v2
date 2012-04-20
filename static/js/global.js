$(document).ready( function() {
	var glow = $('.glow-animation').addClass('glow');
	setInterval(function(){
	    glow.hasClass('glow') ? glow.removeClass('glow') : glow.addClass('glow');
	}, 5000);
});