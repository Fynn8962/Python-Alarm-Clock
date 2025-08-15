

var i = 0;
var speed = 50;
var headerName = document.getElementById("name");
var textName = headerName.innerHTML;
headerName.innerHTML = "";

function typeName(callback) {
    if (i < textName.length) {
      headerName.innerHTML += textName.charAt(i);
      i++;
      setTimeout(() => typeName(callback), speed);
    } else if (callback) {
        callback();
    }
  }

var j = 0;
speedPhrase = 40;
var headerPhrase = document.getElementById("phrase");
var textPhrase = headerPhrase.innerHTML;
headerPhrase.innerHTML = "";


function typePhrase() {
    if (j < textPhrase.length) {
      headerPhrase.innerHTML += textPhrase.charAt(j);
      j++;
      setTimeout(typePhrase, speedPhrase);
    } 
}

window.onload = function() {

  setTimeout(function() {
    typeName(typePhrase); 
  }, 500);
  };



  var buttonTop = document.getElementById("buttonTop")
  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      buttonTop.style.display = "block";
      
    }
    else {
      buttonTop.style.display = "none";
    }
  }

  function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
  
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');

    const button = document.getElementById('darkModeButton');
    if (document.body.classList.contains('dark-mode')) {
      button.textContent = 'Light Mode';
    } else {
      button.textContent = 'Dark Mode';
    }
  }