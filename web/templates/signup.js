function postDataSignup(){
        $('#fail').hide();
        $('#ok').hide()
        $('#loading').show();
        var username = $('#username').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var address = $('#address').val();
        var phone = $('#phone').val();
        var data = JSON.stringify({
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
            data : data,
            dataType:'json',
            success: function(response){
               //alert(JSON.stringify(response));
            },
            error: function(response){
             if(response['status']==401){
                    $('#loading').hide();
                    $('#fail').show()
                }else{
                    $('#loading').hide();
                    $('#ok').show()
                }
              // alert(JSON.stringify(response));

            }
        });
    }
