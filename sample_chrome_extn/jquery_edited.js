

function clickHandler(e){
  var boxName = e.target;
  isArticle(boxName);
}

function isArticle(boxName){
 if(boxName.parentNode){
	if(boxName.className != 0){
    var parentEls = boxName.className;
	boxName = boxName.parentNode;
    isArticle(boxName);
	}
	else {
	var parentEls = boxName.tagName;
	boxName = boxName.parentNode;
    isArticle(boxName);
	}
	
	var eleArray = [];
	eleArray.push(parentEls);
	return eleArray;
	

}
}

document.onclick = clickHandler;
