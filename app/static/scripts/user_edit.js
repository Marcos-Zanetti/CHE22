let cajaId = document.getElementById("id");
let cajaNick = document.getElementById("username");
let cajaMail = document.getElementById("email");
let btn = document.getElementById("submit");
cajaId.style.display = "none";
cajaNick.style.display = "none";
cajaMail.style.display = "none";
btn.style.display = "none";
let selector = document.getElementById('selector');
selector.onclick = function () {
    let choice = selector.value;
    if (choice == "id") {
        btn.style.display = "block";
        cajaId.style.display = "block";
        cajaNick.style.display = "none";
        cajaMail.style.display = "none";
    } else if (choice == "username") {
        btn.style.display = "block";
        cajaId.style.display = "none";
        cajaNick.style.display = "block";
        cajaMail.style.display = "none";
    } else if (choice == "email") {
        btn.style.display = "block";
        cajaId.style.display = "none";
        cajaNick.style.display = "none";
        cajaMail.style.display = "block";
    }
}