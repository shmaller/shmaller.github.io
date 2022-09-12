// Nick Boni
// Fall 2020

function menu_icon_animation(x){
	x.classList.toggle("change");
}

function operate_menu(){
	if(document.getElementById("menu").style.width == "0px"){
		document.getElementById("menu").style.width = "250px";
		document.getElementById("main").style.marginLeft = "250px";
	} else{
		document.getElementById("menu").style.width = "0px";
		document.getElementById("main").style.marginLeft = "0px";
	}
}

function show_page_content(){
	document.getElementById("hidden_content").style.display="block";
}

function scale_page(){
	var siteWidth = 1280;
	var scale = screen.width /siteWidth;

	document.querySelector('meta[name="viewport"]').setAttribute('content', 'width='+siteWidth+', initial-scale='+scale+'');
}