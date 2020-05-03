
//// CREATING DATALIST INPUT OPTIONS FOR THE SEARCH BY PLAYER INPUT
// Get the <datalist> and <input> elements.
var dataList = document.getElementById("player-list-input");
var input = document.getElementById("player-input-name");

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
request.open('GET', 'Scraping/player_list.json', true);
request.send();

// START THE page with the focus on the player-input-name
document.getElementById("player-input-name").focus();
//////////////////////////////////////////////////////////////////


///////////////////////////////////
function goButtonClick(){
    console.log("hi");
}
//////////////////////////////////////////
var currentSelection = undefined;
// DEALING WITH SWITCHES FROM CHANGES IN BY PREDICTING BY NAME OR BY ENTERING STATS
function searchTypeChange(e){
  let playerName = "Player Name".toUpperCase();
  currentSelection = e.target.getAttribute('id');
  e.target.innerText.toUpperCase() === playerName ? 
  
  (
  console.log("playername button selected"),
  
  document.getElementById("search-by-stats-container").style.display= "none",
    //document.getElementById("statsButton").style="border-color:rgb(235, 221, 159); background-color: rgb(235, 221, 159); color= rgba(0,0,0,1);",
  //document.getElementById("playerNameButton").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);",
  document.getElementById("search-by-player-container").style.display = "flex",
  document.getElementById("search-by-player-container").style.flexDirection = "column",
  document.getElementById("search-by-player-container").style.justifyContent = "center",
  document.getElementById("search-by-player-container").style.alignItems = "center",
  document.getElementById("search-by-player-container").style.margin = "2rem",
  document.getElementById("playerNameButton1").style.borderColor = "rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48)",
  document.getElementById("playerNameButton1").style.color = "rgb(247, 184, 48)",
  document.getElementById("playerNameButton1").style.borderStyle = "solid",
  
  document.getElementById("statsButton1").style.borderColor = "rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80)",
  document.getElementById("statsButton1").style.color = "rgb(67, 15, 80)",
  document.getElementById("statsButton1").style.borderStyle = "solid",
  
  
  document.getElementById("player-input-name").focus(), 
  
 
  playerNameCheck()
  ): 
  (
    //document.getElementById("statsButton").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);",
  //document.getElementById("playerNameButton").style="border-color:rgb(235, 221, 159); background-color: rgb(235, 221, 159)",
  
  document.getElementById("search-by-player-container").style.display = "none",
  document.getElementById("search-by-stats-container").style.display= "flex",

  document.getElementById("statsButton1").style.borderColor = "rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48)",
  document.getElementById("statsButton1").style.color = "rgb(247, 184, 48)",
  document.getElementById("statsButton1").style.borderStyle = "solid",
  
  document.getElementById("playerNameButton1").style.borderColor = "rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80)",
  document.getElementById("playerNameButton1").style.color = "rgb(67, 15, 80)",
  document.getElementById("playerNameButton1").style.borderStyle = "solid",
  document.getElementById("playerNameButton1").borderStyle = "solid",
  changePredictByStatsTable()
  );
}
// ASSOCIATED EVENT LISTENTER
document.getElementById("playerNameButton1").addEventListener('click', searchTypeChange, false);
document.getElementById("statsButton1").addEventListener('click', searchTypeChange, false);

//////////////////////////////////////////////////////////////////////////////////

//document.getElementById("statsButton1").addEventListener('hover', makeButtonAppearActive, false);
document.getElementById("statsButton1").addEventListener('mouseover', makeButtonAppearActive, false);
document.getElementById("statsButton1").addEventListener('mouseout', makeButtonAppearInactive, false);
document.getElementById("playerNameButton1").addEventListener('mouseover', makeButtonAppearActive, false);
document.getElementById("playerNameButton1").addEventListener('mouseout', makeButtonAppearInactive, false);
document.getElementById("player-input-name-predict").addEventListener('mouseover', makeButtonAppearActive, false);
document.getElementById("player-input-name-predict").addEventListener('mouseout', makeButtonAppearInactive, false);

function  makeButtonAppearActive(){
  
  this.style.borderColor = "rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48)",
  this.style.color = "rgb(247, 184, 48)",
  this.style.borderStyle = "solid"
}

function makeButtonAppearInactive(){
  if(currentSelection !== this.id){
    this.style.borderColor = "rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80)",
    this.style.color = "rgb(67, 15, 80)",
    this.style.borderStyle = "solid"
  };
}



function playerNameCheck(){
  let player_input_value = document.getElementById("player-input-name").value.replace(/ /gi, "").toUpperCase();
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
    document.getElementById("player-input-name").style.color= "rgb(247, 184, 48)";
    document.getElementById("player-input-name-predict").style.display="block";
   // document.getElementById("go-button").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color: rgba(0,0,0,1);";
  }
  else{
    console.log("input not valid");
    
    document.getElementById("player-input-name-predict").style.display="none";
    document.getElementById("go-button").style.borderColor="";
    document.getElementById("go-button").style.backgroundColor="";
    document.getElementById("go-button").style.color="grey";
    document.getElementById("player-input-name").style.color= "rgb(67, 15, 80)" ;
    "border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);";
  }
}

document.getElementById("player-input-name").addEventListener('input', playerNameCheck, false);
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
  document.getElementById("search-by-stats-container").style.display = "flex";
  document.getElementById("search-by-stats-container").style.alignItems = "center";
  document.getElementById("search-by-stats-container").style.justifyContent = "center";
  document.getElementById("search-by-stats-container").style.margin = "auto";
  document.getElementById("search-by-stats-container").style.marginTop = "2rem";
  document.getElementById("predict-by-stats-table").insertRow(-1);
     
  console.log(document.getElementById("position-select").value);
  if (document.getElementById("position-select").value !=="POS VALUE") {
    let stats = ['TotalYears',  'MVP', 'ProBowls', 'AllPro', 'SbChamp', 'APpoy'];
    let table = document.getElementById("predict-by-stats-table");
    stats.forEach(element => {
      table.insertRow(-1);
      let row =  table.rows.item(table.rows.length-1);
      let cell1 = row.insertCell(0);
      let cell2 = row.insertCell(1);
      cell1.innerHTML = element;
      cell2.innerHTML = '<input type="number" ' + ' id=' + element +' name=' + element +' \
min="0" max="50" step="1">';

      
    });
  } else{
    
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



  ///////////////////api testing only

  // <input type="text" id="api-test-input-text"></input>
  //<button type="submit" id="api-test-submit-button"></button>
// [ TotalYears[index],\
//MVP[index], \
//ProBowl[index], \
//AllPro[index], \
//SbChamp[index], \
//APpoy[index] \
//] for index, element in  enumerate(TotalYears)]


function sendInputToApi(){
  var inputToApi = document.getElementById("api-test-input-text");
  var ApiValuesAsArray = inputToApi.value.split(',');
  let stats = ['TotalYears',  'MVP', 'ProBowls', 'AllPro', 'SbChamp', 'APpoy'];
 
  
  var ApiObject = {};
  stats.forEach(element => { ApiObject[element] = document.getElementById(element).value || 0;} );
  // var ApiObject = {
  //                 Position: ApiValuesAsArray[0].toUpperCase() || 'QB',
  //                 TotalYears: ApiValuesAsArray[1] || 0,
  //                 MVP: ApiValuesAsArray[2] || 0 ,
  //                 ProBowl: ApiValuesAsArray[3] || 0,
  //                 AllPro: ApiValuesAsArray[4] || 0,
  //                 SbChamp: ApiValuesAsArray[5] || 0,
  //                 APpoy: ApiValuesAsArray[6] || 0,
  //                 };
  ApiObject = JSON.stringify(ApiObject);

  var req = new XMLHttpRequest();   // new HttpRequest instance 
  req.open("POST", 'http://127.0.0.1:5000/api/inputs', true); //make this False later to try synchronous version
  req.setRequestHeader("Content-Type", "application/json"); //might not be necessary for now
  req.send(ApiObject);

  req.onreadystatechange = function(response) {
    if (req.readyState === 4) {
      if (req.status === 200) {
        // Parse the JSON
        
      document.getElementById("api-test-response-label").innerHTML =   req.responseText;
      }
    }
  };
  
  //////////let ApiObject1 = document.getElementById("position-select").value

}
  
document.getElementById("api-test-submit-button").addEventListener('click', sendInputToApi, false);
