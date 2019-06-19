var currentUserId = 0;
var currentClickedId = 0;
function whoami(){
        $.ajax({
            url:'/current',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                //alert(JSON.stringify(response));
                $('#cu_username').html(response['id'])
            },
            error: function(response){
                alert(JSON.stringify(response));
            }
        });
    }




function item_send(){

        var id_producto = $('#id_producto').val();
        var cantidad = $('#cantidad').val();
        var username = $('#username').val();
        var data = JSON.stringify({
                "id_producto": id_producto,
                "cantidad": cantidad,
                "username": username,
            });

$.ajax({
            url:'/item_send',
            type:'POST',
            contentType: 'application/json',
            data : data,
            dataType:'json',
            success: function(response){
                $('#action').html(response['statusText']);
            },
            error: function(response){
                alert(JSON.stringify(response));
                if(response['status']==401){
                    $('#loading').hide();
                    $('#fail').show()
                }else{
                    $('#loading').hide();
                    $('#ok').show()
                }
            }
        });
}