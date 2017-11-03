$(document).ready(init());

function init(){
	setInterval(function(){refresh_pre_order()},3000);
}

function refresh_pre_order(){
	console.log('Refresh Pre Order');
    $.ajax({
		url:  "/preorder/products",
		dataType: "json",
		data: {},
		success: function(trans) {
            strproductbox = '';
		    for (var i = 0; i <trans.length; i++){
                var obj = trans[i];
                if (i == 0){
                    document.getElementById("product01-name").innerHTML = obj['product_id'][1];
                }
                if (i == 1){
                    document.getElementById("product02-name").innerHTML = obj['product_id'][1];
                }
            }
		},
		fail: function(msg){
		            console.log('error');
		},
		done: function(){
		            console.log('done');
		}
	});
}