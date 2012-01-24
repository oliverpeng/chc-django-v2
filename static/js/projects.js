$(document).ready( function() {
    $.localScroll({
        hash: false
    });

    $('.toplevel .toggle')
        .css('cursor', 'pointer')
        .toggle(
            function() {
                $(this).parents('.toplevel').addClass('collapsed').next('ol').slideUp();
            },
            function() {
                $(this).parents('.toplevel').removeClass('collapsed').next('ol').slideDown();
            }
        );

    $('table tr:has(a)').hover(
        function() {
            $(this).addClass('hover');
        },
        function() {
            $(this).removeClass('hover');
        }
    );
});