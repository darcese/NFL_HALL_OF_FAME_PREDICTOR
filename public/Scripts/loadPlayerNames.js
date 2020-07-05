var input = document.getElementById("player-input-name");
var dataList = document.getElementById("player-list-input");
// Create a new XMLHttpRequest.
var request = new XMLHttpRequest();


// Handle state changes for the request.
request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {
      // Parse the JSON
      var playersArray = []
      var jsonOptions = JSON.parse(request.responseText);

      // Loop over the JSON array.
      jsonOptions.forEach(function(item, index, array) {
        // Create a new <option> element.
        
        // Set the value using the item in the JSON array.
        // "name": "Rod Smith",
        // "url": "/S/SmitRo23.htm",
        // "position": "DB",
        // "hall of fame": false,
        // "first year": 1992,
        // "last year": 1998,
        // "active": false
        
        playersArray.push(item.name);
        // to check if two players have same name
        if( 0 < index < array.length - 1){
          if(item.name === array[index - 1].name){
            playersArray[index - 1] = array[index - 1].name + " " + array[index - 1].position + " " + array[index - 1]["first year"];
            playersArray[index] = array[index].name + " " + array[index].position + " " + array[index]["first year"];
          }
          if(item.name === array[index + 1].name){
            playersArray[index + 1] = array[index + 1].name + " " + array[index + 1].position + " " + array[index + 1]["first year"];
            playersArray[index] = array[index].name + " " + array[index].position + " " + array[index]["first year"];
          }
        }
      });

      // add player names to option list
      playersArray.forEach(function(item){
        var option = document.createElement('option');
        option.value = 'poop';
        dataList.appendChild(option);
      })      

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
request.open('GET', 'Scripts/player_list.json', true);
request.send();

// START THE page with the focus on the player-input-name
document.getElementById("player-input-name").focus();
//////////////////////////////////////////////////////////////////