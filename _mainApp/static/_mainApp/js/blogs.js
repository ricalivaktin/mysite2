div = document.getElementById("demo-div")
// #############
div.innerHTML += "<p class='alert alert-primary p-3 m-2 fw-bold text-center'>Bu Tablo 5 saniye sonra SİLİNECEK</p>"
setTimeout(function(){
    div.innerHTML = "<div></div>";
},5000)