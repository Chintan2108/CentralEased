/*var json = { "D1" : { "name": "lassan",
            "id": 999,
            "something": "everything"},
  "D2" : { "name" : "lassan XX",
            "id" : 917,
            "something new" : "everything else"}
};

//console.log(json);

//var json = JSON.parse(data);

*/
function addData(json){
	for(data in json){
	  var table = document.createElement("table");
	  table.setAttribute('style',"border:2px solid black; width:50%; border-radius:25px");
	  table.setAttribute('align',"center");
	  table.setAttribute('border',"1px");
	  var th = document.createElement("th");
	  th.innerHTML = data;
	  th.setAttribute('style',"text-align:center")
	  th.setAttribute('colspan','2')
	  var tr = document.createElement("tr");
	  var nl = document.createElement("hr");
	  nl.setAttribute('style',"align:center");
	  th.appendChild(nl);
	  tr.appendChild(th);
	  tr.setAttribute('style',"background-color:#E6E6FA");
	  table.appendChild(tr);
	  //console.log(data);

	  dbs = json[data];

	  for(db in dbs){
		  var tr = document.createElement("tr");
		  var td = document.createElement("td");
		  td.innerHTML = db;
		  tr.appendChild(td);

		  var td = document.createElement("td");
		  td.innerHTML = dbs[db];
		  tr.appendChild(td);

		  table.appendChild(tr);

		}

		  var databaseHolder = document.getElementById('databaseholder');
		  databaseHolder.appendChild(table);
		  var br = document.createElement("br");
		  databaseHolder.appendChild(br);
		  databaseHolder.appendChild(br);
	}
}
