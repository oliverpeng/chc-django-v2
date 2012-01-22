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
})(jQuery);