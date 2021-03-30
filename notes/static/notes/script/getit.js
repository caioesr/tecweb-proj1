function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {

  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});

document.querySelectorAll("p").forEach(function(node){
  node.ondblclick=function(){
      var val=this.innerHTML;
      var input=document.createElement("input");
      input.value=val;
      input.onblur=function(){
          var val=this.value;
          this.parentNode.innerHTML=val;
      }
      this.innerHTML="";
      this.appendChild(input);
      input.focus();
  }
});

document.querySelectorAll("h3").forEach(function(node){
  node.ondblclick=function(){
      var val=this.innerHTML;
      var input=document.createElement("input");
      input.value=val;
      input.onblur=function(){
          var val=this.value;
          this.parentNode.innerHTML=val;
      }
      this.innerHTML="";
      this.appendChild(input);
      input.focus();
  }
});

function updateValues(btn){
  var forms = btn.parentElement.parentElement.parentElement;
  var old_title = forms.children[1].children[1];
  var new_title = forms.children[1].children[2];
  var old_details =forms.children[2].children[0];
  var new_details = forms.children[2].children[1];

  var old_input_title = document.createElement("input");
  var old_input_details = document.createElement("input");

  old_input_title.value = old_title.value;
  old_input_title.name = "old_title";
  old_input_details.value = old_details.value;
  old_input_details.name = "old_details";
  old_input_title.setAttribute("type","hidden");
  old_input_details.setAttribute("type","hidden");

  forms.appendChild(old_input_title);
  forms.appendChild(old_input_details);

  old_title.value = new_title.innerHTML;
  old_details.value = new_details.innerHTML;
}