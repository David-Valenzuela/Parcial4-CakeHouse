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
        letras = " +0123456789",
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

    var input = document.getElementById('ccnum');
    input.addEventListener('input', function () {
        if (this.value.length > 16) {
            this.value = this.value.slice(0, 16);
        };
    })

    var input = document.getElementById('expmonth');
    input.addEventListener('input', function () {
        if (this.value.length > 2) {
            this.value = this.value.slice(0, 2);
        };
    })

    var input = document.getElementById('expyear');
    input.addEventListener('input', function () {
        if (this.value.length > 4) {
            this.value = this.value.slice(0, 4);
        };
    })

    var input = document.getElementById('cvv');
    input.addEventListener('input', function () {
        if (this.value.length > 3) {
            this.value = this.value.slice(0, 3);
        };
    })

};


function validar() {
    var nombre = document.forms["formulario"]["nombre"].value;
    var apellido = document.forms["formulario"]["paterno"].value;
    var materno = document.forms["formulario"]["materno"].value;
    var email = document.forms["formulario"]["email"].value;
    var direc = document.forms["formulario"]["direccion"].value;
    var number = document.forms["formulario"]["num"].value;
    var cel = document.forms["formulario"]["celular"].value;
    var name = document.forms["formulario"]["name"].value;
    var tarj = document.forms["formulario"]["cardnumber"].value;
    var mes = document.forms["formulario"]["expmonth"].value;
    var year = document.forms["formulario"]["expyear"].value;
    var cvv = document.forms["formulario"]["cvv"].value;


    if (nombre == "") {
        document.getElementById("a-nombre").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-nombre").style.visibility = "hidden";
    };

    if (apellido == "") {
        document.getElementById("a-apellido").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-apellido").style.visibility = "hidden";
    };
    if (materno == "") {
        document.getElementById("m-apellido").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("m-apellido").style.visibility = "hidden";
    };
    if (direc == "") {
        document.getElementById("a-direc").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-direc").style.visibility = "hidden";
    };
    if (number < 1) {
        document.getElementById("a-num").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-num").style.visibility = "hidden";
    };
    if (cel.length != 12) {
        document.getElementById("a-celular").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-celular").style.visibility = "hidden";
    };
    if (name == "") {
        document.getElementById("a-name").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-name").style.visibility = "hidden";
    };
    if (email == "") {
        document.getElementById("a-email").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-email").style.visibility = "hidden";
    };
    if (tarj.length == 16) {
        document.getElementById("a-tarj").style.visibility = "hidden";

    } else {
        document.getElementById("a-tarj").style.visibility = "visible";
        return false;
    };
    if (mes < 1 || mes > 12) {
        document.getElementById("a-mes").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-mes").style.visibility = "hidden";
    };
    if (year.length != 4) {
        document.getElementById("a-year").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-year").style.visibility = "hidden";
    };
    if (cvv.length != 3) {
        document.getElementById("a-cvv").style.visibility = "visible";
        return false;
    } else {
        document.getElementById("a-cvv").style.visibility = "hidden";
    };
    alert("¡Pago realizado con éxito!")
}


$(document).ready(function () {
     
    $("#producto").on("mouseover", function () {
      $(this).css({
        "box-shadow": "0 0 30px rgb(0,0,0,0.568)"
      });
    });
    $("#producto").on("mouseleave", function () {
      $(this).css({
        "box-shadow": ""
      });
    });
  });
