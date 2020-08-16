var input = document.getElementById("player-input-name");
var dataList = document.getElementById("player-list-input");
// Create a new XMLHttpRequest.
var request = new XMLHttpRequest();

/// this is shared with sendpredictbyplayername 
var clientPlayerNametoServerUIDDictionary = {};

// Handle state changes for the request.
request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {
      // Parse the JSON
      var jsonOptions = JSON.parse(request.responseText);

      //create dictionary
      

      // Loop over the JSON array.
      jsonOptions.forEach(function(item, index, array) {
        
          var option = document.createElement('option');
          option.value = item.name;
          //console.log(array[100].name);
          // clean this shit up later
          if ( 0 < index  && index <  array.length - 2){       
            if(item.name === array[index-1].name ||  item.name === array[index+1].name ){
              option.value +=  ` ${item.position} ${item['first year']}-${item.active ? 'Active': item['last year']}`;
            }
          }
          if(index === 0){
            if(item.name === array[index+1].name ){
              option.value +=  ` ${item.position} ${item['first year']}-${item.active ? 'Active': item['last year']}`;
            }
          }
          if(index === array.length - 1){
            if(item.name === array[index-1].name ){
              option.value +=  `${item.position} ${item['first year']}-${item.active ? 'Active': item['last year']}`;
            }
          }
          // add player names to option list, add dictionary items
          clientPlayerNametoServerUIDDictionary[option.value] = item.url;         
          dataList.appendChild(option);
      });
      // Update the placeholder text.     
      input.placeholder = "Player first and last name";
    }      
     else {
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
