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

	$('#search-min').on("input", function() {
		var poisk = $(this).val().toLowerCase();
		if (poisk.length > 0) {
			$('.list-min>li').each(function() {
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
			$('.list-min>li').each(function() {
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

    $('.list-min>div').each(function() {
    	let d = $(this);
    	if (d.html() == '') {
    		d.prev().css('color', 'red');
    	}
    });

    $('.list-min>li').on('click', function() {
    	let d = $(this).next();
    	if (d.css('display') == 'none') {
    		d.show();
    	} else {
    		d.hide();
    	}
    });
});