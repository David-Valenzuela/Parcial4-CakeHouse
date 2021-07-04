function unidad() {
    var und = document.forms["pastel"]["und"].value;

    if (und < 1 || und > 10) {
        document.getElementById("alerta").style.visibility = "visible";
        document.getElementById("und").style.border = "solid 2px red";
        return false;
    } else {
        document.getElementById("alerta").style.visibility = "hidden";
        document.getElementById("und").style.border = "";
    };
}

$(document).ready(function () {
    /* Registro*/
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
    /*Producto*/
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