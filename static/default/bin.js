<!--
function $mm(obj){
   return (typeof obj == "object")?obj:document.getElementById(obj);;
}
//js操作cookie
function SetCookie(name,value){
	var minute = 10000; //保存天数
	var exp = new Date();
	exp.setTime(exp.getTime() + minute*60*1000*60*24);
	document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}
function getCookie(name){//取cookies函数
	var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
	if(arr != null) return unescape(arr[2]); return null;
}
function delCookie(name)//删除cookie
{
	var exp = new Date();
	exp.setTime(exp.getTime() - 1);
	var cval=getCookie(name);
	if(cval!=null) document.cookie= name + "="+cval+";expires="+exp.toGMTString();
}
//插入回复@
function backcomment(msg){
	$mm('content').value=$mm('content').value+"@"+msg;
}
function $mmajax(){
	var url=arguments[0]||""; 
	var queryStr=arguments[1]||""; 
	if(window.ActiveXObject){  
		xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");  
	}else if(window.XMLHttpRequest){
		xmlHttp = new XMLHttpRequest();  
	}
	if(0==xmlHttp.readyState || 4==xmlHttp.readyState){
		var browserflag=true;
		if(isFirefox=navigator.userAgent.indexOf("Firefox")>0){
			browserflag=false
		}
		xmlHttp.onreadystatechange=(browserflag)?(serverResponse):(serverResponse());				
		//xmlHttp.onreadystatechange=serverResponse;
	       xmlHttp.open("POST",url,browserflag);
	       xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	       xmlHttp.send(queryStr);
	       xmlHttp.onreadystatechange = (browserflag)?(serverResponse):(serverResponse());
	       }else{
			   window.alert("服务器超时...");
	       }
}
function serverResponse(){
	if(4==xmlHttp.readyState){
		if(200==xmlHttp.status){
			var resData=eval("["+xmlHttp.responseText+"]");
			alert(resData[0].msg);
			if(resData[0].no!=-1){
				if(resData[0].msg=='顶成功')
					$mm('dignum').innerHTML=parseInt($mm('dignum').innerHTML)+1;
				else
					$mm('dignum').innerHTML=parseInt($mm('dignum').innerHTML)-1;
			}
		}
	}
}
window.onload = function() {
	$mm('submit').disabled = false;
	if(getCookie("author")){
	$mm('name').value=getCookie("author");
	$mm('emails').value=getCookie("email");
	$mm('websites').value=getCookie("url")?getCookie("url"):"";
	}
}
//-->