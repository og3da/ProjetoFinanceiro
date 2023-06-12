const name = document.getElementById('name');
const button = document.getElementById('botao');
const email = document.getElementById('email');
const tel = document.getElementById('tel');
const comments = document.getElementById('comments');

$(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
  
      var winTop = $(window).scrollTop();
      if (pos < winTop + 600) {
        $(this).addClass("slide");
      }
    });
  });

$(document).ready(function(){
    $(".navbar a, footer a[href='#myPage'], a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;

      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){

        window.location.hash = hash;
        });
      } 
    });
})

function emailValidator(email) {
    let emailPattern =
    /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/;
    return emailPattern.test(email);
}

const phoneValidator = (tel) => {
    const telefoneRegex = /^\(\d{2}\) \d{4,5}-\d{4}$/gi;
    return telefoneRegex.test(tel);
};

button.addEventListener('click', (event) => {
    event.preventDefault()
    if(name.value && email.value && comments.value && tel.value != "") {       
        if(emailValidator(email.value) != true) {
        alert("digite um email valido Ex: email@gmail.com")
        }
        else if(phoneValidator(tel.value) != true){
        alert('digite um telefone valido \n Exemplo: \n (41) 9218-2419; (41) 9128-2374; \n (411) 97258-2664')
        }
        else {
        alert('enviado!')
        }
    }
    else {
        alert('mensagem não enviada \n preencha todos os campos!')
    }
})
