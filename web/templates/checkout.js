function pay(){
        var country = $('#c_country').val();
        var name = $('#c_fname').val();
        var fullname = $('#c_lname').val();
        var address = $('#c_address').val();
        var city = $('#c_state_country').val();
        var email = $('#c_email_address').val();
        var phone = $('c_phone').val();
        var comment = $('c_order_notes').val();
        var data = JSON.stringify({
                "country": country,
                "city": city,
                "name": name,
                "fullname": fullname,
                "email": email,
                "address":address,
                 "phone": phone,
                "comment": comment
            });

        $.ajax({
            url:'/buy_checkout',
            type:'POST',
            contentType: 'application/json',
            data : data,
            dataType:'json',
            success: function(response){
              alert(JSON.stringify(response));
            },
            error: function(response){
              alert(JSON.stringify(response));
            }
        });
    }