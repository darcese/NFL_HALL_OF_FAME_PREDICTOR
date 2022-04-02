var dataList = document.getElementById("player-list-input");




//////////////////////////////////////////player-input-stats-predict
var currentSelection = undefined;
// DEALING WITH SWITCHES FROM CHANGES IN BY PREDICTING BY NAME OR BY ENTERING STATS
function searchTypeChange(e){
  document.getElementById( "api-test-response-label").style.display= "hidden";
  document.getElementById( "player-input-stats-predict").style.display= "hidden";
  document.getElementById( "player-input-name-predict").style.display= "hidden";
  let playerName = "Player Name".toUpperCase();
  currentSelection = e.target.getAttribute('id');
  e.target.innerText.toUpperCase() === playerName ? 
  
  (

  
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
  document.getElementById("statsButton1").style.backgroundColor = "rgba(67, 15, 80, 0.5)",
  
  
  document.getElementById("player-input-name").focus(), 
  document.getElementById( "api-test-response-label").style.display= "none",
  document.getElementById( "player-input-stats-predict").style.display= "none",
  document.getElementById( "player-input-name-predict").style.display= "none",
 
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
  document.getElementById("playerNameButton1").style.backgroundColor = "rgba(67, 15, 80, 0.5)",
  document.getElementById("playerNameButton1").style.borderStyle = "solid",
  document.getElementById("playerNameButton1").borderStyle = "solid",
  changePredictByStatsTable(),
  document.getElementById( "api-test-response-label").style.display= "none",
  document.getElementById( "player-input-stats-predict").style.display= "none",
  document.getElementById( "player-input-name-predict").style.display= "none"

  );
}
// ASSOCIATED EVENT LISTENTER
document.getElementById("playerNameButton1").addEventListener('click', searchTypeChange, false);
document.getElementById("statsButton1").addEventListener('click', searchTypeChange, false);
//document.getElementById("playerNameButton1").addEventListener('ontouchend', searchTypeChange, false);
//document.getElementById("statsButton1").addEventListener('ontouchend', searchTypeChange, false);
    
//////////////////////////////////////////////////////////////////////////////////

//document.getElementById("statsButton1").addEventListener('hover', makeButtonAppearActive, false);
document.getElementById("statsButton1").addEventListener('mousemove', makeButtonAppearActive, false);
document.getElementById("statsButton1").addEventListener('mouseout', makeButtonAppearInactive, false);
document.getElementById("playerNameButton1").addEventListener('mousemove', makeButtonAppearActive, false);
document.getElementById("playerNameButton1").addEventListener('mouseout', makeButtonAppearInactive, false);
document.getElementById("player-input-name-predict").addEventListener('mousemove', makeButtonAppearActive, false);
document.getElementById("player-input-name-predict").addEventListener('mouseout', makeButtonAppearInactive, false);
document.getElementById("player-input-stats-predict").addEventListener('mousemove', makeButtonAppearActive, false);
document.getElementById("player-input-stats-predict").addEventListener('mouseout', makeButtonAppearInactive, false);
document.getElementById( "api-test-response-label").style.display= "hidden";
document.getElementById( "player-input-stats-predict").style.display= "hidden";
document.getElementById( "player-input-name-predict").style.display= "hidden";

function  makeButtonAppearActive(){
  
  this.style.borderColor = "rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48) rgb(247, 184, 48)",
  this.style.color = "rgb(247, 184, 48)",
  this.style.borderStyle = "solid",
  this.style.backgroundColor= "rgba(67, 15, 80,0.5)";
}

function makeButtonAppearInactive(){
  if(currentSelection !== this.id){
    this.style.borderColor = "rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80) rgb(67, 15, 80)",
    this.style.color = "rgb(67, 15, 80)",
    this.style.borderStyle = "solid",
    this.style.backgroundColor= "rgba(247, 184, 48, 0.5)";
  };
}
