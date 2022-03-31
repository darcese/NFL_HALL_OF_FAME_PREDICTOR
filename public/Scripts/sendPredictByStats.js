
function sendInputToApi(){
   
   
    

    let stats = ['Total Years',  'MVPs', 'Pro Bowls', 'All Pros', 'SB Wins', 'AP POYs'];
    let table = document.getElementById("predict-by-stats-table");
    statInputIds = []
    stats.forEach(element => {
      statInputIds.push(element.replace(/\s/g, '')+"statInput");
      console.log(element.replace(/\s/g, '')+"statInput");
    });

    
    var ApiObject = {};
    statInputIds.forEach(element => { ApiObject[element.replace('statInput','')] = document.getElementById(element).value || 0;} );
    // var ApiObject = {
    //                 Position: ApiValuesAsArray[0].toUpperCase() || 'QB',
    //                 TotalYears: ApiValuesAsArray[1] || 0,
    //                 MVP: ApiValuesAsArray[2] || 0 ,
    //                 ProBowl: ApiValuesAsArray[3] || 0,
    //                 AllPro: ApiValuesAsArray[4] || 0,
    //                 SbChamp: ApiValuesAsArray[5] || 0,
    //                 APpoy: ApiValuesAsArray[6] || 0,
    //                 };
    ApiObject['Position'] = document.getElementById("position-select").value; 
    ApiObject = JSON.stringify(ApiObject);
    console.log(ApiObject);
  
    var req = new XMLHttpRequest();   // new HttpRequest instance 

    req.open("POST", 'https://nfl-hall-of-fame-predictor-api.herokuapp.com/api/inputs_as_stats/generate_prediction', true); //make this False later to try synchronous version
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
    
document.getElementById("player-input-stats-predict").addEventListener('click', sendInputToApi, false);
  //document.getElementById("player-input-name").addEventListener('focus', (event) => {
   // document.getElementById("player-input-name").style.color= 'pink';    
  //});