
function clickHandler(e){
  var boxName = e.target;
  isArticle(boxName);
}

	
function isArticle(boxName){
	if(boxName.parentNode){
		if(boxName.className){
			var parentEls = boxName.className;
			isValue(parentEls);
			boxName = boxName.parentNode;
			isArticle(boxName);
		}
		else {
			var parentEls = boxName.tagName;
			isValue(parentEls);
			boxName = boxName.parentNode;
			isArticle(boxName);
		}	
	}
		
}
document.onclick = clickHandler;

function isValue(parentEls){
	var eleArray = [];
	eleArray.push(parentEls);
	document.write(eleArray + ",");

}


//document.onclick = clickHandler;
