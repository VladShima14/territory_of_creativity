$(window).load(function() {
	

	$('.main_slider .flexslider').flexslider({
		animation: "slide",
		slideshowSpeed: 5000,
		animationSpeed: 600,
		controlNav: false,
		prevText: '<img src="img/arrw.png">',
		nextText: '<img src="img/arrw.png">'
		// directionNav: false
	});

	$('.pic_block .flexslider').flexslider({
		animation: "slide",
		slideshowSpeed: 3000,
		animationSpeed: 600,
		controlNav: false,
		directionNav: false
	});

	
});