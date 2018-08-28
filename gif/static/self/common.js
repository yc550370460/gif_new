(function ()
{
	var menuline_current = null;

	$(function ()
	{

		$("#header .menu li.active").each(function ()
		{
			menuline_current = $(this).attr("data-index");
			showMenuLine(menuline_current);
		});


		$("#header .menu li").hover(function ()
		{
			var index = $(this).attr("data-index");
			showMenuLine(index);
		}, function ()
		{
		});

		$("#header .menu").hover(function ()
		{
		}, function ()
		{
			showMenuLine(menuline_current);
		});

		$(".dock ul.icons li").hover(function ()
		{
			$(".dock ul.icons li").removeClass("active");
			$(this).addClass("active");
		});

		$(".dock ul.icons").hover(function ()
		{

		}, function ()
		{
			$(".dock ul.icons li").removeClass("active");
		});

		$(".dock").each(function ()
		{
			$(this).css("top", ($(window).height() - $(this).height()) / 2);
		});
		$(window).resize(function ()
		{
			$(".dock").css("top", ($(window).height() - $(".dock").height()) / 2);
		});
		$("#archive").click(function(){
            AddFavorite('Gif','http://www.baidu.com')
        })
	});


    function AddFavorite(title,url){
    try{
       window.external.addFavorite(url,title);
     }
    catch(e){
     try{
        window.sidebar.addPanel(title,url,"");
      }
     catch(e){
       alert("Sorry, your web browser not support.\n\nPlease use Ctrl+D.");
       }
     }
    }

	window.showMenuLine = function (index)
	{
		var jmenuitem = $("#header .menu li:eq(" + index + ")");
		var op = {
			left: (jmenuitem.offset().left + 6) + "px",
			width : index == 4 ? "75px"  : "45px"
		};

		$("#menuline").show().animate(op, function ()
		{

		});

	};





})(jQuery);

