//Loads Who, What, Where in that order
for (var i = 0; i < 3; i++) {
    var getURL = new XMLHttpRequest();
    var cards = document.getElementById("cards");
    var CardType = "" 
    switch (i) {
        case 0:
            CardType = "Who";
        case 1:
            CardType = "What";
        case 2:
            CardType = "Where";
    }
    var Card = new Element();
    if (CardType != "") {
        getURL.open("GET","http://localhost/api/get" + CardType);
            getURL.onloadend = () => {
                Card.textContent = getURL.responseText;
            }
            getURL.onerror = () => {
                Card.textContent = "Sorry, we couldn't load your result. Please try again.";
            }
            getURL.send();
            Card.textContent = "We are randomly choosing a partner for you!";
    }
}