/*
	Author: Mint IT Media
*/
var gotoTopFlag = false;
var items = '';

$(window).ready(function(){
	load_resize_listener();
	load_portafolio_menu_listener();
	menu_fixer();

	items = $('#portfolio a');
	$( window ).scroll(function() {
		scroll_listener();
	});
	$( window ).resize(function() {
		load_resize_listener();
		menu_fixer();
	});
	$("body").scrollTop(0);
});
/*
	function to keep menu fixed on top
*/
function menu_fixer(){
	$('.menu').css('left',$('.content').width()+120);
}
/*
	Function to listen portafolio menu clicks
*/
function load_portafolio_menu_listener(){
	$('#portfolio a').click(function(){
		gotoTop($(this).data('slug'));
		return false;
	});
}

/*
    Function to move scroll to specif element tag
*/
function gotoTop(id, more)
{
	var offset = typeof(more) != 'undefined' ? more : 0;
	if(id.length){
		gotoTopFlag = true;
		$('html, body').animate({
			scrollTop: $('#'+id).offset().top + offset
		}, 1000, function(){
			gotoTopFlag = false;
			scroll_listener();
		});
	}
}
/*
    Function to adjust the size of the videos to fit the full width of the column.
*/
function load_resize_listener(){
	$("iframe").each(function() { 
		var width = $(this).width();
		var height = $(this).height();
		var ratio = width / height;
		if($(".project").width() < 663){
			var newWidth = $(".project").width();
		}else{
			//var newWidth = $(".project").width() * 2 / 3;
			var newWidth = 670;
		}
		var newHeight = newWidth / ratio;
		$(this).width(newWidth).height(newHeight);
	});
}

/*
	function to listen scroll and updates main menu according to scroll position
*/
function scroll_listener(){	
	if(!gotoTopFlag && !$('#about').hasClass('in') && !$('#more').hasClass('in')){
		var offset = 5;
		var flag_portafolio = false;
		for(var i=0; i<items.length; i++){
			slug = $(items[i]).data('slug');
			if(!$('#'+slug).length) {
			    return;
			}
			if($(window).scrollTop() + offset > $('#'+slug).offset().top){
				flag_portafolio = true;
				if(!$(items[i]).hasClass('active')){
					$('#portfolio').find('.active').removeClass();
					$(items[i]).parent().addClass('active');
				}
			}
		}
		if(!flag_portafolio){
			$('#portfolio').find('.active').removeClass();
		}
	}
}
