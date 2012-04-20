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
    $('#wp-ads .scrollContainer > section:not(.ad-intro-video)').click( function() {
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

/* Blog rotating ad. If youtube video is playing, stop rotating ad. */
function onYouTubePlayerReady(playerId) {
    ytplayer = document.getElementById("ytplayer");
    ytplayer.addEventListener("onStateChange", "onytplayerStateChange");
}

function onytplayerStateChange(newState) {
    if (newState == 1) { // playing video
        jQuery('#wp-ads .scrollContainer').cycle('pause');
    } else {
        jQuery('#wp-ads .scrollContainer').cycle('resume');
    }
}