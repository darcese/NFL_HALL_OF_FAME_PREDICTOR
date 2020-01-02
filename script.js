
//// CREATING DATALIST INPUT OPTIONS FOR THE SEARCH BY PLAYER INPUT
// Get the <datalist> and <input> elements.
var dataList = document.getElementById("player-list-input");
var input = document.getElementById("player-input");

// Create a new XMLHttpRequest.
var request = new XMLHttpRequest();

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
        // Add the <option> element to the <datalist>.
        dataList.appendChild(option);
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
request.open('GET', 'Scraping/full_player_list.json', true);
request.send();

// START THE page with the focus on the player-input
document.getElementById("player-input").focus();
//////////////////////////////////////////////////////////////////


///////////////////////////////////
function goButtonClick(){
    console.log("hi");
}
//////////////////////////////////////////

// DEALING WITH SWITCHES FROM CHANGES IN BY PREDICTING BY NAME OR BY ENTERING STATS
function searchTypeChange(e){
  let playerName = "Player Name".toUpperCase();
  e.target.innerText.toUpperCase() === playerName ? 
  (document.getElementById("statsButton").style="border-color:rgb(235, 221, 159); background-color: rgb(235, 221, 159); color= rgba(0,0,0,1);",
  document.getElementById("playerNameButton").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);",
  document.getElementById("search-by-player-container").style.visibility = "visible",
  document.getElementById("player-input").focus(), 
  document.getElementById("search-by-stats-container").style.visibility= "hidden",
  playerNameCheck()
  ): 
  (document.getElementById("statsButton").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);",
  document.getElementById("playerNameButton").style="border-color:rgb(235, 221, 159); background-color: rgb(235, 221, 159)",
  changePredictByStatsTable(),
  document.getElementById("search-by-player-container").style.visibility = "hidden",
  document.getElementById("search-by-stats-container").style.visibility= "visible"
  );
}
// ASSOCIATED EVENT LISTENTER
document.getElementById("playerNameButton").addEventListener('click', searchTypeChange, false);
document.getElementById("statsButton").addEventListener('click', searchTypeChange, false);
//////////////////////////////////////////////////////////////////////////////////




function playerNameCheck(){
  let player_input_value = document.getElementById("player-input").value.replace(/ /gi, "").toUpperCase();
  let player_list = document.getElementById("player-list-input");
  let i = 0;
  let input_valid = false;
  while(i < document.getElementById("player-list-input").options.length){
    if (player_input_value === player_list.options[i].value.replace(/ /gi, "").toUpperCase()){
      input_valid = true;
      break;
    }
    else{
      i++;
    }  
  }
  PredictByNameReady(input_valid);
}

function PredictByNameReady(input_valid){
  if (input_valid === true){
    console.log("input valid");
    document.getElementById("go-button").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color: rgba(0,0,0,1);";
  }
  else{
    console.log("input not valid");
    document.getElementById("go-button").style.borderColor="";
    document.getElementById("go-button").style.backgroundColor="";
    document.getElementById("go-button").style.color="grey";
    "border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);";
  }
}

document.getElementById("player-input").addEventListener('input', playerNameCheck, false);
//document.getElementById("player-list-input").addEventListener('input', playerNameCheck, false);

///////////////////////////////////


///


/////////////

//// PLACEHOLDER FUNCTION TO CHANGE ROWS BASED ON POSITION WHEN PREDICTING BY TYPING IN STATS
function selectedPositionChange(){
  console.log("position changed");
  changePredictByStatsTable();
}

function modifyText(new_text) {
    const t2 = document.getElementById("t2");
    t2.firstChild.nodeValue = new_text;    
  }

function changePredictByStatsTable(){
  deletePositionRelatedRows();
  console.log(document.getElementById("position-select").value);
  switch (document.getElementById("position-select").value) {
    case 'QB':
      console.log('Oranges are $0.59 a pound.');
      break;
    case 'Mangoes':
    case 'WR':
        let table = document.getElementById("predict-by-stats-table");
        document.getElementById("predict-by-stats-table").insertRow(-1);
        let row =  table.rows.item(table.rows.length-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = "STAT 1";
        cell2.innerHTML = '<input type="number" id="stat1Input" name="tentacles" \
        min="0" max="10000" step="10">';
        document.getElementById("predict-by-stats-table").insertRow(-1);      
        var cell1 = table.rows.item(table.rows.length-1).insertCell(0);
        var cell2 = table.rows.item(table.rows.length-1).insertCell(1);
        cell1.innerHTML = "STAT 2";
        cell2.innerHTML = '<input type="number" id="stat2Input" name="tentacles" \
        min="0" max="10000">';
        console.log('Mangoes and papayas are $2.79 a pound.');
      // expected output: "Mangoes and papayas are $2.79 a pound."
      function addWRRows(){
      }
      break;
    default:     
  }
}

function deletePositionRelatedRows(){
  while ( document.getElementById("predict-by-stats-table").rows.length > 1) {
    document.getElementById("predict-by-stats-table").deleteRow(-1);
  } 
}
function addWRRows(){
}
document.getElementById("position-select").addEventListener('change', selectedPositionChange, false);
////////////////////////////////////////////


//// Delete later and capitalize stuff manually
const searchByDiv = document.getElementById("enter-string-or-stats-option-container");
const searchByDivChildren = searchByDiv.children;

for ( var i = 0; i < searchByDivChildren.length; i++) {
    searchByDivChildren[i].innerHTML = searchByDivChildren[i].innerHTML.toUpperCase();
  }


  
