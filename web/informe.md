# Proyecto DBP
> AWQAQ es una marca de distintos tipos de productos que tienen que ver con el bienestar y la salud de la persona. 
En nuestro proyecto hicimos una plataforma web de estilo "E-commerce" para los productos de AWQAQ. 
Contamos con la posibilidad de registrar tus datos y poder ingresar en cualquier otra ocasión para realizar compras de cualquiera de nuestros 4 productos con los que contamos por el momento.
 Utilizamos los conocimientos del curso en todo momento para reaización del Proyecto, tuvimos algunas dificultades al comienzo al aprender a usar el Git Bash y al momento de entender el funcionamiento de las funciones que conectan la información otorgada por el cliente con el Servidor. La plataforma tiene un registro de los datos de compra pero no hay manera de realizar pago dentro de esta. Aun no tenemos los conocimientos suficientes como para implementar un metodo de pago dentro de la plataforma, por eso no se realizo en el proyecto.
 
 
 


#Integrantes
* Alejandro Mamani
* Antonio Salinas
* Julio Bonifaz

 
#Explicación Codigo
##Rutas a los HTML del Servidor
```python
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout',  methods = ["GET"])
def logout():
    session.clear()
    return render_template('index.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/hot')
def hot():
    return render_template('Hot.html')


@app.route('/tooth')
def tooth():
    return render_template('toothbrush.html')


@app.route('/index_log')
def index_log():
    return render_template('index_log.html')


@app.route('/sports')
def sports():
    return render_template('Sports.html')


@app.route('/kine')
def kinesio():
    return render_template('shop-single.html')


@app.route('/thanks')
def thanks():
    return render_template('thankyou.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')
```

##Clases
###Clase User
``` python
class User(connector.Manager.Base):
	__tablename__ = 'users'

	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	username = Column(String(20))
	email = Column(String(120))
	password = Column(String(60))
	address = Column(String(200))
	phone = Column(String(20))
```
Se crea la base de datos User para el SignUp y Login.

###Clase Shop
``` python
class Shop(connector.Manager.Base):
	__tablename__ = 'shops'

	id = Column(Integer,  Sequence('shop_id_seq'), primary_key=True)
	country = Column(String(30))
	city = Column(String(30))
	username = Column(String(30), ForeignKey('users.id'))
	address = Column(String(200), ForeignKey('users.id'))
	phone = Column(String(20), ForeignKey('users.id'))
	comment = Column(String(30))
	username_r = relationship(User, foreign_keys=[username])
	address_r = relationship(User, foreign_keys=[address])
	phone_r = relationship(User, foreign_keys=[phone])

```
Se crea la base de datos a traves del ORM con todos los datos del cliente para el momento de compra del producto.

###Clase Product
``` python
class Product(connector.Manager.Base):
	__tablename__ = 'products'
	id = Column(Integer,  Sequence('product_id_seq'), primary_key=True)
	itemName = Column(String(50))
	itemDescription = Column(String(300))
	itemPrice = Column(String(30))
```
Creación de Base de Datos del Producto a traves del ORM.

###Clase Carrito
``` python
class Carito (connector.Manager.Base):
	__tablename__ = 'Carito'
	id = Column(Integer, primary_key=True)
	producto_id = Column(Integer, nullable=False)
	cantidad = Column(Integer, nullable=False)
	user_id = Column(Integer, nullable=False)
```
Creación de Base de Datos del Carrito a traves del ORM.


##Funcionamiento SignUp/Login
### Formulario Sign Up
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
  
  Este codigo representa el formulario creado en el html para el SignUp.


###Funcion PostData para el SignUp

``` javascript
function postDataSignup(){
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
               alert(JSON.stringify(response));
            },
            error: function(response){
               alert(JSON.stringify(response));
            }
        });
    }
   ```
 Este JavaScript crea la relación Cliente-Servidor para el proceso de recolección de datos del cliente al momento de registrarse.
    


###Funcion getData para el Login

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


### Formulario Login 
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
Este html muestra el formulario para hacer el Login.

## Contacto
##HTML formulario Contacto
``` html
           <form id= "contact" name="contact" action="{{url_for('contact')}}" method="POST" class="item-3" onsubmit="return upload(); return false;">
             <div class="p-3 p-lg-5 border">

                <section>
                  <div class="form-group row">
                    <div class="col-md-6">
                      <label for="c_fname" class="text-black">Nombre <span class="text-danger">*</span></label>
                      <input type="text" class="form-control" id="c_fname" name="c_fname">
                    </div>
                    <div class="col-md-6">
                      <label for="c_lname" class="text-black">Apellido <span class="text-danger">*</span></label>
                      <input type="text" class="form-control" id="c_lname" name="c_lname">
                    </div>
                  </div>
                </section>

                <section>
                <div class="form-group row">
                  <div class="col-md-12">
                    <label for="c_email" class="text-black">Email <span class="text-danger">*</span></label>
                    <input type="email" class="form-control" id="c_email" name="c_email" placeholder="">
                  </div>
                </div>
                </section>

                <section>
                    <div class="form-group row">
                  <div class="col-md-12">
                    <label for="c_subject" class="text-black">Tema </label>
                    <input type="text" class="form-control" id="c_subject" name="c_subject">
                  </div>
                </div>
               </section>


                <div class="form-group row">
                  <div class="col-md-12">
                    <label for="c_message" class="text-black">Mensaje </label>
                    <textarea name="c_message" id="c_message" cols="30" rows="7" class="form-control"></textarea>
                  </div>
                </div>
                <div class="form-group row">
                  <div class="col-lg-12">
                    <input type="submit" class="btn btn-primary btn-lg btn-block" value="Enviar Mensaje">
                  </div>
                </div>
              </div>
           </form>
  ```
###HTML script Contacto
``` html
<script>
    // validation of user data
    var name = document.forms["contact"]["c_fname"];
    var lastname = document.forms["contact"]["c_lname"];
    var mail = document.forms["contact"]["c_email"];
    var subject = document.forms["contact"]["c_subject"];
    var message = document.forms["contact"]["c_message"];

    name.addEventListener("blur", validate);
    lastname.addEventListener("blur", validate);
    mail.addEventListener("blur", validate);
    subject.addEventListener("blur", validate);
    message.addEventListener("blur", validate);f

</script>
```
###Javascript Contacto
``` javascript
$(function(){
    var url = "http://127.0.0.1:5000/users";


    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "id",
            loadUrl: url ,
            insertUrl: url ,
            updateUrl: url ,
            deleteUrl: url ,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),
        editing: {
            allowUpdating: true,
            allowDeleting: true,
            allowAdding: true
        },
        remoteOperations: {
            sorting: true,
            paging: true
        },
        paging: {
            pageSize: 12
        },
        pager: {
            showPageSizeSelector: true,
            allowedPageSizes: [8, 12, 20]
        },
        columns: [{
            dataField: "id",
            dataType: "number",
            allowEditing: false
        }, {
            dataField: "c_fname"
        }, {
            dataField: "c_lname"
        }, {
            dataField: "c_email"
        }, {
            dataField: "c_subject"

        }, {
            dataField: "c_message"
        },],
    }).dxDataGrid("instance");
});


```

## Dificultades al momento de realizar el Proyecto.
* Crear la manera de almacenar información en el servidor propuesta por el cliente. Es decir hacer la conexión Server-Html-JavaScript para que el servidor pueda recibir la información.
* Encontrar una buena plantilla HTML de estilo E-Commerce que cuente con los estilos, fuentes e iconos necesarios para poder tener una plataforma web con el proposito de **venta de productos**.

## Contenido Exerno
1.  Shoppers - HTML Template 
https://colorlib.com/wp/template/shoppers/
