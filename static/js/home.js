$(document).ready(function(){

    $('#pulse')
    	.hide()
    	.jsMovie({
	        sequence: 'Pulse_##.png',
	        from: 1,
	        to: 28,
	        folder : "/static/img/home/pulse/",
	        height: 55,
	        width: 55,
	        playOnLoad: true,
	    })
	    .bind("loaded", function() {
	    	$(this).fadeIn();
	    });
});