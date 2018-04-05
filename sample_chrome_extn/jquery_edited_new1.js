document.onclick = clickHandler;
//document.addEventListener("click", clickHandler, true);

function clickHandler(e){	

  var boxName = e.target;
  isArticle(boxName);
}

	var parentElsClassName ="";
	var parentElsTagName ="";
	//var flag = 0;
function isArticle(boxName){
	
	if(boxName.parentNode){
		if(boxName.tagName != "HTML"){
			
			 parentElsClassName += boxName.className + ",";
			 parentElsTagName += boxName.tagName + ",";
			 boxName = boxName.parentNode;
			 isArticle(boxName);
             
		}
		else
		{
			isValue(parentElsClassName,parentElsTagName); 
		}
	}	
}

function isValue(parentElsClassName,parentElsTagName){
	//alert("S");
	 var splitparentElsClassName = parentElsClassName.split(',');
	 var splitparentElsTagName = parentElsTagName.split(',');
	 var eleArray = [];
	 for(var i = 0;i<splitparentElsClassName.length;i++)
	 //for(var i = splitparentElsClassName.length-1;i>=0;i--)
	 {
		 eleArray.push(splitparentElsClassName[i]+ "," + splitparentElsTagName[i]);
		 
	 }
	
	
	isArray(eleArray);

}
function isArray(new_args){	

var lineArray = [];
//var infoArray = [];

new_args.forEach(function (infoArray, index) {
			var line = infoArray;
			lineArray.push(index == 0 ? "data:text/csv;charset=utf-8,classname,tagname \n" + line : line);
			
		});

var csvContent = lineArray.join("\n");
var encodedUri = encodeURI(csvContent);
var varlink = document.createElement("a");
varlink.setAttribute("href", encodedUri);
varlink.setAttribute("target","_blank");
varlink.setAttribute("download", "attributes.csv");
//document.body.appendChild(varlink); // Required for FF
varlink.click();
window.location.reload(true);

} 



	
	

