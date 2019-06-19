function getData(){
        $('#try').hide();
        $('#HOLA').hide()

        var username = $('#username').val();
        var password = $('#password').val();
        var message = JSON.stringify({
                "username": username,
                "password": password
            });

        $.ajax({
            url:'/authenticate',
            type:'POST',
            contentType: 'application/json',
            data : message,
            dataType:'json',
            success: function(response){
                //$('#action').html(response['statusText']);
            },
            error: function(response){
                //alert(JSON.stringify(response));
                if(response['status']==401){

                    $('#try').show()
                }else{

                    $('#HOLA').show()
                }
            }
        });
    }