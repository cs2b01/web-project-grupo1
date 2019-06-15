# Proyecto DBP
> AWQAQ es una marca de distintos tipos de productos que tienen que ver con el bienestar y la salud de la persona. 
En nuestro proyecto hicimos una plataforma web de estilo "E-commerce" para los productos de AWQAQ. 
Contamos con la posibilidad de registrar tus datos y poder ingresar en cualquier otra ocasión para realizar compras de cualquiera de nuestros 4 productos con los que contamos por el momento.
 Utilizamos los conocimientos del curso en todo momento para reaización del Proyecto, tuvimos algunas dificultades al comienzo al aprender a usar el Git Bash y al momento de entender el funcionamiento de las funciones que conectan la información otorgada por el cliente con el Servidor. La plataforma tiene un registro de los datos de compra pero no hay manera de realizar pago dentro de esta. Aun no tenemos los conocimientos suficientes como para implementar un metodo de pago dentro de la plataforma, por eso no se realizo en el proyecto.
 
 
 


#Integrantes
* Alejandro Mamani
* Antonio Salinas
* Julio Bonifaz

 
## Explicación Codigo

#### Funcion getData para SignUp
``` javascript
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
```

Esta función recoge todos los valores ingresados por el cliente al momento de hacer el SignUp, los convierte en un STRING en formato JSON, haciendo posible al servidor recibir esta informacion y almacenarla para luego poder ingresar a la plataforma e ingresar sin necesidad de registrarse nuevamente.


#Funcion getData para el Login

``` javascript
function getData(){
        $('#fail').hide();
        $('#ok').hide()
        $('#loading').show();
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
                    $('#loading').hide();
                    $('#fail').show()
                }else{
                    $('#loading').hide();
                    $('#ok').show()
                }
            }
        });
    }
```

Esta función comprueba si el usuario y contraseña ingresados por el cliente se encuentran en la base de datos a traves de la función **Authenticate**. El servidor comprueba si es que existen y luego manda una respuesta('Success' o 'Error').


#### Función Authenticate SignUp
``` python
def authenticate_signup():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    email = message ['email'],
    address = message['address'],
    phone = message['phone']
    db_session = db.getSession(engine)

    try:
        user = db_session.query(db_models.User).filter(db_models.User.username == username
                                 ).filter(db_models.User.password == password
                                ).filter(db_models.User.email == email
                                         ).filter(db_models.User.address == address
                                                  ).filter(db_models.User.phone == phone
                                                           ).one()
        session['logged_user'] = user.id
        message = {'message': 'USTED YA ESTA REGISTRADO'}
        return render_template("login.html")

    except Exception:
        message = {'message': 'GRACIAS'}
        return Response(status=200, mimetype='application/json')
```
# Formulario LOGIN 
``` html
<table style="margin: 0 auto;">
        <tr>
            <td>Username</td>
            <td><input type="text" name="username" id="username"/></td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password" id="password" /></td>
        </tr>
        <tr>
            <td colspan="2">
                <input type="button" value="login" onclick="getData()"/>
            </td>
        </tr>
        <tr>
            <td >
                <div id="action"></div>

            </td>
        </tr>
    </table>
```

# Formulario Sign Up
``` html
 <table style="margin: 0 auto;">
        <tr>
            <td>Username</td>
            <td><input type="text" name="username" id="username"/></td>
        </tr>
         <tr>
            <td>Email</td>
            <td><input type="text" name="email" id="email"/></td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password" id="password" /></td>
        </tr>
         <tr>
            <td>Address</td>
            <td><input type="text" name="address" id="address" /></td>
        </tr>
        <tr>
            <td>Phone</td>
            <td><input type="text" name="phone" id="phone" /></td>
        </tr>

        <tr>
            <td colspan="2">
                <input type="button" value="login" onclick="getData()"/>
            </td>
        </tr>
        <tr>
            <td >
                <div id="action"></div>

            </td>
        </tr>
    </table>
  ```

## Dificultades al momento de realizar el Proyecto.
* Crear la manera de almacenar información en el servidor propuesta por el cliente. Es decir hacer la conexión Server-Html-JavaScript para que el servidor pueda recibir la información.
* Encontrar una buena plantilla HTML de estilo E-Commerce que cuente con los estilos, fuentes e iconos necesarios para poder tener una plataforma web con el proposito de **venta de productos**.

## Contenido Exerno
1.  Shoppers - HTML Template 
https://colorlib.com/wp/template/shoppers/
