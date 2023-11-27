var btnSignin = document.querySelector("#signin");
var btnSignup = document.querySelector("#signup");

var body = document.querySelector("body");

btnSignin.addEventListener("click", function () {
  body.className = "sign-in-js";
});

btnSignup.addEventListener("click", function () {
  body.className = "sign-up-js";
});


/* function validateAndRegister() {
  // Obtenha os valores dos campos
  var nome = $("#name").val();
  var email = $("#email").val();
  var senha = $("#password").val();

  // Faça a validação, por exemplo, verificar se os campos estão preenchidos
  if (!nome || !email || !senha) {
    alert("Todos os campos são obrigatórios. Preencha todos os campos.");
    return;
  }

  // Obtenha o token CSRF
  var csrf_token = $("[name=csrfmiddlewaretoken]").val();

  // Configurar o cabeçalho da solicitação AJAX
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": csrf_token,
    },
  });

  // Faça a requisição Ajax para cadastrar o usuário
  $.ajax({
    type: "POST",
    url: "/cadastrar_usuario/", // Substitua pelo URL correto da sua view de cadastro
    data: {
      nome: nome,
      email: email,
      senha: senha,
    },
    success: function (response) {
      alert("Usuário cadastrado com sucesso!");
      // Adicione aqui qualquer outra ação desejada após o cadastro bem-sucedido
    },
    error: function (error) {
      alert("Erro ao cadastrar usuário. Tente novamente.");
      console.log(error);
    },
  });
} */
