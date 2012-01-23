(function($) {
    $(document).ready( function() {
        $('.read-more').toggle(
            function() {
                $(this)
                    .html('Quick View -')
                    .next('.entry').slideDown().end()
                    .prev('.excerpt').slideUp();
            },
            function() {
                $(this)
                    .html('Read More +')
                    .next('.entry').slideUp().end()
                    .prev('.excerpt').slideDown();
            }
        );
    });

    // Entire rotating ad banner is clickable
    $('#wp-ads .scrollContainer > section').click( function() {
        var href = $(this).find('a').attr('href');
        if (href) {
            window.location.href = href;
        }
    }).css('cursor', 'pointer');

    $('#wp-ads .scrollContainer').cycle({
        fx: 'scrollLeft',
        easing: 'swing',
        timeout: 8000,
        pager:  '#wp-ads .nav',
        speed: 500
      });
})(jQuery);