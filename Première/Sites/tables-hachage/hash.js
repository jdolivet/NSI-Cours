var hash = {
	init: function(){
		this.insertSpan = this.byId("hash-demo-insert");
		this.insertInput = this.byId("hash-demo-insert-input");
		this.searchInput = this.byId("hash-demo-search-input");
		this.view = this.byId("hash-demo-view");
		this.log = this.byId("hash-demo-log");
				
		//Initialize templates
		jsviews.templates({
			algoTemplate: this.byId("hash-algo-select-template").innerHTML,
			tableTemplate: this.byId("hash-table-template").innerHTML,
		});
		
		//Create the algo select from the template
		this.byId("hash-add-select-please").innerHTML += jsviews.render.algoTemplate({algos: this.algos});
		this.algoSelect = this.byId("hash-demo-algo")

		this.automatic = false;
		
		//Render the view for the first time
		this.algoSelection();
		this.inputChange(!this.byId("hash-default-insert").checked);
	},

	byId: function(id){
		return document.getElementById(id);
	},
	
	/*****************************************************************************\
									EVENT HANDLING
	\*****************************************************************************/

	//Called when the usre change the algorithm
	algoSelection: function(){
		this.algo = this.algos[this.algoSelect.value];
		this.hashtable = [];

		//Populate the hashtable with -1 as it seems jsrender didn't like undefined
		for(var i = 0; i < this.algo.size; i++){
			this.hashtable.push(-1);
		}
		
		this.drawHashtable();
		
		//Reset some things
		this.cancelAutoInsert();
		this.log.innerHTML = "";
	},

	//Called when the user changes the input method
	inputChange: function(value){
		this.automated = value;
		this.insertSpan.style.display = value ? "none" : "inline";
		this.cancelAutoInsert();
	},

	//Called when the user clicks on insert
	doInsert: function(){
		this.cancelAutoInsert();
		
		//If it is a manual insertion just check the value and do it
		if(!this.automated){
			var n = parseInt(this.insertInput.value);
			if(n >= 0){
				this.insert(n);
			}
			this.insertInput.value = "";
		}else{
			//If it is an automatic insertion start it;
			var self = this;
			
			var autoInsert = function(){
				var n = self.pickNumber();
				self.insert(n);
			}; 
			
			//Save it to be able to cancel it
			this.autoInterval = setInterval(autoInsert, 2000);
			
			//Do the first insertion right now to have immediate feedback
			autoInsert();
		}
	},
	
	//Called when the user clicks on search
	doSearch: function(){
		var n = parseInt(this.searchInput.value);
		if(n >= 0){
			this.search(n);
		}
		this.searchInput.value = "";
	},
	
	cancelAutoInsert: function(){
		clearInterval(this.autoInterval);
	},

	/*****************************************************************************\
									PRESENTATION
	\*****************************************************************************/

	
	drawHashtable: function(){
		//Draw every bucket using a template
		this.view.innerHTML = jsviews.render.tableTemplate(this.hashtable);
	},
	
	//Used to highlight part of the text in the logs
	hl: function(s){
		return '<span class="hash-hl">' + s + '</span>';
	},
	
	/*****************************************************************************\
									ALGORITHMS (very simple ones)
	\*****************************************************************************/

	//Picks a random number, we want the number of digits to be distributed evenly
	pickNumber: function(){
		var nDigits = Math.floor(Math.random() * 5) + 1;
		var n = 0;
		for(var i = 0; i < nDigits; i++){
			n = n*10 + Math.floor(Math.random() * 10);
		}
		return n;
	},
	
	//Does the insertion in the hashtable and at the same time creates the log
	insert: function(n){
		var log = [];
		log.push(this.algo.log(n, this));
		
		var index = this.algo.apply(n);
		var endIndex = index + this.algo.size;

		while(index != endIndex){
			var realIndex = index % this.algo.size;
			
			//We found an empty cell, put the value in it
			if(this.hashtable[realIndex] < 0){
				this.hashtable[realIndex] = n;
				log.push("");
				log.push("la case " + this.hl(realIndex) + " est vide, on range " + this.hl(n) + " dans cette case");
				break;
			}
			
			//We found the value in the hashtable, finish now
			if(this.hashtable[realIndex] == n){
				log.push("");
				log.push(this.hl(n) + " existe déjà dans la table");
				break;
			}
			
			//Handles the "end of hashtable, go back at the start" case
			if(index != this.algo.size - 1){
				log.push("la case " + this.hl(realIndex) + " est occupée on avance d'une case");
			}else{
				log.push("la case " + this.hl(realIndex) + " est occupée et comme c'est la dernière case on revient au début");
			}
			index ++;
		}
		
		//Did we find the value ?
		if(index == endIndex){
			log.push("");
			log.push("toutes les cases de la table sont occupées");
			this.cancelAutoInsert();
		}
		
		//Update the view
		this.log.innerHTML = log.join("<br/>");
		this.drawHashtable();
	},
	
	search: function(n){
		var log = [];
		log.push(this.algo.log(n, this));
		
		var hasFound = false;
		var index = this.algo.apply(n);
		var endIndex = index + this.algo.size;

		while(index != endIndex){
			var realIndex = index % this.algo.size;
			
			//We found an empty cell, end of the search
			if(this.hashtable[realIndex] < 0){
				log.push("la case " + this.hl(realIndex) + " est vide");
				break;
			}

			//We found the value in the hashtable, finish now
			if(this.hashtable[realIndex] == n){
				hasFound = true;
				log.push("");
				log.push(this.hl(n) + " se trouve dans la case " + this.hl(realIndex));
				break;
			}
			
			//Handles the "end of hashtable, go back at the start" case
			if(index != this.algo.size - 1){
				log.push(this.hl(n) + " n'est pas dans la case " +this.hl(realIndex) + " on avance d'une case");
			}else{
				log.push(this.hl(n) + " n'est pas dans la case " +this.hl(realIndex) + " et comme c'est la dernière case de la table on revient au début");
			}
			index ++;
		}

		//Did we find the value ?s
		if(!hasFound){
			log.push("");
			log.push("l'élément cherché ne figure pas dans la table.");
		}
		
		//Update the view
		this.log.innerHTML = log.join("<br/>");
		this.drawHashtable();
	},
	
	//The list of all the algorithms
	algos: [
		{
			name: "Modulo 5",
			size: 5,
			apply: function(n){
				return n % 5;
			},
			log: function(n, main){
				return main.hl(n) + " MOD " + main.hl(5) + " = " + main.hl(this.apply(n));
			}
		},
		{
			name: "Modulo 12",
			size: 12,
			apply: function(n){
				return n % 12;
			},
			log: function(n, main){
				return main.hl(n) + " MOD " + main.hl(12) + " = " + main.hl(this.apply(n));
			}
		},
		{
			name: "Modulo 16",
			size: 16,
			apply: function(n){
				return n % 16;
			},
			log: function(n, main){
				return main.hl(n) + " MOD " + main.hl(16) + " = " + main.hl(this.apply(n));
			}
		},
		{
			name: "Modulo 21",
			size: 21,
			apply: function(n){
				return n % 21;
			},
			log: function(n, main){
				return main.hl(n) + " MOD " + main.hl(21) + " = " + main.hl(this.apply(n));
			}
		},
		{
			name: "Modulo 27",
			size: 27,
			apply: function(n){
				return n % 27;
			},
			log: function(n, main){
				return main.hl(n) + " MOD " + main.hl(27) + " = " + main.hl(this.apply(n));
			}
		},
		{
			name: "Sommes Chiffres",
			size: 10,
			apply: function(n){
				var sum = 0;
				while(n != 0){
					sum += n % 10;
					n = Math.floor(n / 10);
				}
				return sum % 10;
			},
			log: function(n, main){
				var text = "La somme des chiffres de " + main.hl(n) + " est ";

				//We need to get all the digits in reverse order
				var textSum = "";
				var first = true;
				var sum = 0;
				while(n != 0){
					if(!first){
						textSum = "+" + textSum;
					}
					sum += n % 10;
					textSum = main.hl(n%10) + textSum;
					n = Math.floor(n / 10);
					first = false;
				}
				
				text += textSum + " = " + main.hl(sum) + " on garde le dernier chiffre " + main.hl(sum%10);
				return text;
			}
		}
	]
	
}

if(window.addEventListener){
    window.addEventListener('load',function(){hash.init();});
}
else{
    window.attachEvent('onload',function(){hash.init();});
}