//rut
function validarForm() {
    var rut = document.forms["formulario"]["rut"].value;
    if (rut.length == 10) {
        document.getElementById("rut").style.border = "solid 2px green";
        document.getElementById("alert-rut").style.visibility = "hidden";
    } else {
        document.getElementById("alert-rut").style.visibility = "visible";
        document.getElementById("rut").style.border = "solid 2px red";
        return false;
    }

};

function validarRut(rut) {
    var b = new Boolean(true);
    var valor = rut.value.replace('.', '');
    valor = valor.replace('-', '');
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();
    rut.value = cuerpo + '-' + dv;

    if (cuerpo.length < 7) {
        document.getElementById("alert-rut").style.visibility = "visible";
        document.getElementById("rut").style.border = "solid 2px red";
        b = true;
        return false;

    } else {
        document.getElementById("alert-rut").style.visibility = "hidden";
        document.getElementById("rut").style.border = ""
        b = false;

    };
    suma = 0;
    multiplo = 2;

    for (i = 1; i <= cuerpo.length; i++) {
        index = multiplo * valor.charAt(cuerpo.length - i);
        suma = suma + index;
        if (multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }

    }
    dvEsperado = 11 - (suma % 11);
    dv = (dv == 'K') ? 10 : dv;
    dv = (dv == 0) ? 11 : dv;
    if (dvEsperado != dv) {
        document.getElementById("alert-rut").style.visibility = "visible";
        document.getElementById("rut").style.border = "solid 2px red";
        b = true;
        return false;
    };
    console.log(b);
    rut.setCustomValidity('');
}

function confirmacion() {
    var estado = validarRut(rut);
    if (estado == true) {
        document.getElementById("btnvalida").addEventListener("click", function (evt) {
            evt.preventDefault()
        });
    }

}
//rut

//password
function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

$(document).ready(function validarPassword() {
    $("#btnvalida").on("click", function () {
        var rut = document.forms["formulario"]["rut"].value;
        if (rut.length == 10) {
            document.getElementById("rut").style.border = "solid 2px green";
            document.getElementById("alert-rut").style.visibility = "hidden";
        } else {
            document.getElementById("alert-rut").style.visibility = "visible";
            document.getElementById("rut").style.border = "solid 2px red";
            return false;
        }

        var password1 = $("#password").val();
        
        if (password1.length < 6 || password1.length > 12) {
            $("#password").css({
                "border": "solid 2px red"

            });
            $("#alert-pass1").css({
                "visibility": "visible",

            })

            event.preventDefault();
        } else {
            $("#alert-pass1").css({
                "visibility": "hidden"
            });
        };

    });

});


//jsmoneda
$(document).ready(function () {
    $.getJSON('https://mindicador.cl/api', function (data) {
        var indicadores = data;
        $("#dolar").text("Dolar: $"+indicadores.dolar.valor)
    }).fail(function () {
        console.log('Error al consumir la API!');
    });
})

$(document).ready(function () {
    $.getJSON('https://mindicador.cl/api', function (data) {
        var indicadores = data;
        $("#euro").text("Euro: €"+indicadores.euro.valor)
    }).fail(function () {
        console.log('Error al consumir la API!');
    });
})
//js_moneda