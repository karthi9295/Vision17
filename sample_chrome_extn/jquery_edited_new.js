
function clickHandler(e){
	alert("H");
  var boxName = e.target;
  isArticle(boxName);
}

	
function isArticle(boxName){
	if(boxName.parentNode){
		if(boxName.className){
			var parentElsClassName = boxName.className;
			var parentElsTagName = boxName.tagName;
			isValue(parentElsClassName,parentElsTagName);
			boxName = boxName.parentNode;
			isArticle(boxName);
		}
	}
		
}
document.onclick = clickHandler;

function isValue(parentElsClassName,parentElsTagName){
	var className = parentElsClassName;
	var tagName = parentElsTagName;
	var eleArray = [];
	eleArray.push("[" + parentElsTagName + "," + parentElsClassName + "]")
	//eleArray.join(",");
	//eleArray.push(parentElsClassName);
	//eleArray.join(",");
	
	//var eleArray_updated = [];
	/* for(var i = 0; i < eleArray.length; ++i)
		{
			eleArray_updated.push(eleArray[i]);
		} */
	//document.write(eleArray+",");
	//var eleArray_updated = Array.prototype.join.call(eleArray, ",");
	//isArray(eleArray_updated);
	document.write(eleArray + ",");
}
/* function isArray(eleArray_updated){	
var lineArray = [];
//var infoArray = [];
	eleArray_updated.forEach(function (infoArray, index) {
		var line = infoArray
			lineArray.push(index == 0 ? "data:text/csv;charset=utf-8," + line : line);
		});
var csvContent = lineArray.join("\n");
var encodedUri = encodeURI(csvContent);
var link = document.createElement("a");
link.setAttribute("href", encodedUri);
link.setAttribute("download", "my_data.csv");
document.body.appendChild(link); // Required for FF
link.click();
} 
 */

