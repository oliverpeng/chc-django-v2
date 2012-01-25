(function($) {

    var FLICKR_API_KEY = '60873912bb09d2ef6ef7ec6979d8efa3',
        FLICKR_USER_ID = '46965176@N02',
        IMAGES_PER_PAGE = 9,
        IMAGES_PER_FETCH = 36,
        $photostream,
        $ulContainer,
        _firstFetch = true,
        _currPage = 0,
        _numPages = 0,
        
        /*
         * Private methods 
         */
        
        /* Simple helper function to convert key, value pairs in object to URL query string
        Sample input:
        {
             'key1': 'value1',
             'key2': 5
        }
        Output:
        "key1=value1&key2=5"
        
        NOT meant to be robust (handle array types, etc.)
        */
        _toUrlQueryString = function(object) {
            var array = [];
            $.each(object, function(index, value) {            
                if ( typeof(value)!== 'string' ) {
                    value = value.toString();
                }
             
                array.push(index + '=' + encodeURIComponent(value));
            });
            return array.join('&');
        },
        
        /* Builds Flickr photo URL based on http://www.flickr.com/services/api/misc.urls.html
        size parameter can be string or array of strings. If an array is provided, an object is returned
        keyed by size.
        
        Example:
        Input - ['m','s']
        Output - { m: 'url1', s: 'url2' }
        */
        _buildFlickrPhotoURL = function(farmId, serverId, id, secret, size) {
            // http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
            var base_url = 'http://farm'+ farmId +'.static.flickr.com/'+ serverId +'/'+ id +'_'+ secret;
            if (typeof(size) === 'string') {
                return base_url +'_'+ size +'.jpg';
            } else if ( size instanceof Array ) {
                var returnObj = {};
                $.each(size, function(i, v) {
                    returnObj[v] = base_url + '_' + v + '.jpg';
                });
                return returnObj;
            } else {
                return ''; // silent fail
            }
        },
        
        /* Make ajax request to fetch CHC's Flickr photostream
        Options:
         page     - page #
         per_page - how many images per request
         callback - callback function to run upon successful ajax request
        
        Based on Flickr API: http://www.flickr.com/services/api/
        */
        _ajaxFetchPhotos = function(options) {
            options = options || {};
            var defaultOpts = {
                'page': 1,
                'per_page': 30,
                'callback': function(json, textStatus, jqXHR) { /* do nothing */ }
            }
            options = $.extend({}, defaultOpts, options);
         
            var fetchParams = {
                'method': 'flickr.people.getPublicPhotos',
                'api_key': FLICKR_API_KEY,
                'user_id': FLICKR_USER_ID,
                'format': 'json',
                'nojsoncallback': 1
            }
            $.extend(fetchParams, { page: options.page, per_page: options.per_page, format: options.format });
         
            $.ajax({
                url: 'http://api.flickr.com/services/rest/?' + _toUrlQueryString(fetchParams),
                dataType: 'json',
                success: options.callback
            });
        },

        /* Returns page of current image being displayed in Fancybox
        */
        _getPageOfFancyBoxImage = function() {
            // What is URL of image being displayed?
            var imgSrc = $('.fancybox-image').attr('src');
            
            // Grab anchor tag that links to that URL
            var $thumb = $('a[href="'+imgSrc+'"]');
            var $ul = $thumb.parents('ul');

            var page = 0;
            do {
                $ul = $ul.prev();
                page++; 
            } while($ul.length > 0);

            return page;
        }
        
    /*
     * Public methods 
     */

    $.fn.flickrLoader = function() {
        var self = this,
            prevButton = $('<a></a>')
                .addClass('prev')
                .attr('title', 'Previous')
                .appendTo(self),
                
            viewPort = $('<div></div>')
                .addClass('viewport')
                .appendTo(self),
        
            ulContainer = $('<div></div>')
                .addClass('ul-container')
                .appendTo(viewPort),
            
            nextButton = $('<a></a>')
                .addClass('next')
                .attr('title', 'Next')
                .appendTo(self);
            
            galleryButton = $('<a></a>')
                .addClass('gallery')
                .attr('title', 'Gallery')
                .attr('href', 'http://www.flickr.com/photos/churcheshelpingchurches/')
                .attr('target', '_blank')
                .appendTo(self);
        
        $ulContainer = ulContainer;
        $photostream = $(self);
        
        // TODO: move this
        $photostream.bind('pageChange', function() {
            if ( _currPage <= 1 ) {
                prevButton.addClass('disabled');
            } else {
                prevButton.removeClass('disabled');
            }
            
            if ( _currPage >= _numPages ) {
                nextButton.addClass('disabled');
                $.flickrLoader.fetchImages();
            } else {
                nextButton.removeClass('disabled');
            }
        }).trigger('pageChange');
        
        nextButton.click( $.flickrLoader.nextPage );
        prevButton.click( $.flickrLoader.prevPage );
        
        return this;
    };
    
    $.flickrLoader = {};
    
    $.flickrLoader.fetchImages = function() {
        _ajaxFetchPhotos({
            page: (_numPages*IMAGES_PER_PAGE / IMAGES_PER_FETCH)+1,
            'per_page': IMAGES_PER_FETCH,
            callback: function(json) {
                if(!json.photos) {
                    // console.log(json.message);
                    return;
                }
                
                var $ul = $( document.createElement('ul') );
                $.each(json.photos.photo, function(i, photo) {
                    var urls = _buildFlickrPhotoURL(photo.farm, photo.server, photo.id, photo.secret, ['s','z']);
                    var $image = $( document.createElement('img') ).attr('src', urls.s);
                    var $a = $( document.createElement('a') ).attr('href', urls.z).attr('rel','group1').append( $image );
                    $( document.createElement('li') ).append( $a ).appendTo($ul);
                    
                    if ( (i+1)%IMAGES_PER_PAGE === 0 ) {
                        $ul.hide().appendTo($ulContainer);
                        $ul = $( document.createElement('ul') );
                    }
                });
                
                _numPages += IMAGES_PER_FETCH / IMAGES_PER_PAGE;
                
                if (_firstFetch) {
                    _firstFetch = false;
                    $ulContainer.find('ul:first').css('left', '890px').show();
                    _currPage = 1;
                }
                $photostream.trigger('pageChange');
                $('#photostream .ul-container a').fancybox({
                    afterShow: function() {
                        var currPage = $.flickrLoader.getCurrPage();
                        var pageOfImage = _getPageOfFancyBoxImage();

                        if( currPage < pageOfImage ) {
                            $.flickrLoader.nextPage();
                        } else if ( currPage > pageOfImage ) {
                            $.flickrLoader.prevPage();
                        }
                    }
                });
            }
        });
    };
    
    $.flickrLoader.nextPage = function() {
        if ( _currPage === _numPages ) {
            return;
        }
        
        var $currUL = $ulContainer.find('ul:visible');
        var $nextUL = $currUL.next();
        
        if ($currUL.queue('fx').length > 0 ) {  // wait for all animations to end first
            return;
        }
        
        $nextUL.css({left: 1780, display: 'block' }); // Put it right of current
        
        // Animate them both left
        $currUL.animate({left: 0}, 'slow', 'easeOutQuad', function() {
            $(this).hide();
        });
        $nextUL.animate({left: 890}, 'slow', 'easeOutQuad');
        
        _currPage++
        $photostream.trigger('pageChange');
    };
    
    $.flickrLoader.prevPage = function() {
        if ( _currPage === 1 ) {
            return;
        }
        
        var $currUL = $ulContainer.find('ul:visible');
        var $prevUL = $currUL.prev();
        
        if ($currUL.queue('fx').length > 0 ) {  // wait for all animations to end first
            return;
        }
        
        $prevUL.css({ left: 0, display: 'block' }); // Put it left of current
        
        // Animate them both right
        $currUL.animate({left: 1780}, 'slow', 'easeOutQuad', function() {
            $(this).hide();
        });
        $prevUL.animate({left: 890}, 'slow', 'easeOutQuad');
        
        _currPage--;
        $photostream.trigger('pageChange');
    };
    
    $.flickrLoader.getCurrPage = function() {
        return _currPage;
    }
    
    $.flickrLoader.getPageOfImage = function(imageIndex) {
        return Math.floor(imageIndex/IMAGES_PER_PAGE)+1;
    }
    
})(jQuery);
