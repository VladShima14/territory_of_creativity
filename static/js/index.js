$(document).ready(function () {
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.slider-nav',
        fade: true
    });
    $('.slider-nav').slick({
        // variableWidth: true,
        slidesToShow: 3, // 3,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.slider-for',
        focusOnSelect: true
    });
    $(".colors div").click(function(e){
        e.preventDefault();
        slideIndex = $(this).index();
        $(".slider-for").slick( 'slickGoTo', slideIndex );
        // $(this).removeClass("active");
        $(".colors div").removeClass("active");
        $(this).addClass("active");
    });
    $("#prev").click(function(){
        $(".slider-for").slick('slickPrev');
    })
    $("#next").click(function(){
        $(".slider-for").slick('slickNext');
    })
});