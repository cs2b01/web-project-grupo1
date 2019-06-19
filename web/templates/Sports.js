function item_send(){
$.ajax({
        var id_producto = $('#id_producto').val();
        var cantidad = $('#cantidad').val();
        var data = JSON.stringify({
                "id_producto": id_producto,
                "cantidad": cantidad
            });


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