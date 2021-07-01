function soloLetras(e) {
    var key = e.keyCode || e.which,
        tecla = String.fromCharCode(key).toLowerCase(),
        letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",
        especiales = [8, 37, 39, 46],
        tecla_especial = false;

    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        };
    };
    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    };
};

function soloNumeros(e) {
    var key = e.keyCode || e.which,
        tecla = String.fromCharCode(key).toLowerCase(),
        letras = "0123456789",
        especiales = [8, 37, 39, 46],
        tecla_especial = false;
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
    var input = document.getElementById('celular');
    input.addEventListener('input', function () {
        if (this.value.length > 12) {
            this.value = this.value.slice(0, 12);
        };
    })
    var tel = celular.value.slice(4, 12)
    celular.value = '+569' + tel;
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
        document.getElementById("siguiente").addEventListener("click", function (evt) {
            evt.preventDefault()
        });
    };
}

function validarFormulario() {
    var rut = document.forms["formulario"]["run"].value;
    var nombre = document.forms["formulario"]["nombre"].value;
    var paterno = document.forms["formulario"]["paterno"].value;
    var materno = document.forms["formulario"]["materno"].value;
    var email = document.forms["formulario"]["email"].value;
    var celular = document.forms["formulario"]["celular"].value;
    var ciudad = document.forms["formulario"]["ciudad"].value;
    var comuna = document.forms["formulario"]["comuna"].value;
    var direccion = document.forms["formulario"]["direccion"].value;
    var numero = document.forms["formulario"]["numeracion"].value;

    //Confirmacion Rut
    if (rut.length == 10) {
        document.getElementById("rut").style.border = "solid 2px green";
        document.getElementById("alert-rut").style.visibility = "hidden";
    } else {
        document.getElementById("alert-rut").style.visibility = "visible";
        document.getElementById("rut").style.border = "solid 2px red";
        return false;
    };

    //Confirmacion Nombre
    if (nombre == "") {
        document.getElementById("alert-nombre").style.visibility = "visible";
        document.getElementById("nombre").style.border = "solid 2px red";
        return false;
    } else {
        document.getElementById("nombre").style.border = "solid 2px green";
        document.getElementById("alert-nombre").style.visibility = "hidden";
    };

    //Confirmacion Apellidos
    if (paterno == "" || materno == "") {
        document.getElementById("alert-p").style.visibility = "visible";
        document.getElementById("alert-m").style.visibility = "visible";
        document.getElementById("paterno").style.border = "solid 2px red";
        document.getElementById("materno").style.border = "solid 2px red";
        return false
    } else {
        document.getElementById("paterno").style.border = "solid 2px green";
        document.getElementById("materno").style.border = "solid 2px green"
        document.getElementById("alert-p").style.visibility = "hidden";
        document.getElementById("alert-m").style.visibility = "hidden";
    };

    //Confirmacion Email
    if (email == "") {
        document.getElementById("alert-email").style.visibility = "visible";
        document.getElementById("email").style.border = "solid 2px red";
        return false;
    } else {
        document.getElementById("email").style.border = "solid 2px green";
        document.getElementById("alert-email").style.visibility = "hidden";
    };

    //Confirmacion Celular
    if (celular.length == 12) {
        document.getElementById("celular").style.border = "solid 2px green";
        document.getElementById("alert-celular").style.visibility = "hidden";

    } else {
        document.getElementById("alert-celular").style.visibility = "visible";
        document.getElementById("celular").style.border = "solid 2px red";
        return false;
    };

    //Confirmacion Ciudad
    if (ciudad == "") {
        document.getElementById("alert-ciu").style.visibility = "visible";
        document.getElementById("ciudad").style.border = "solid 2px red";
        return false;

    } else {
        document.getElementById("ciudad").style.border = "solid 2px green";
        document.getElementById("alert-ciu").style.visibility = "hidden";

    };

    //Confirmacion Comuna
    if (comuna == "") {
        document.getElementById("alert-comuna").style.visibility = "visible";
        document.getElementById("comuna").style.border = "solid 2px red";
        return false;
    } else {
        document.getElementById("comuna").style.border = "solid 2px green";
        document.getElementById("alert-comuna").style.visibility = "hidden";
    };

    //Confirmacion Direccion
    if (direccion == "") {
        document.getElementById("alert-direc").style.visibility = "visible";
        document.getElementById("direccion").style.border = "solid 2px red";
        return false;
    } else {
        document.getElementById("direccion").style.border = "solid 2px green";
        document.getElementById("alert-direc").style.visibility = "hidden";
    };

    //Confirmacion Numeracion
    if (numero < 1) {
        document.getElementById("alert-num").style.visibility = "visible";
        document.getElementById("numeracion").style.border = "solid 2px red";
        return false;
    } else {
        document.getElementById("numeracion").style.border = "solid 2px green";
        document.getElementById("alert-num").style.visibility = "hidden";

    };

};


$(document).ready(function () {
    $("#siguiente").on("click", function () {
        var condiciones = $("#termino").is(":checked");
        var rut = confirmacion();
        if (!condiciones) {
            $("#alert-term").css({
                "visibility": "visible"
            })
            event.preventDefault();
        } else {
            $("#alert-term").css({
                "visibility": "hidden"
            })
        };
        if (rut == true) {
            event.preventDefault();
        };
    });
    
    /* Nombre */
    $("#nombre").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#nombre").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Apellido Paterno */
    $("#paterno").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#paterno").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });
    /* Apellido Materno */
    $("#materno").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#materno").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Rut */
    $("#rut").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#rut").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Email */
    $("#email").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#email").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Celular */
    $("#celular").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#celular").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Ciudad */
    $("#ciudad").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#ciudad").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Comuna */
    $("#comuna").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#comuna").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Calle */
    $("#direccion").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#direccion").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });

    /* Numeracion */
    $("#numeracion").on("mouseover", function () {
        $(this).css({
            "background-color": "#f6d1de"
        });
    });
    $("#numeracion").on("mouseleave", function () {
        $(this).css({
            "background-color": ""
        });
    });
    /* Registro */
    $("#registro").on("mouseover", function () {
        $(this).css({
            "box-shadow":"0 0 30px rgb(0,0,0,0.568)"
        });
    });
    $("#registro").on("mouseleave", function () {
        $(this).css({
            "box-shadow": ""
        });
    });

});