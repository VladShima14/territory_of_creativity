$( document ).ready(function() {
	$(document).on('click', '.ordered_item .item_settings .item_price img', function() {
		$(this).closest(".ordered_item").remove();
	});


	$('.item_quantity .plus').click(function() {
		var num = parseInt($(this).parent().find('.quan_numb').text());
		$(this).parent().find('.quan_numb').text(num + 1);
	});
	$('.item_quantity .minus').click(function() {
		var num = parseInt($(this).parent().find('.quan_numb').text());
		if (num > 1) {
			$(this).parent().find('.quan_numb').text(num - 1);
		}
	});
});


