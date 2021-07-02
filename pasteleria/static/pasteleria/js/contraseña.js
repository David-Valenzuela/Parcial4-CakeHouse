/* Funcion Mostrar y ocultar Contraseña */
function myFunction() {
  var x = document.getElementById("password");
  var y = document.getElementById("password2");
  if (y.type === "password") {
    y.type = "text";
  }
  else {
    y.type = "password";
  } 
  if (x.type === "password") {
      x.type = "text";
  } else {
      x.type = "password";
  }
  
} 

/*Validacion Constraseña*/
$(document).ready(function () {
  $("#siguiente").on("click", function () {
      var password1 = $("#password").val();
      var password2 = $("#password2").val();

      if (password1.length < 6 || password1.length > 12) {
          $("#password").css({
              "border": "solid 1px red"

          });
          $("#alert-pass1").css({
              "visibility": "visible"
          })
          $("#alert-pass1").text("Su contraseña debe poseer entre 6 y 12 caracteres.")
          event.preventDefault();
      } else {
        $("#password").css({
          "border": "solid 1px green"

        });  
        $("#alert-pass1").css({
              "visibility": "hidden"
          });
      };



      if (password2 != password1) {
          $("#password2").css({
              "border": "solid 1px red"

          });
          $("#alert-pass2").css({
              "visibility": "visible"
          })
          $("#alert-pass2").text("Las constraseñas no coinciden.")
          event.preventDefault();
      } else {
        $("#password").css({
          "border": "solid 1px red"

        });  
        $("#alert-pass2").css({
              "visibility": "hidden"
          });
      };

      /* Registro */
      $("#register-form").on("mouseover", function () {
          $(this).css({
              "box-shadow": "0 0 30px rgb(0,0,0,0.568)"
          });
      });
      $("#register-form").on("mouseleave", function () {
          $(this).css({
              "box-shadow": ""
          });
      });

  });
});




/* Registro */
$("#register-form").on("mouseover", function () {
  $(this).css({
      "box-shadow":"0 0 30px rgb(0,0,0,0.568)"
  });
});
$("#register-form").on("mouseleave", function () {
  $(this).css({
      "box-shadow": ""
  });
});

