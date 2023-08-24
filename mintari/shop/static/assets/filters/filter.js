filterSelection("all")
function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("product_filter");
    for (i = 0; i < x.length; i++) {
        hideElement(x[i], c);
    }
}

function hideElement(element, c){
    if (c == "all"){// if filter selection is all elements, all elements visible
        element.hidden = false
    }else if (!element.classList.contains(c)){// if filter selection is all elements, all elements visible
        element.hidden = true
    }else if (element.classList.contains(c)){
        element.hidden = false
    }
}


