$(document).ready(function() {
    $('#search').on("input", function() {
		var poisk = $(this).val().toLowerCase();
		if (poisk.length > 0) {
			$('.item').each(function() {
				var t = $(this);
				var name = t.children('a').text();
				var i = name.toLowerCase().indexOf(poisk);
				if (i != -1) {
					let up = name.substr(i, poisk.length);
					let span = '<span class="y">' + up + '</span>';
					let rename = name.replace(up, span);
					t.children('a').html(rename);
					t.show();
				} else {
					let bac = t.children('span').text();
					let span = '<span class="y">' + bac + '</span>';
					let rename = name.replace(span, bac);
					t.children('a').html(rename);
					t.hide();
				}
			});
		} else {
			$('.item').each(function() {
				var t = $(this);
				let name = $(this).text();
				let bac = t.children('span').text();
				let span = '<span class="y">' + bac + '</span>';
				let rename = name.replace(span, bac);
				t.children('a').html(rename);
				t.show();
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
					let up = name.substr(i, poisk.length);
					let span = '<span class="y">' + up + '</span>';
					let rename = name.replace(up, span);
					t.html(rename);
					t.show();
				} else {
					let bac = t.children('span').text();
					let span = '<span class="y">' + bac + '</span>';
					let rename = name.replace(span, bac);
					t.html(rename);
					t.hide();
				}
			});
		} else {
			$('.list-min>li').each(function() {
				var t = $(this);
				let name = $(this).text();
				let bac = t.children('span').text();
				let span = '<span class="y">' + bac + '</span>';
				let rename = name.replace(span, bac);
				t.html(rename);
				t.show();
			});
		}
	});

    $('.menu-head, .menu-icon').on('click', function() {
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

    $('.add_feed').on('click', function() {
    	$(this).hide();
    	$('.feedback_form').show();
    });
});