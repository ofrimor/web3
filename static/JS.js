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
  


