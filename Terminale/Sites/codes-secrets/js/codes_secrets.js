/**
	A l'attaque des codes secrets

	Dépendances : 
		• JQuery : http://jquery.com/ (MIT licence)
		• JQuery UI : http://jqueryui.com/ (MIT licence)
		• http://davidbau.com/encode/seedrandom-min.js (BSD licence)

*/

$(function(){

	/*********************************************************************************************************************/
	/***************************                     DONNEES                   **********************************/
	/*********************************************************************************************************************/
	
	var error_key = 'La clé doit être un nombre.'; //erreur de format de la clé
	
	//description de l'attaque à texte clair connu
	var kpta_descr = 'Cette attaque consiste dans ce cas à connaître un mot ou une partie du texte clair et de trouver une unique correspondance dans le texte chiffré pour le décrypter et dévoiler la clé de chiffrement.';
	
	//description de l'attaque force brute
	var bf_descr = "Cette attaque consiste à essayer toutes les possibilités. Ici il n'y a que 25 décalages, donc on peut déchiffrer un texte en maximum 25 essais. (voir explication ci-dessous)";
	
	//erreur de format de texte clair connu
	var error_kpt = 'Le texte clair connu doit comporter uniquement des lettres et de la ponctuation';
	
	//message lorsqu'on a pas de correspondance pour l'attaque à texte clair connu
	var no_match = 'Aucune correspondance n\'a été trouvée.';

	//message lorsqu'on a plusieurs correspondance pour l'attaque à texte clair connu
	var several_match = 'La clé ne peut pas être dévoilée car plusieurs correspondances ont été trouvées.';
	
	//première partie : chiffe de César
		var s_elts = new Array();
		var s_descr = new Array();
		var s_pre = 'shifted';
		var s_type = 'chiffrage';
		
		s_elts[0] = $('#shifted_plainText');
		s_elts[1] = $('#shifted_key');
		s_elts[2] = $('#shifted_buttonsArea');
		s_elts[3] = $('#shifted .knownPlainText');
		
		s_descr[0] = "Veuillez saisir le texte à transformer"; //infobulle de la zone de texte avant transformation
		s_descr[1] = "Entrez ici la clef de décalage"; //infobulle de la clé
		s_descr[2] = "Choisissez ici l'action à effectuer"; //infobulle des boutons
		s_descr[3] = "Veuillez saisir le texte clair connu"; //infobulle de l'attaque à texte connu
		
		
		//deuxième partie : chiffrage par permutation
		var p_elts = new Array();
		var p_descr = new Array();
		var p_pre = 'permuted';
		var p_type = 'chiffrage';
		
		p_elts[0] = $('#permuted_plainText');
		p_elts[1] = $('#permuted_key');
		p_elts[2] = $('#permuted_buttonsArea');
		p_elts[3] = $('#permuted .knownPlainText');
		
		p_descr[0] = "Veuillez saisir le texte à transformer"; //infobulle de la zone de texte avant transformation
		p_descr[1] = "Entrez ici la clef de permutation"; //infobulle de la clé
		p_descr[2] = "Choisissez ici l'action à effectuer"; //infobulle des boutons
		p_descr[3] = "Veuillez saisir le texte clair connu"; //infobulle de l'attaque à texte connu
	
		
		//troisième partie : analyse fréquentielle
		var fa_elts = new Array();
		var fa_descr = new Array();
		var fa_pre = 'freq_ana';
		var fa_type = 'freq_ana';
		
		fa_elts[0] = $('#freq_ana_plainText');
		fa_elts[1] = $('#freq_ana_letters');
		fa_descr[0] = "Veuillez saisir le texte à déchiffrer"; //infobulle de la zone de texte avant transformation
		fa_descr[1] = "Indiquez les substitutions à faire (uniquement des lettres)"; //infobulle des substitutions
	


	/*********************************************************************************************************************/
	/***************************                     TOOLTIP                    **********************************/
	/*********************************************************************************************************************/

	var Tooltip = function(elt,content){

		this.elt=elt;
		this.content=content;
		var that = this; 
		
		this.show = function()
		{
			$(this.elt).tooltip("open");
		}
		
		this.setEnable = function(enable)
		{
			if(enable==true)
				$(this.elt).tooltip("enable");
			else
				$(this.elt).tooltip("disable");
		}
		
		this.close = function()
		{
			$(this.elt).tooltip("close");
		}
		
		this.reset=function()
		{
			$(this.elt).tooltip("option","content",this.content);
		}
		
		/*******************************************/
		
		this.CONSTRUCT=function()
		{
			$(this.elt).tooltip({
					items : ".tooltip, .error-label",
					content: function(){
							return that.content;
					},
					position: {
							my: "center bottom+70",
							at: "center top",
							using: function( position, feedback ) {
								$( this ).css( position );
								$(this).css('cursor','pointer').attr('title','Fermer');
								$(this).on('click',function(){
									that.close();
								});
								$( "<div>" ).addClass( "arrow" ).addClass(feedback.vertical).addClass(feedback.horizontal).appendTo( this );
							}
						}
				});
		}
		
		this.CONSTRUCT();
	}

	/*********************************************************************************************************************/
	/***************************                     HELP                     **********************************/
	/*********************************************************************************************************************/

	var Help = function(elts,descr,prefixe,type)
	{
		this.elements = elts;
		this.descriptions = descr;
		this.tooltips = new Array();
		var that = this; //instance courante en globale
		this.prefixe = prefixe;
		this.type=type;

		this.showAll = function()
		{
			for(var i=0;i<this.tooltips.length;i++)
			{
				this.tooltips[i].show();
			}
		}
		
		this.enableMouseOver = function(bool)
		{
			for(var i=0;i<this.tooltips.length;i++)
			{
				this.tooltips[i].setEnable(bool);
			}
		}
		
		this.closeAll = function()
		{
			for(var i=0;i<this.tooltips.length;i++)
			{
				this.tooltips[i].close();
			}
		}
		
		this.help=function(step)
		{
			$("#"+that.prefixe+" .tooltip:eq("+step+")").tooltip("open");
		}
		
		this.openDialog=function()
		{
			this.closeAll();
			$('#'+this.prefixe+'_dialog').dialog();
		}
		
		this.closeDialog=function()
		{
			$('#'+this.prefixe+'_dialog').dialog("close");
		}
		
		this.CONSTRUCT = function()
		{		
			for(var i=0;i<this.elements.length;i++)
			{
				this.tooltips[i] = new Tooltip(this.elements[i],this.descriptions[i]);
			}

			this.enableMouseOver($('#'+that.prefixe+'_mouseover').is(':checked'));
			
			$('#'+that.prefixe+'_mouseover').on('change',function(){
				that.enableMouseOver($('#'+that.prefixe+'_mouseover').is(':checked'));
			});
			
			this.elements[0].on('focus',function(){
				that.tooltips[0].close();
			});
			
			$('#'+this.prefixe+' .helpDialog').on('click',function(){
				that.openDialog();
			});
			
			$('#'+this.prefixe+'_openAll').on('click',function(){
				that.showAll();
				that.closeDialog();
			});
		}
		
		
		
		this.CONSTRUCT();
	}


	/*********************************************************************************************************************/
	/***************************                     TRANSFORMATION                     **********************************/
	/*********************************************************************************************************************/
	var Transformation = function(elements,prefixe,type,help)
	{
		this.prefixe = prefixe;
		this.elements = elements;
		var that = this;
		this.type=type;
		this.help=help;
		this.alphabet = "abcdefghijklmnopqrstuvwxyz";
		this.trAlphabet = "abcdefghijklmnopqrstuvwxyz";
		this.ponctuation =  ",?;.:/!'-_";
		
		
		/**
			Construit la liste des lettres appartenant au texte sur lequel on veut faire une analyse fréquentielle.
			Les lettres apparaissent dans l'ordre décroissant de leur nombre d'apparition avec un champ pour la substitution
		*/
		this.buildLettersFields = function()
		{
			var count = this.getNbLetters();
			var exReplace = this.getReplacement();
			$('#'+this.prefixe+'_letters').html(""); //vidage conteneur des champs
			var html = '<table class="lettersTable">'; 
			var allZero = false;
			var k = 0;
			while(allZero == false)
			{
				var max = 0;
				var code = 0;
				allZero = true;
				for(var i=1;i<=count.length;i++)
				{
					if(count[i]>max){
						max = count[i];
						code = i+96;
						allZero = false;
					}
				}
				if(max>0){
					if(k%5==0 && k!=0)
					{
						html+= '</table><table class="lettersTable">';
					}
					k++;
					count[code-96]=0;

					html += '<tr>';
						html +=	'<td class="lettersTableCell">'+max+'</td>';
						html +=	'<td class="lettersTableCell"><label for="l_'+String.fromCharCode(code)+'">'+String.fromCharCode(code)+'</label></td>';
						html +=	'<td><input class="letters" maxlength="1" value="'+exReplace[code-96]+'" type="text" id="l_'+String.fromCharCode(code)+'"></td>';
					html +=	'</tr>';
				}
			}
			html+='</table><br style="clear:both;"/>';
			$(html).appendTo('#'+this.prefixe+'_letters'); //remplissange conteneur des champs
		}
		
		this.substitute = function()
		{
			this.buildLettersFields();
			var text = this.elements[0].attr('value').toLowerCase();
			var tr_text="";
			
			for(var i=0;i<text.length;i++)
			{
				if(Controller.isLetter(text.charCodeAt(i))==true)
				{
					var tr = $('#l_'+text.charAt(i)).attr('value');
					if(tr=="")
						tr_text+=text.charAt(i);
					else if(Controller.isLetter(tr.charCodeAt(0)))
						tr_text+=tr;
					else 
						tr_text+=text.charAt(i);
				}
				else
					tr_text+=" ";
			}
			
			$('#'+this.prefixe+'_encryptedText').attr('value',tr_text);
		}
		
		
		this.encode = function()
		{

				this.abc_transform();
				var plainText = this.elements[0].attr('value').toLowerCase();
				var trText = "";

				for(var i=0;i<plainText.length;i++)
				{
					if(Controller.isLetter(plainText.charCodeAt(i)))
					{
						var k=0;
						while(plainText.charAt(i)!=this.alphabet.charAt(k))
						{
							k++;
						}
						trText += this.trAlphabet[k];
					}
					else if(this.ponctuation.indexOf(plainText.charAt(i))!=-1)
						trText += plainText.charAt(i);
					else
						trText += " ";
				}
				$('#'+this.prefixe+'_encryptedText').attr('value',trText);
		}
		
		this.decode = function()
		{

				this.abc_transform();
				var encryptedText = this.elements[0].attr('value').toLowerCase();
				var trText = "";
				for(var i=0;i<encryptedText.length;i++)
				{
					if(Controller.isLetter(encryptedText.charCodeAt(i)))
					{
						var k=0;
						while(encryptedText.charAt(i)!=this.trAlphabet.charAt(k))
						{
							k++;
						}
						trText += this.alphabet[k];
					}
					else if(this.ponctuation.indexOf(encryptedText.charAt(i))!=-1)
						trText += encryptedText.charAt(i);
					else
						trText += " ";
				}
				$('#'+this.prefixe+'_encryptedText').attr('value',trText);
		}
		
		this.swap = function()
		{
			var plainText = this.elements[0].attr('value');
			this.elements[0].attr('value',$('#'+this.prefixe+'_encryptedText').attr('value'));
			$('#'+this.prefixe+'_encryptedText').attr('value',plainText);
		}
		
		this.abc_transform=function()
		{
			if($('#'+this.prefixe+'_key').attr('value').length>0)
				var key = parseInt($('#'+this.prefixe+'_key').attr('value'));
			else {
				var key=0;
			}
			if(!isNaN(key))
			{
				switch(this.prefixe)
				{
					case "shifted" : 
						this.trAlphabet = this.alphabet.substring(this.alphabet.length-(key%26),this.alphabet.length)+this.alphabet.substring(0,this.alphabet.length-(key%26));
						$('#shifted_alphabet').text(this.trAlphabet);
					break;
					case "permuted" : 
						
						Math.seedrandom(""+key); //random avec graine
						var rands = new Array();
						this.trAlphabet = "";
						for(var i=0;i<26;i++)
						{
							var rand = parseInt(Math.random()*25+1); //[1-26]
							var notfound=true;
							if($.inArray(rand,rands)>-1) //si la lettre correspondant à ce nombre au hasard est déjà dans la permutation
							{
								for(var k=rand+1;notfound;k++) //on cherche la plus proche suivante qui n'y est pas
								{
									if($.inArray(k%26,rands)==-1)
									{
										rand = k%26;
										notfound=false;
									}
								}
							}

							rands[i] = rand;
							lettre = String.fromCharCode(rand+97);
							this.trAlphabet += lettre;
						}
						$('#permuted_alphabet').text(this.trAlphabet);
					break;
				}
			}
		}
		
		this.getNbLetters = function()
		{
			var text = this.elements[0].attr('value').toLowerCase();
			var count = new Array();
			for(var i=0;i<=26;i++) count[i]=0;

			for(var i=0;i<text.length;i++)
			{
				count[text.charCodeAt(i)-96]++;
			}
			return count;
		}
		
		this.getReplacement = function()
		{
			var letters = this.getNbLetters();
			var replacements = new Array();
			for(var i=0;i<=26;i++) replacements[i]="";
			
			for(var i=1;i<letters.length;i++)
			{
				if(letters[i]>0 && $('#l_'+String.fromCharCode(i+96)).length==1) {
					replacements[i] = $('#l_'+String.fromCharCode(i+96)).attr('value');
				}
			}
			return replacements;
		}

		this.CONSTRUCT = function()
		{
			if(this.prefixe=='shifted' || this.prefixe=='permuted')
				this.abc_transform();
		}
		
		this.CONSTRUCT();
	}
	
	/*********************************************************************************************************************/
	/***************************                     BRUTE FORCE                    **********************************/
	/*********************************************************************************************************************/
	
	var BruteForce = function(transformation)
	{
		this.transformation = transformation;
		this.prefixe = transformation.prefixe;
		this.elements = transformation.elements;
		this.type=transformation.type;
		var that = this;
		this.key=0;
		
		this.stopState = false;
		
		this.ite = function(){
		
			if(this.key>=26 || this.key<0)
			{
				this.stop();
			}
			
			if(!this.stopState)
			{
				$('#'+that.prefixe+'_key').attr('value',that.key);
				that.transformation.abc_transform();
				that.transformation.decode();
				
				setTimeout(function(){
					that.key++;
					that.ite();
				},1000);
			}
			else{
				that.key--;
			}
		}
		
		this.stop = function()
		{
			this.stopState=true;
		}
		
		this.go = function()
		{
			this.key=0;
			this.stopState=false;
			this.ite();
		}
		
		this.previous = function()
		{
			if(this.key>0)
			{
				this.key--;
				$('#'+that.prefixe+'_key').attr('value',that.key);
				that.transformation.abc_transform();
				that.transformation.decode();
			}
		}
		
		this.next = function()
		{
			if(this.key<26)
			{
				this.key++;
				$('#'+that.prefixe+'_key').attr('value',that.key);
				that.transformation.abc_transform();
				that.transformation.decode();
			}
		}
	}
	
	/*********************************************************************************************************************/
	/***************************                     KNOWNPLAINTEXT                     **********************************/
	/*********************************************************************************************************************/
	
	var KnownPlainText = function(transformation)
	{
		this.transformation = transformation;
		this.prefixe = transformation.prefixe;
		this.elements = transformation.elements;
		this.type=transformation.type;
		var that = this;
		
		this.attackCesar = function()
		{
			var knownText = $('#shifted .knownPlainText').attr('value');
			var text = this.elements[0].attr('value').toLowerCase();
			var matchKey = new Array();
			var matchWord = new Array();
			var nb=0;
			
			for(var i=0;i<text.length-knownText.length+1;i++)
			{
				var match = true;
				var ref =  text[i].charCodeAt(0) - knownText[0].charCodeAt(0);
				ref = ref<0 ? Math.abs(ref) : 26-ref;
				var word = text[i];
				for(var k=1;k<knownText.length;k++)
				{
					if(Controller.isLetter(knownText[k].charCodeAt(0))){	
						var diff =  text[i+k].charCodeAt(0) - knownText[k].charCodeAt(0);
						diff = diff<0 ? Math.abs(diff) : 26-diff;
						if(diff != ref) 
							var match=false;
					}
					else{
						if(knownText[k]!=text[i+k])
							var match=false;
					}
					word+=text[i+k];
				}
				
				if(match)
				{
					matchKey[nb] = ref;
					matchWord[nb] = word;
					nb++;
				}
			}
			
			if(matchKey.length==0)
			{
				$('<div title="Résultat">'+no_match+'</div>').dialog({modal:true});
			}
			else if(matchKey.length==1)
			{
				$('<div title="Résultat">La clé est '+matchKey[0]+'.<br />Le texte "'+knownText+'" chiffré est "'+matchWord[0]+'".</div>').dialog({modal:true});
				$('#'+that.prefixe+'_key').attr('value',matchKey[0]);
				this.transformation.decode();
			}
			else
			{
				$('<div title="Résultat">'+several_match+'</div>').dialog({modal:true});
			}
		}
		
		this.attackPermutation = function()
		{
			var knownText = $('#permuted .knownPlainText').attr('value');
			var text = this.elements[0].attr('value').toLowerCase();
			var matchKey = new Array();
			var matchWord = new Array();
			var matchIndex = new Array();
			var nb=0;
			
			for(var i=0;i<text.length-knownText.length+1;i++)
			{
				if(i==0 || text[i-1]==" " || text[i]==" " || this.transformation.ponctuation.indexOf(text[i+1])!=-1)
				{
					
					var match = true;
					var word = "";
					for(var k=0;k<knownText.length;k++)
					{
						if(!Controller.isLetter(knownText[k].charCodeAt(0)) || !Controller.isLetter(text[i+k].charCodeAt(0))){	
							if(knownText[k]!=text[i+k])
								var match=false;
						}
						word+=text[i+k];
					}

					if(match && (i==text.length-knownText.length || text[i+k]==" " || text[i+k-1]==" " || this.transformation.ponctuation.indexOf(text[i+k])!=-1))
					{
						var equal = false;
						for(var m=0;m<matchWord.length;m++)
						{
							if(matchWord[m]==word)
							{
								equal = true;
							}
						}
						
						if(!equal)
						{
							matchWord[nb] = word;
							matchIndex[nb]=i;
							nb++;
						}
					}
				}
			}
			
			if(matchWord.length==0)
			{
				$('<div title="Résultat">'+no_match+'</div>').dialog({modal:true});
			}
			else if(matchWord.length==1)
			{
				
				var clearValues = knownText.charAt(0);
				var encryptedValues= text.charAt(matchIndex[0]);
				for(var i=0;i<knownText.length;i++)
				{
					if(knownText.charAt(i)!=" " && this.transformation.ponctuation.indexOf(knownText.charAt(i))==-1 && clearValues.indexOf(knownText.charAt(i))==-1)
					{
						var k=-1;
						while(clearValues.charCodeAt(k+1)<knownText.charCodeAt(i))
						{	
							k++;
						}
						
						clearValues = clearValues.substring(0,k+1)+knownText.charAt(i)+clearValues.substring(k+1,clearValues.length);
						encryptedValues = encryptedValues.substring(0,k+1)+text.charAt(matchIndex[0]+i)+encryptedValues.substring(k+1,encryptedValues.length);
					}
				}
				var ligne1='<tr>';
				var ligne2 = '<tr>';
				for(var i=0;i<clearValues.length;i++)
				{
						ligne1 += '<td class="keyResult alphabet">'+clearValues.charAt(i)+'</td>';
						ligne2 += '<td class="keyResult alphabet">'+encryptedValues.charAt(i)+'</td>';
				}
				ligne1 +='</tr>';
				ligne2 += '</tr>';
				
				$('<div title="Résultat">Une correspondance a été trouvée. Le texte "'+knownText+'" chiffré est "'+matchWord[0]+'". La clé partiellement déchiffrée est : <table class="lettersTableResult">'+ligne1+ligne2+'</table></div>').dialog({modal:true});
			}
			else
			{
				$('<div title="Résultat">'+several_match+'</div>').dialog({modal:true});
			}
		}
	
	}
	
	/*********************************************************************************************************************/
	/***************************                     CONTROLLER                     **************************************/
	/** Dépendances : Transformation, Help, Tooltip, ForceBrute, KnownPlainText **/
	/*********************************************************************************************************************/
	var Controller = function(elements,descriptions,prefixe,type)
	{
		var that = this;
		this.elements = elements;
		this.prefixe = prefixe;
		this.type=  type;
		this.help = new Help(this.elements,descriptions,this.prefixe,this.type);
		this.transformation = new Transformation(this.elements,this.prefixe,this.type);
		
		this.erreur=function(elt,texte,open)
		{
			$(elt).tooltip("option","content",'<div class="ui-state-error" style="border:none;"><span class="ui-icon ui-icon-alert" style="float:left;margin-right:10px;"></span></div>'+texte);
			if(open==true) $(elt).tooltip("open");
		}
		
		this.isEmpty=function(elt)
		{
			return $(elt).attr('value').length==0;
		}
		
		this.getStep=function()
		{
			var step = 0;
			if(this.checkPlainText(this.elements[0])==0 && !this.isEmpty(this.elements[0])){
				step++;
				if(this.type=='chiffrage')
				{
					if(this.checkKey(this.elements[1])==0 && !this.isEmpty(this.elements[1]))
						step++;
				}	
			}
			return step;
		}
		
		this.checkPlainText = function(elt)
		{
			var text = $(elt).attr('value').toLowerCase();
			var erreurs=0;
			var words="[";
			for(var i=0;i<text.length; i++)
			{
				if(!this.isCorrect(text.charAt(i)))
				{
					words+=text.charAt(i)+""
					erreurs++;
				}	
			}
			var s = erreurs>1 ? "s" : "";
			words+="]";
			if(erreurs>0){
				that.erreur($(elt),"Le texte comporte "+erreurs+" caractère"+s+" incompatible"+s+". Il doit contenir uniquement des lettres.");
			}
			return erreurs;
		}
		
			
		this.checkKey = function(elt)
		{
			if(isNaN($(elt).attr('value')))
			{
				that.erreur(this.elements[1],error_key);
				return 1;
			}
			return 0;
		}
		
		Controller.isLetter=function(code)
		{
			return (code>=97 && code <=122)  //10 : retour à la ligne ; 32 : espace
		}
		
		this.isCorrect=function(str)
		{
			var ponctuation = ",?;.:/!'-_";
			
			for(var i=0;i<str.length;i++)
			{
				var code = str.charCodeAt(i);
				if(!(code==10 || code==32 || (code>=97 && code <=122) || ponctuation.indexOf(String.fromCharCode(code))>-1))
					return false;
			}
			return true;
		}
		
		this.isLetter = function (code)
		{
			return Controller.isLetter(code);
		}
		
		this.CONSTRUCT = function()
		{
			//texte avant transformation
			this.elements[0].on('blur',function(){
				that.help.tooltips[0].reset();
				var erreurs = that.checkPlainText($(this));
				if(erreurs>0){
					$(this).tooltip("open");
					$(this).on('focus',function(){
						$(that.help.tooltips[0].close());
					});
				}
			});
			
			//clic sur l'aide
			$('#'+this.prefixe+' .help').on('click',function(){
				that.help.help(that.getStep());
			});
			
			//type chiffrage
			if(this.type=="chiffrage")
			{
				//champ des clefs
				this.elements[1].on('blur',function(){
					that.help.tooltips[1].reset();
					var erreurs = that.checkKey($(this));
					if(erreurs>0){
						$(this).tooltip("open");
						$(this).on('focus',function(){
							$(that.help.tooltips[1].close());
						});
					}
					else
					{
						that.transformation.abc_transform();
					}
				}).on('keyup',function(){
					that.transformation.abc_transform();
				}).on('focus',function(){
					that.help.tooltips[1].close();
				});
				
				//bouton encode
				$('#'+this.prefixe+'_buttonsArea .encode').on('click',function(){
					if(that.isEmpty(that.elements[0]) || that.isEmpty(that.elements[1]))
						that.help.help(that.getStep());
					else
						that.transformation.encode();
				});
				
				//bouton decode
				$('#'+this.prefixe+'_buttonsArea .decode').on('click',function(){
							
					if(that.isEmpty(that.elements[0]) || that.isEmpty(that.elements[1]))
						that.help.help(that.getStep());
					else
						that.transformation.decode();
				});
				
				//bouton swap
				$('#'+this.prefixe+'_buttonsArea .swap').on('click',function(){		
						that.transformation.swap();
				});
				
				if(this.prefixe=='shifted')
				{
					//attaque à texte clair connu
					$('#shifted .kpa').tooltip({items : 'span', content:function(){
							return kpta_descr;
						}
					});
					var knownPlainText = new KnownPlainText(this.transformation);
					$('#shifted .knownPlainTextSubmit').on('click',function(){
						if(that.isEmpty(that.elements[0]) || that.isEmpty(that.elements[3]))
						{
							if(that.isEmpty(that.elements[0]))
								that.elements[0].tooltip("open");
							if(that.isEmpty(that.elements[3]))
								that.elements[3].tooltip("open");
						}
						else if(!that.isCorrect(that.elements[3].attr('value')))
						{
							that.erreur(that.elements[3],error_kpt,true);
						}
						else
							knownPlainText.attackCesar();
					});
				}
				else if(this.prefixe=='permuted')
				{
						//attaque à texte clair connu
					$('#permuted .kpa').tooltip({items : 'span', content:function(){
							return kpta_descr;
						}
					});
				
					var knownPlainText = new KnownPlainText(this.transformation);
					$('#permuted .knownPlainTextSubmit').on('click',function(){
						if(that.isEmpty(that.elements[0]))
							that.help.help(that.getStep());
						else
							knownPlainText.attackPermutation();
					});
				}
				
				if(this.prefixe=='shifted')
				{
					$('#shifted .fba').tooltip({items : 'span', content:function(){
							return bf_descr;
						}
					});
					//attaque force brute
					var bruteForce = new BruteForce(this.transformation);
					
					//bouton Lancer
					$('#'+this.prefixe+' .brute_force_go').on('click',function(){
						if(that.isEmpty(that.elements[0]))
							that.help.help(0);
						else
						{
							bruteForce.go();
							$(this).attr('disabled','disabled');
							$('#'+that.prefixe+' .brute_force_previous').attr('disabled','disabled');
							$('#'+that.prefixe+' .brute_force_next').attr('disabled','disabled');
							$('#'+that.prefixe+' .brute_force_stop').removeAttr('disabled');
							
						}
					});
					
					//bouton Arrêter
					$('#'+this.prefixe+' .brute_force_stop').on('click',function(){
						bruteForce.stop();
						$(this).attr('disabled','disabled');
						$('#'+that.prefixe+' .brute_force_go').removeAttr('disabled');
						$('#'+that.prefixe+' .brute_force_previous').removeAttr('disabled');
						$('#'+that.prefixe+' .brute_force_next').removeAttr('disabled');
					});
					
					//bouton < (précédent)
					$('#'+this.prefixe+' .brute_force_previous').on('click',function(){
						if(that.isEmpty(that.elements[0]))
							that.help.help(0);
						else
						{
							bruteForce.previous();
						}
					});
					
					//bouton > (suivant)
					$('#'+this.prefixe+' .brute_force_next').on('click',function(){
						if(that.isEmpty(that.elements[0]))
							that.help.help(0);
						else
						{
							bruteForce.next();
						}
					});
				}
				
				
			}
			else if(this.type=="freq_ana")
			{
				//dans le cas de l'analyse fréquentielle
				this.elements[0].on('keyup',function(){
					that.transformation.buildLettersFields();
				}).on('blur',function(){
					that.transformation.buildLettersFields();
				});
				
				
				//bouton appliquer substitutions
				$('#'+this.prefixe+' #freq_ana_substitute').on('click',function(){
					if(that.isEmpty(that.elements[0]))
					{
						that.help.help(0);
					}
					else
						that.transformation.substitute();
				});
			}
		}
		
		this.CONSTRUCT();
	}

	/*********************************************************************************************************************/
	/***************************                     ENTRY                 **********************************/
	/*********************************************************************************************************************/
		
		//première partie : chiffe de César

		var s_control = new Controller(s_elts,s_descr,s_pre,s_type);
		
		//deuxième partie : chiffrage par permutation
		
		var p_control = new Controller(p_elts,p_descr,p_pre,p_type);
		
		//troisième partie : analyse fréquentielle
		
		var fa_control = new Controller(fa_elts,fa_descr,fa_pre,fa_type);
});