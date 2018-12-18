// var scrollFromTopPx = 200;

// $(window).scroll(function () {
// 	if ($(this).scrollTop() > scrollFromTopPx) {
// 		$('header').css('background-color','rgba(237,238,235, 0.98)');
// 		$(".right_menu, .left_menu, .shipping").css("display","none");
// 		$(".nav_logo").css(
// 		{
// 			"float":"none",
// 				// "margin-top":"44px"
// 			});
// 		$(".nav_logo img").css("width","70%");
// 		$("header").css("min-height","100px");
// 	} else {
// 		$('header').css('background-color','transparent');
// 		$(".right_menu, .left_menu, .shipping").css("display","block");
// 		$(".nav_logo").css(
// 		{
// 			"float":"left",
// 			"margin-top":"0"
// 		});
// 		$(".nav_logo img").css("width","100%");
// 		$("header").css("min-height","150px");
// 	}

// });

// $( document ).ready(function() {
//     $('#scroller').click(function () {
// 		$('body,html').animate(
// 			{scrollTop: 0}, 1000); return false;

// 	});
// });


$(document).ready(function() {
	$(".nav_menu > ul").hover(
		function(){
			$(".dropmenu").css("display","block");
		}, function(){
			$(".dropmenu").css("display","none");
		}
	);

	for(var i=1; i<=$(".nav_menu ul").length-1; i++){
		var curWidth = $(".nav_menu ul li:nth-child("+i+")").width();
		console.log(curWidth);
		$(".dropmenu ul:nth-child("+i+")").width(curWidth);
	}

});


