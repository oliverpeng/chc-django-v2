$(document).ready( function() {
    $.localScroll({
        hash: false
    });

    $('.toplevel')
        .css('cursor', 'pointer')
        .addClass('collapsed')
        .toggle(
            function() {
                $(this).removeClass('collapsed').next('ol').slideDown();
            },
            function() {
                $(this).addClass('collapsed').next('ol').slideUp();
            }
        )
        .next('ol').hide();
});