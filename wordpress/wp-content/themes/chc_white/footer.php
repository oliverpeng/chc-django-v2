	<footer>
        <h2 hidden>Footer</h2>
        <div class="container">
            <div class="column">
                <h4>Contact Us</h4>
                <div class="vcard">
                    <span class="fn n">
                        <span class="given-name"></span>
                        <span class="additional-name"></span>
                        <span class="family-name"></span>
                    </span>
                    <div class="org">Churches Helping Churches</div>
                    <div class="adr">
                        <div class="street-address">P.O. Box 6558</div>
                        <span class="locality">Elgin</span>, 
                        <span class="region">IL</span><br>
                        <span class="postal-code">60121-6558</span>
                    </div>
                    <div class="tel">1-847-398-7024 ext. 3452</div>
                    <a class="email" href="mailto:information@churcheshelpingchurches.com">information@churcheshelpingchurches.com</a>
                </div>  
            </div>
            <div class="column">
                <h4>Co-Founders</h4>
                <ul class="square">
                    <li><a title="James MacDonald" href="http://jamesmacdonald.com/" target="_blank">jamesmacdonald.com</a></li>
                    <li><a title="Pastor Mark" href="http://pastormark.tv/" target="_blank">pastormark.tv</a></li>
                </ul>
            </div>
            <div class="column">
                <h4 class="search">Search</h4>
                <form method="get" id="searchform" action="/blog">
                    <input type="search" value="" name="s">
                </form>
                <h4>Connect With Us</h4>
                <ul class="connect">
                    <li><a title="Facebook" href="https://www.facebook.com/ChurchesHelpingChurches" target="_blank" class="ir">Facebook</a></li>
                    <li><a title="RSS" href="" target="_blank" class="ir">RSS Feed</a></li>
                    <li><a title="Twitter" href="http://twitter.com/churcheshelping" target="_blank" class="ir">Twitter</a></li>
                </ul>
            </div>

            <p id="copyright">Copyright © 2011-2012 Churches Helping Churches. All rights reserved.</p>
        </div>
    </footer>

	<?php wp_footer(); ?>

<!-- here comes the javascript -->

<!-- jQuery is called via the Wordpress-friendly way via functions.php -->

<!-- this is where we put our custom functions -->
<script src="/static/js/wp.js"></script>

<!-- Asynchronous google analytics; this is the official snippet.
	 Replace UA-XXXXXX-XX with your site's ID and uncomment to enable.
	 
<script>

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-XXXXXX-XX']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
-->
	
</body>

</html>
