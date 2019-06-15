function getData(){
        $('#fail').hide();
        $('#ok').hide()
        $('#loading').show();
        var username = $('#username').val();
         var email = $('#email').val();
        var password = $('#password').val();
        var address = $('#address').val();
        var address = $('#phone').val();
        var message = JSON.stringify({
                "username": username,
                "email": email,
                "password": password,
                "address": address,
                "phone": phone
            });

        $.ajax({
            url:'/signup',
            type:'POST',
            contentType: 'application/json',
            data : message,
            dataType:'json',
            success: function(response){
                $('#action').html(response['AHORA ERES PARTE DE NUESTRA COMUNIDAD']);
            },
            error: function(response){
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