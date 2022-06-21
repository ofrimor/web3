var i = 0;
var j=0;
var txt = 'YES! we are happy';
var txtt = 'Happy to meet you!';
var speed = 50;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  
  }
}


function typeWriter2() {
    if (i < txtt.length) {
      document.getElementById("demo2").innerHTML += txtt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    
    }
  }
  


  //print date to log
const d = Date();
console.log(d);

//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});

