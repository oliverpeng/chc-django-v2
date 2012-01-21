(function($) {
    $(document).ready( function() {
        $('.read-more').toggle(
            function() {
                console.log('hi');
                $(this)
                    .html('Quick View -')
                    .next('.entry').slideDown().end()
                    .prev('.excerpt').slideUp();

            },
            function() {
                console.log('bye');
                $(this)
                    .html('Read More +')
                    .next('.entry').slideUp().end()
                    .prev('.excerpt').slideDown();
            }
        );
    });
})(jQuery);