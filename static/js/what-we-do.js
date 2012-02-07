$(document).ready( function() {
    $('#slider .panel')
        .css('cursor', 'pointer')
        .click( function() {
            var href = $(this).find('a').attr('href');
            if (href) {
                window.location.href = href;
            }
        });
});