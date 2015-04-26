var TONGJI_DEBUG = false;
var TONGJI_BASE_URL = "http://www.weixiaoxin.cn";

var TONGJI = [
		{name:'view', url : TONGJI_BASE_URL+"/WxTongji/view?", params : {action:'', target_id:0}},
		{name:'follow', url : TONGJI_BASE_URL+"/WxTongji/follow?", params : {wid:0, wghname:''}},
		{name:'pageview', url : TONGJI_BASE_URL+"/WxTongji/pageview?", params : {source:0, target_id:0}},
		{name:'static_follow', url : TONGJI_BASE_URL+"/WxTongji/count?", params : {wid:0, wxname:''}},
		{name:'static_pageview', url : TONGJI_BASE_URL+"/WxTongji/count?", params : {uid:0, post_id:0, key:'', title:''}}
];

function DEBUG(object){
	if(TONGJI_DEBUG)
	console.log(object);
}

function follow(b, url){
	if(TONGJI_DEBUG)
	new Image().src = url+"&action=suc_follow";
	else
	WeixinJSBridge.invoke(
		'addContact',
		{"webtype": "1","username": b}, 
		function(a) {
			if (a.err_msg == 'add_contact:ok') {
				new Image().src = url+"&action=suc_follow";
				
				//关注成功
			} else if(a.err_msg != 'add_contact:added'){
				new Image().src = url+"&action=err_follow";
			}
		}
	);
}

function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}

function getParams(obj, object){
	var param_array = [];					
	for(attr_name in object.params){
		var value = $(obj).attr(attr_name);
		if(typeof(value) == undefined) continue;
		param_array.push(attr_name+"="+value);
	}
	
	return param_array.join('&');
}

$(document).ready(function(){
	$(TONGJI).each(function(key, object){
		DEBUG(object);
		var action_name = object.name;
		
		switch(action_name){
			case 'follow':
				if(TONGJI_DEBUG || typeof(WeixinJSBridge) != 'undefined')
				$("*[action-name="+action_name+"]").bind('click.'+action_name, function(){
					follow($(this).attr('wghname'), object.url + getParams($(this), object));
				});
			break;
			
			case 'view':
				$("*[action-name="+action_name+"]").bind('click.'+action_name, function(){
					var param_array = [];
					for(attr_name in object.params){
						var value = $(this).attr(attr_name);
						if(typeof(value) == undefined) break;
						param_array.push(attr_name+"="+value);
					}					
					new Image().src = object.url + param_array.join('&');
				});
			break;
			
			case 'pageview':
				var source = 0;
				var target_id=0;
				
				if(location.href.match(/wxnavs.html/)) {
					source = 1;
					target_id = UID;	
				}
				
				if(location.href.match(/_mini.html/)) {
					source = 2;
					target_id = WID;
				}
				if(location.href.match(/cateshow/)) {
					source = 2;
					target_id = WID;
				}
				if(target_id==0) break;		
				new Image().src = object.url + "source="+source+"&target_id="+target_id;
			break;
			
			case 'static_pageview':
				if("undefined" != typeof(IS_STATIC) && IS_STATIC){
					var params = "uid="+_uid+"&post_id="+_post_id+"&key="+_key+"&title="+_title;
					
					if(getQueryString('ret') == 1)
					new Image().src = object.url + "action=ret_share&" + params;
					else
					new Image().src = object.url + "action=views&" + params;
				}
			break;
			
			case 'static_follow':
				$("*[action-name="+action_name+"]").bind('click', function(){
					var params = "uid="+_uid+"&post_id="+_post_id+"&key="+_key+"&title="+_title;
					follow($(this).attr('wname'), object.url + params + "&" + getParams($(this), object));
				});
			break;
		}
	});
});