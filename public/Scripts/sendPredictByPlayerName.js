

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

    document.getElementById("api-test-response-label").innerHTML = "";
    if (input_valid === true){
      console.log("input valid");
      document.getElementById("player-input-name").style.color= "rgb(247, 184, 48)";
      document.getElementById("player-input-name").style.borderColor= "rgb(247, 184, 48)";
      document.getElementById("player-input-name").style.backgroundColor= "rgba(67, 15, 80,0.5)";
  
      document.getElementById("player-input-name-predict").style.display="flex";
     // document.getElementById("go-button").style="border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color: rgba(0,0,0,1);";
    }
    else{
      console.log("input not valid");
      
      document.getElementById("player-input-name-predict").style.display="none";
      document.getElementById("player-input-name").style.color= "rgb(67, 15, 80)" ;
      document.getElementById("player-input-name").style.borderColor= "rgb(67, 15, 80)";
      document.getElementById("player-input-name").style.backgroundColor= "rgba(247, 184, 48, 0.5)";
  
      "border-color:rgb(167, 230, 167); background-color: rgb(167, 230, 167); color= rgba(0,0,0,1);";
    }
  }
  
  document.getElementById("player-input-name").addEventListener('input', playerNameCheck, false);




  ////////////////////////////////////////////////

  function sendPlayerNameToAPIForPrediction(){
    var inputToApi = document.getElementById("player-input-name");
    //var ApiValuesAsArray = inputToApi.value.split(',');
    //let stats = ['TotalYears',  'MVP', 'ProBowls', 'AllPro', 'SbChamp', 'APpoy'];
   
    
    var ApiObject = {};
    ApiObject['Name'] = inputToApi.value; 
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
    //req.open("POST", 'http://127.0.0.1:5000/api/input_as_name/generate_prediction', true); //make this False later to try synchronous version
    req.open("POST", 'https://nfl-hall-of-fame-predictor-api.herokuapp.com/api/input_as_name/generate_prediction', true);
    req.setRequestHeader("Content-Type", "application/json"); //might not be necessary for now
    req.send(ApiObject);
  
    req.onreadystatechange = function(response) {
      if (req.readyState === 4) {
        if (req.status === 200) {
          // Parse the JSON
          
        document.getElementById( "api-test-response-label").style.display= "flex";
        document.getElementById("api-test-response-label").innerHTML =   Number(Number(req.responseText).toFixed(2)* 100 ) + '%';
        window.scrollBy(0, 100);
        }
      }
    };
    
    //////////let ApiObject1 = document.getElementById("position-select").value
  
  }
    
 // document.getElementById("api-test-submit-button").addEventListener('click', sendInputToApi, false);

 var playerNameInput = document.getElementById("player-input-name");
 playerNameInput.addEventListener('input', function(){
   console.log(this.value + this.label);
 });

  document.getElementById("player-input-name-predict").addEventListener('click', sendPlayerNameToAPIForPrediction, false);