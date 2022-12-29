const sources = [];
const titles = [];
const authors = [];
const dates = [];
const links = [];
var table_length = 0;
var style_count = 10;

// Read CSV & Write on Page
async function getData() {
  const response = await fetch('db.csv');
  const data = await response.text();
  const table = data.split(/\n/).slice(1);
  table_length = table.length;
  
  table.every(row => {
      
    const columns = row.split(',');
  
    const source = columns[0];
    sources.push(source);
    
    const title = columns[1];
    titles.push(title);

    const author = columns[2];
    authors.push(author);

    const date = columns[3];
    dates.push(date);

    const link = columns[4];
    links.push(link);

      // Check if the link value is undefined
      if (link != undefined) {
    
      // Create Link Text
      var temp_link = document.createElement("a");
      temp_link.href = link;
      temp_link.target = '_blank';
      temp_link.innerHTML = title;
      temp_link.style.textDecoration = "none";

      var par = document.createElement("p");
      par.style.fontSize = "20px";  //Set style for Headline
      par.style.fontWeight = "900";
      par.style.marginTop = "22px";
      par.classList.add("gen_headline");
      par.appendChild(temp_link);

      }

      // If content is not null:
      if (document.getElementById("content")) {

      document.getElementById("content").appendChild(par);

      // Create Subtext
      const para = document.createElement("p");
      if (author.length < 4) {
        var node = document.createTextNode("By " + source + " | " + date);
      } 
      else {
        var node = document.createTextNode("By " + author + " at " + source + " | " + date);
      }
      // const node = document.createTextNode("By Benjamin Lee at thingiverse.com | 9 hours ago");
      para.style.fontSize = "14px";  //Set style for Subtext
      para.style.color = "#949494";
      para.style.padding = "8px 0 24px 0";
      para.style.borderBottom = "1px solid #d9e1ec"; 
      para.classList.add("gen_subtext");
      para.appendChild(node);

      const element = document.getElementById("content");
      element.appendChild(para);

        
      // Hide Elements
      let x = document.getElementsByClassName('gen_headline');
      let y = document.getElementsByClassName('gen_subtext');
      for (let i = 0; i < x.length; i++) { 
        if (i > 9) {
            x[i].style.display="none";
            y[i].style.display="none";
        }
        else {
            x[i].style.display="block"; 
            y[i].style.display="block";  
        }
        
    }

      }
      
      return true;
  });
  
}


function lookUp() {
    let input = document.getElementById('myInput').value;
    input=input.toLowerCase();
    let x = document.getElementsByClassName('gen_headline');
    let y = document.getElementsByClassName('gen_subtext');
    let loadButton = document.getElementById("load");

    if (input.length < 1) {
      for (let i = 0; i < x.length; i++) { 
        if (i > 9) {
            x[i].style.display="none";
            y[i].style.display="none";
        }
        else {
            x[i].style.display="block"; 
            y[i].style.display="block";  
        }
        
    }
    }
      
    else {
  
    for (let i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
            y[i].style.display="none";
            loadButton.style.display="none";
        }
        else {
            x[i].style.display="block"; 
            y[i].style.display="block";  
            loadButton.style.display="block";
        }
        
    }

    }

  
}

function loadMore() {
    style_count += 10;
    let x = document.getElementsByClassName('gen_headline');
    let y = document.getElementsByClassName('gen_subtext');

    for (let i = 0; i < x.length; i++) { 
        if (i > style_count-1) {
            x[i].style.display="none";
            y[i].style.display="none";
        }
        else {
            x[i].style.display="block"; 
            y[i].style.display="block";  
        }   
    }
}

var toggle = false;
function myFunction() {
  var element = document.body;
  let searchbar = document.getElementById("myInput");
  let colorbutton = document.getElementById("colorbutton");
  let svgcolor = document.getElementById("before");
  element.classList.toggle("dark-mode");
  searchbar.classList.toggle("dark-mode");
  colorbutton.classList.toggle("dark-mode2");
  svgcolor.classList.toggle("dark-mode2");
  if (toggle === true) {
      document.getElementById('image_full').src  = 'images/logo.svg';
  } else {
      document.getElementById('image_full').src = 'images/logo-dark.svg';
  }
  toggle = !toggle; 
}



// Display first 10 News
getData(9);

