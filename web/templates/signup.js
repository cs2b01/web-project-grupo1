function postDataSignup(){
        var username = $('#username').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var address = $('#address').val();
        var address = $('#phone').val();
        var register = JSON.stringify({
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
            data : register,
            dataType:'json',
            success: function(response){
               alert(JSON.stringify(response)
            },
            error: function(response){
               alert(JSON.stringify(response));
            }
        });
    }
