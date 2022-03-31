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
      let stats = ['Total Years',  'MVPs', 'Pro Bowls', 'All Pros', 'SB Wins', 'AP POYs'];
      let table = document.getElementById("predict-by-stats-table");
      statInputIds = []

      function decrement(e) {
        let statInput = e.target.nextElementSibling;
        let min =  parseInt(statInput.min);
        let value = parseInt(statInput.value);
        if(min < value){
          value -= 1;
           document.getElementById(statInput.id).value = value;
           statValuesChange();
        }
      }
      
      function increment(e) {
        let statInput = e.target.previousElementSibling;
        let max =  parseInt(statInput.max);
        let value = parseInt(statInput.value);
        if(value < max){
          value += 1;
           document.getElementById(statInput.id).value = value;
           statValuesChange();
        }
      }

      stats.forEach(element => {
        table.insertRow(-1);
        let row =  table.rows.item(table.rows.length-1);
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        cell1.innerHTML = element;
        
        //element.replace since id cant have spaces
        statInputIds.push(element.replace(/\s/g, '')+"statInput");
        cell2.innerHTML =   String.raw`<div class="container">
        <button id=${element.replace(/\s/g, '')+"decrement"} class="decrement">
        -
        </button>
        <input id=${element.replace(/\s/g, '')+"statInput"} value= 0 min=0 max=35 type="number" class="statInput" readonly >
        <button id=${element.replace(/\s/g, '')+"increment"} class="increment">
        +
        </button>
      </div>`;
       
        // element.replace(/\s/g, '')

      document.getElementById(element.replace(/\s/g, '')+"decrement").addEventListener("click", decrement);
      
      document.getElementById(element.replace(/\s/g, '')+"increment").addEventListener("click", increment);
      
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


function statValuesChange(){

    var shouldBeDisplayed = true;
   
    for (var id of statInputIds) { 
      if (isNaN(parseInt(document.getElementById(id).value, 10)) === true){
        shouldBeDisplayed = false;
      }
    }
    if(shouldBeDisplayed=== true){
      document.getElementById("player-input-stats-predict").style.display = "flex";
    }
    else{
      document.getElementById("player-input-stats-predict").style.display = "none";
      document.getElementById( "api-test-response-label").style.display= "none";
    }
 
  }
  ////////////////////////////////////////////
  
  
  //// Delete later and capitalize stuff manually
  //const searchByDiv = document.getElementById("enter-string-or-stats-option-container");
  //const searchByDivChildren = searchByDiv.children;
  
  //for ( var i = 0; i < searchByDivChildren.length; i++) {
  //    searchByDivChildren[i].innerHTML = searchByDivChildren[i].innerHTML.toUpperCase();
   // }
  
  
  
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