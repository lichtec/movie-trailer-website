var main = function () {
    
    $('.arrow-next').click(function() {
        var currentSlide = $('.active-slide');
        var nextSlide= $('.active-slide').next();
        var currentDot = $('.active-dot');
        var nextDot= $('.active-dot').next();
        if(nextSlide.length == 0) {
			nextSlide = $('.slide').first();
			nextDot = $('.dot').first();
		}
        currentSlide.fadeOut(600);
        currentSlide.removeClass('active-slide');
        nextSlide.fadeIn(600);
        nextSlide.addClass('active-slide');
        currentDot.removeClass('active-dot');
        nextDot.addClass('active-dot');
    });
	
    $('.arrow-prev').click(function() {
        var currentSlide = $('.active-slide');
        var prevSlide= $('.active-slide').prev();
        var currentDot = $('.active-dot');
        var prevDot= $('.active-dot').prev();
        if(prevSlide.length == 0) {
    		prevSlide = $('.slide').last();
    		prevDot = $('.dot').last();
  		}
        currentSlide.fadeOut(600);
        currentSlide.removeClass('active-slide');
        prevSlide.fadeIn(600);
        prevSlide.addClass('active-slide');
        currentDot.removeClass('active-dot');
        prevDot.addClass('active-dot');
    });

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.active-slide', function (event) {
            //alert('test');
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
			//alert($(this).attr('class'));
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
};

$(document).ready(main);