function bind_clicks() {

	// Make tweets clickable
	$('.twitter-tweet').click( function(e) {
		e.preventDefault();
		e.stopImmediatePropagation();

		// Get hyperlink		
		var hyperlink = $(this).attr('link')
		window.open(hyperlink,'testing')
	})
	
	// Navigation links
	$('.nav-link').click( function(e) {
		e.preventDefault();
		e.stopImmediatePropagation();

		// Identify which was clicked on
		var clicked_on_name = $(this).attr('id')
		
		// Fade out all content
		$('.body-area-content').fadeOut(150)

		setTimeout(function(){
		    // Fade in the appropriate content
			var content_name = '#' + clicked_on_name + '-content'
			console.log(content_name)
			$(content_name).fadeIn()
		}, 151);
	})
}

$( document ).ready(function() {
    bind_clicks()
});


