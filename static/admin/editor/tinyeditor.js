TINY={};

function T$(i){return document.getElementById(i)}
function T$$$(){return document.all?1:0}
var uploadexc="";
var colorswitch="";
var editorobj;
var bodyevent;
TINY.editor=function(){
	var c=[], offset=-30;
	c['cut']=[1,'剪切','a','cut',1];
	c['copy']=[2,'复制','a','copy',1];
	c['paste']=[3,'粘贴','a','paste',1];
	c['bold']=[4,'粗体','a','bold'];
	c['italic']=[5,'斜体','a','italic'];
	c['underline']=[6,'下划线','a','underline'];
	c['strikethrough']=[7,'删除线','a','strikethrough'];
	c['subscript']=[8,'下标','a','subscript'];
	c['superscript']=[9,'上标','a','superscript'];
	c['orderedlist']=[10,'数字列表','a','insertorderedlist'];
	c['unorderedlist']=[11,'符号列表','a','insertunorderedlist'];
	c['outdent']=[12,'减少缩进','a','outdent'];
	c['indent']=[13,'增加缩进','a','indent'];
	c['leftalign']=[14,'左对齐','a','justifyleft'];
	c['centeralign']=[15,'居中','a','justifycenter'];
	c['rightalign']=[16,'右对齐','a','justifyright'];
	c['blockjustify']=[17,'两端对齐','a','justifyfull'];
	c['undo']=[18,'撤销','a','undo'];
	c['redo']=[19,'重做','a','redo'];
	c['image']=[20,'插入图片','i','insertimage','输入图片地址:','http://'];
	
	c['hr']=[21,'插入分隔线','a','inserthorizontalrule'];
	c['link']=[22,'插入超链接','i','createlink','输入地址:','http://'];
	c['unlink']=[23,'移除链接','a','unlink'];
	c['unformat']=[24,'移除格式','a','removeformat'];
	c['print']=[25,'打印','a','print'];
	c['swf']=[26,'插入Flash','i','insertswf','输入Flash地址:','http://'];
	c['media']=[27,'插入视频','i','insertmedia','输入视频地址L:','http://'];
	c['upload']=[28,'上传文件','a','uploadfile'];
	c['forecolor']=[29,'文字颜色','a','forecolor'];
	c['backcolor']=[30,'文字背景','a','backcolor'];
	function edit(n,obj){
		this.n=n; window[n]=this; this.t=T$(obj.id); this.obj=obj; this.xhtml=obj.xhtml;
		var p=document.createElement('div'), w=document.createElement('div'), h=document.createElement('div'),
		l=obj.controls.length, i=0;
		this.i=document.createElement('iframe'); this.i.frameBorder=0;
		//添加iframe的id
		this.i.id=obj.iframeid||'editoriframe';
		subbtn=obj.subbutton||'subit';
		//添加结束
		this.i.width=obj.width||'500'; this.i.height=obj.height||'250'; this.ie=T$$$();
		h.className=obj.rowclass||'teheader'; p.className=obj.cssclass||'te'; p.style.width=this.i.width+'px'; p.appendChild(h);
		for(i;i<l;i++){
			var id=obj.controls[i];
			if(id=='n'){
				h=document.createElement('div'); h.className=obj.rowclass||'teheader'; p.appendChild(h)
			}else if(id=='|'){
				var d=document.createElement('div'); d.className=obj.dividerclass||'tedivider'; h.appendChild(d)
			}else if(id=='font'){
				var sel=document.createElement('select'), fonts=obj.fonts||['Verdana','Arial','Georgia'], fl=fonts.length, x=0;
				sel.className='tefont'; sel.onchange=new Function(this.n+'.ddaction(this,"fontname")');
				sel.options[0]=new Option('字体','');
				for(x;x<fl;x++){
					var font=fonts[x];
					sel.options[x+1]=new Option(font,font)
				}
				h.appendChild(sel)
			}else if(id=='size'){
				var sel=document.createElement('select'), sizes=obj.sizes||['T',1,2,3,4,5,6,7], sl=sizes.length, x=0;
				sel.className='tesize'; sel.onchange=new Function(this.n+'.ddaction(this,"fontsize")');
				for(x;x<sl;x++){
					var size=sizes[x];
					sel.options[x]=new Option(size,size)
				}
				h.appendChild(sel)
			}else if(id=='style'){
				var sel=document.createElement('select'),
				styles=obj.styles||[['样式',''],['段落','<p>'],['Header 1','<h1>'],['Header 2','<h2>'],['Header 3','<h3>'],['Header 4','<h4>'],['Header 5','<h5>'],['Header 6','<h6>']],
				sl=styles.length, x=0;
				sel.className='testyle'; sel.onchange=new Function(this.n+'.ddaction(this,"formatblock")');
				for(x;x<sl;x++){
					var style=styles[x];
					sel.options[x]=new Option(style[0],style[1])
				}
				h.appendChild(sel)
			}else if(c[id]){
				var div=document.createElement('div'), x=c[id], func=x[2], ex, pos=x[0]*offset;
				div.className=obj.controlclass;
				div.style.backgroundPosition='0px '+pos+'px';
				div.title=x[1];
				ex=func=='a'?'.action("'+x[3]+'",0,'+(x[4]||0)+')':'.insert("'+x[4]+'","'+x[5]+'","'+x[3]+'")';
				div.onclick=new Function(this.n+(id=='print'?'.print()':ex));
				div.onmouseover=new Function(this.n+'.hover(this,'+pos+',1)');
				div.onmouseout=new Function(this.n+'.hover(this,'+pos+',0)');
				h.appendChild(div);
				if(this.ie){div.unselectable='on'}
			}
		}
		this.t.parentNode.insertBefore(p,this.t); this.t.style.width=this.i.width+'px';
		w.appendChild(this.t); w.appendChild(this.i); p.appendChild(w); this.t.style.display='none';
		if(obj.footer){
			var f=document.createElement('div'); f.className=obj.footerclass||'tefooter';
			if(obj.toggle){
				var to=obj.toggle, ts=document.createElement('div');
				ts.className=to.cssclass||'toggle'; ts.innerHTML=obj.toggletext||'代码';
				ts.onclick=new Function(this.n+'.toggle(0,this);return false');
				f.appendChild(ts)
			}
			if(obj.resize){
				var ro=obj.resize, rs=document.createElement('div'); rs.className=ro.cssclass||'resize';
				rs.onmousedown=new Function('event',this.n+'.resize(event);return false');
				rs.onselectstart=function(){return false};
				f.appendChild(rs)
			}
			p.appendChild(f)
		}
		this.e=this.i.contentWindow.document; this.e.open();
		var m='<html><head>', bodyid=obj.bodyid?" id=\""+obj.bodyid+"\"":"";
		uploadexc=obj.uploadexc;
		if(obj.cssfile){m+='<link rel="stylesheet" href="'+obj.cssfile+'" />'}
		if(obj.css){m+='<style type="text/css">'+obj.css+'</style>'}
		m+='</head><body'+bodyid+'>'+(obj.content||this.t.value);
		m+='</body></html>';
		this.e.write(m);
		this.e.close(); this.e.designMode='on'; this.d=1;
		if(this.xhtml){
			try{this.e.execCommand("styleWithCSS",0,0)}
			catch(e){try{this.e.execCommand("useCSS",0,1)}catch(e){}}
		}
	};
	edit.prototype.print=function(){
		this.i.contentWindow.print()
	},
	edit.prototype.hover=function(div,pos,dir){
		div.style.backgroundPosition=(dir?'34px ':'0px ')+(pos)+'px'
	},
	edit.prototype.ddaction=function(dd,a){
		var i=dd.selectedIndex, v=dd.options[i].value;
		//选择完毕，恢复
		dd.options[0].selected = true;
		this.action(a,v);
	},
	edit.prototype.action=function(cmd,val,ie){
		if(ie&&!this.ie){
			alert('您的浏览器不支持此项操作')
		}else{
			switch(cmd){
				case 'uploadfile':
					if(!window.open(uploadexc,'newwindow', 'height=200, width=350,toolbar=no, menubar=no, scrollbars=no,resizable=no,status=no,left=400,top=200')){
						alert('请禁用浏览器弹出窗口拦截或者同时按住键盘Ctrl和Alt按键，再点击上传按钮');};
				break;
				case 'forecolor':
				//alert(window.event);
					coloropen(this.e,cmd);
				break;
				case 'backcolor':
					coloropen(this.e,cmd);
				break;
				default:
					this.e.execCommand(cmd,0,val||null);
				break;
			}
			
		}
	},
	edit.prototype.insert=function(pro,msg,cmd){
		var val=prompt(pro,msg);
		if(val!=null&&val!=''){
			switch(cmd)
				{
				case 'insertswf':
					var swfdata='<embed src="'+val+'" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" wmode="opaque" width="480" height="400"></embed>';
					if(!-[1,]){
					ooo= this.e.selection.createRange();
					ooo.pasteHTML(swfdata);
					}else{
					this.e.execCommand("insertHTML",false,swfdata);
					}				 
				break
				case'insertmedia':
				var swfdata='<embed type="application/x-mplayer2" classid="clsid:6bf52a52-394a-11d3-b153-00c04f79faa6" src="'+val+'" enablecontextmenu="false" autostart="false" width="480" height="400" />';
					if(!-[1,]){
					ooo= this.e.selection.createRange();
					ooo.pasteHTML(swfdata);
					}else{
					this.e.execCommand("insertHTML",false,swfdata);
					}
				break;
			   default:
				 this.e.execCommand(cmd,0,val)
			   }		
		}
	},
	edit.prototype.setfont=function(){
		execCommand('formatblock',0,hType)
	},
	edit.prototype.resize=function(e){
		if(this.mv){this.freeze()}
		this.i.bcs=TINY.cursor.top(e);
		this.mv=new Function('event',this.n+'.move(event)');
		this.sr=new Function(this.n+'.freeze()');
		if(this.ie){
			document.attachEvent('onmousemove',this.mv); document.attachEvent('onmouseup',this.sr)
		}else{
			document.addEventListener('mousemove',this.mv,1); document.addEventListener('mouseup',this.sr,1)
		}
	},
	edit.prototype.move=function(e){
		var pos=TINY.cursor.top(e);
		this.i.height=parseInt(this.i.height)+pos-this.i.bcs;
		this.i.bcs=pos
	},
	edit.prototype.freeze=function(){
		if(this.ie){
			document.detachEvent('onmousemove',this.mv); document.detachEvent('onmouseup',this.sr)
		}else{
			document.removeEventListener('mousemove',this.mv,1); document.removeEventListener('mouseup',this.sr,1)
		}
	},
	edit.prototype.toggle=function(post,div){
		if(!this.d){
			var v=this.t.value;
			if(div){div.innerHTML=this.obj.toggletext||'代码'}
			if(this.xhtml&&!this.ie){
				v=v.replace(/<strong>(.*)<\/strong>/gi,'<span style="font-weight: bold;">$1</span>');
				v=v.replace(/<em>(.*)<\/em>/gi,'<span style="font-weight: italic;">$1</span>')
			}
			this.e.body.innerHTML=v;
			this.t.style.display='none'; this.i.style.display='block'; this.d=1
		}else{
			var v=this.e.body.innerHTML;
			if(this.xhtml){
				v=v.replace(/<span class="apple-style-span">(.*)<\/span>/gi,'$1');
				v=v.replace(/ class="apple-style-span"/gi,'');
				v=v.replace(/<span style="">/gi,'');
				v=v.replace(/<br>/gi,'<br />');
				v=v.replace(/<br ?\/?>$/gi,'');
				v=v.replace(/^<br ?\/?>/gi,'');
				v=v.replace(/(<img [^>]+[^\/])>/gi,'$1 />');
				v=v.replace(/<b\b[^>]*>(.*?)<\/b[^>]*>/gi,'<strong>$1</strong>');
				v=v.replace(/<i\b[^>]*>(.*?)<\/i[^>]*>/gi,'<em>$1</em>');
				v=v.replace(/<u\b[^>]*>(.*?)<\/u[^>]*>/gi,'<span style="text-decoration:underline">$1</span>');
				v=v.replace(/<(b|strong|em|i|u) style="font-weight: normal;?">(.*)<\/(b|strong|em|i|u)>/gi,'$2');
				v=v.replace(/<(b|strong|em|i|u) style="(.*)">(.*)<\/(b|strong|em|i|u)>/gi,'<span style="$2"><$4>$3</$4></span>');
				v=v.replace(/<span style="font-weight: normal;?">(.*)<\/span>/gi,'$1');
				v=v.replace(/<span style="font-weight: bold;?">(.*)<\/span>/gi,'<strong>$1</strong>');
				v=v.replace(/<span style="font-style: italic;?">(.*)<\/span>/gi,'<em>$1</em>');
				v=v.replace(/<span style="font-weight: bold;?">(.*)<\/span>|<b\b[^>]*>(.*?)<\/b[^>]*>/gi,'<strong>$1</strong>')
			}
			if(div){div.innerHTML=this.obj.toggletext||'设计'}
			this.t.value=v;
			if(!post){
				this.t.style.height=this.i.height+'px';
				this.i.style.display='none'; this.t.style.display='block'; this.d=0
			}
		}
	},
	edit.prototype.post=function(){
		if(this.d){this.toggle(1)}
	};
	return{edit:edit}
}();
//颜色选择器开始
document.write('<div id="colorpane" style=" border:2px solid gray;position:absolute;z-index:999;display:none;"></div> ');
var ColorHex=new Array('00','33','66','99','CC','FF');
var SpColorHex=new Array('FF0000','00FF00','0000FF','FFFF00','00FFFF','FF00FF');
var current=null;
function initcolor(evt) 
{ 
var colorTable='';
for (i=0;i<2;i++) 
{ 
for (j=0;j<6;j++) 
{ 
colorTable=colorTable+'<tr height=10>';
if (i==0){ 
colorTable=colorTable+'<td width=10 style="cursor:pointer;background-color:#'+ColorHex[j]+ColorHex[j]+ColorHex[j]+'"  onMouseover="changecolor(this.style.backgroundColor);" onClick="colorclose();">';} 
else{ 
	colorTable=colorTable+'<td width=10 style="cursor:pointer;background-color:#'+SpColorHex[j]+'"  onMouseover="changecolor(this.style.backgroundColor);" onClick="colorclose();">';}
	for (k=0;k<3;k++){
		for (l=0;l<6;l++){
			colorTable=colorTable+'<td width=10 style="cursor:pointer;background-color:#'+ColorHex[k+i*3]+ColorHex[l]+ColorHex[j]+'" onMouseover="changecolor(this.style.backgroundColor);" onClick="colorclose();">';
		}
	} 
} 
} 
colorTable='<div id="colorshow" style="background:#F2F2F2;text-align:center;" onClick="colorclose();">点击此处关闭[X]</div><table border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse" bordercolor="000000" style="cursor:pointer;">'+colorTable+'</table>'; 
T$("colorpane").innerHTML=colorTable; 
} 
function changecolor(obj){
if(colorswitch=='backcolor'&&navigator.userAgent.indexOf("Firefox")!=-1){
	editorobj.execCommand('hilitecolor',0,obj);
	return false;
}
T$('colorshow').innerHTML='点击关闭[X]';
editorobj.execCommand(colorswitch,0,obj);
} 
function colorclose(){
T$("colorpane").style.display = "none"; 
} 
function coloropen(obj,swit){
editorobj=obj;
colorswitch=swit;
T$("colorpane").style.left=bodyevent.clientX+"px";
T$("colorpane").style.top=bodyevent.clientY+"px";
T$("colorpane").style.display = "block";
}
//颜色选择器结束
TINY.cursor=function(){
	//js加载后先执行这个
	initcolor();
	window.document.onmousemove=function colorpanemove(evt){
		bodyevent=evt || window.event;
	}
	return{
		top:function(e){
			return T$$$()?window.event.clientY+document.documentElement.scrollTop+document.body.scrollTop:e.clientY+window.scrollY
		}
	
	}
}();

//document.getElementById("MyIFrame").contentDocument.getElementById("s").style.color="blue"; 