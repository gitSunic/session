$(document).ready(function() {
    $('#search').on("input", function() {
		var poisk = $(this).val().toLowerCase();
		if (poisk.length > 0) {
			$('.item').each(function() {
				var t = $(this);
				var name = $(this).text();
				var i = name.toLowerCase().indexOf(poisk);
				if (i != -1) {
					t.show();
				} else {
					t.hide();
				}
			});
		} else {
			$('.item').each(function() {
				var t = $(this);
				$(this).show();
			});
		}
	});

    $('.menu-head').on('click', function() {
        if ($('.menu-item').css('display') != 'none') {
            $('.menu-item').slideUp(200);
        }
        else {
            $('.menu-item').slideDown(200);
        }
    });

    $('.add').on('click', function() {
        $(this).hide();
        $('form').show();
    });
});