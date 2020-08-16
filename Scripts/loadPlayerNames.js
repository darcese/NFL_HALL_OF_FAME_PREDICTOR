var input = document.getElementById("player-input-name");
var dataList = document.getElementById("player-list-input");
// Create a new XMLHttpRequest.
var request = new XMLHttpRequest();


// TODO CHECK IF PLAYER HAS A REPEAT NAME IF SO APPEND POSITION YEAR START

var clientPlayerNametoServerUIDDictionary = {};

// Handle state changes for the request.
request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {
      // Parse the JSON
      var jsonOptions = JSON.parse(request.responseText);

      // Loop over the JSON array.
      jsonOptions.forEach(function(item) {
        // Create a new <option> element.
        var option = document.createElement('option');
        // Set the value using the item in the JSON array.
        option.value = item.name;
        dataList.appendChild(option);
        clientPlayerNametoServerUIDDictionary[item.name] = item.url;
      });

      // Update the placeholder text.
      input.placeholder = "player first & last name";
      
    } else {
      // An error occured :(
      input.placeholder = "Couldn't load datalist options :(";
    }
  }
};

// Update the placeholder text.
input.placeholder = "Loading options...";

// Set up and make the request.
request.open('GET', '../Scraping/player_list.json', true);
request.send();

// START THE page with the focus on the player-input-name
document.getElementById("player-input-name").focus();
//////////////////////////////////////////////////////////////////