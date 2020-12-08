jQuery.noConflict();

/** ====================== **/
/** ===== PARAMETRES ===== **/
/** ====================== **/

var display = 0; // Mode d'affichage par défaut
var couleurDefaut = '#58c3f0';
var couleurFocus = '#eb9b00';
var couleurFocus2 = '#b0832c';
var couleurValide = '#a8d031';
var couleurMax = '#ff0000';

// Objets jQuery généraux
var canvas = document.getElementById('visCanvas');
var boutonVisuel = jQuery('#boutonVisuel');
var boutonTemporel = jQuery('#boutonTemporel');
var boutonJournal = jQuery('#boutonJournal');

// Objets jQuery de la partie visuelle
var spanCopies = jQuery('#visNbCopies');
var spanComparaisons = jQuery('#visNbComparaisons');
var visChoixTri = jQuery('#visChoixTri');
var visChoixAccelere = jQuery('#visChoixAccelere');
var visBoutonStart = jQuery('#visBoutonStart');
var visBoutonStep = jQuery('#visBoutonStep');
var visBoutonRestart = jQuery('#visBoutonRestart');
var visHint0 = jQuery('#visHint0');
var visHint1 = jQuery('#visHint1');
var visHint2 = jQuery('#visHint2');

// Objets jQuery de la partie temporelle
var tempTailleTab = jQuery('#tempTailleTab');
var tempNbTab = jQuery('#tempNbTab');
var tempChoixTri = jQuery('#tempChoixTri');
var tempBoutonStart = jQuery('#tempBoutonStart');
var tempResultats = jQuery('#tempResultats');

// Objets jQuery du journal
var logContent = jQuery('#logContent');
var logBoutonReset = jQuery('#logBoutonReset');
var logBoutonCopier = jQuery('#logBoutonCopier');

/** ============================== **/
/** ===== OBJETS AFFICHABLES ===== **/
/** ============================== **/

// Le texte "Tableau à trier" qui s'affiche sur le canvas dans la partie supérieure
var textTab = new createjs.Text('Tableau à trier', 'bold 12px sans-serif', '#000000');
textTab.x = 225;
textTab.y = 130;
textTab.alpha = 0.8;
textTab.textAlign = 'center';

// Le cadre noir délimitant le tableau à trier dans la partie supérieure du canvas
var cadreTab = new createjs.Shape();
cadreTab.graphics.beginStroke("#000000").moveTo(9,123).lineTo(442,123).endStroke();
for (var i = 0 ; i<17 ; i++)
{
	cadreTab.graphics.beginStroke('#000000').moveTo(9+27*i,123).lineTo(9+27*i,100).endStroke();
}

// Le cadre du tableau temporaire pour le tri fusion, identique au premier cadre mais dans la partie inf?eure du canvas
var cadreTemp = cadreTab.clone();
cadreTemp.y = 150;

// Le cadre de la case temporaire pour les 4 autres types de tri
var cadreTemp2 = new createjs.Shape();
cadreTemp2.graphics.beginStroke('#000000').moveTo(211,250).lineTo(211,273).lineTo(239,273).lineTo(239,250).endStroke();

// Le texte "Zone temporaire" qui s'affiche dans la partie inférieure du canvas
var textTemp = new createjs.Text('Zone temporaire', 'bold 12px sans-serif', '#000000');
textTemp.x = 225;
textTemp.y = 280;
textTemp.alpha = 0.8;
textTemp.textAlign = 'center';

/** ===================== **/
/** ===== FONCTIONS ===== **/
/** ===================== **/

// function zap : int -> void
// Change le mode d'affichage du grain :
//	* 0 : Tri visuel
//	* 1 : Tri temporel
//	* 2 : Journal
function zap (n)
{
	n == 0 ? jQuery("#visuel").show() : jQuery("#visuel").hide();
	n == 1 ? jQuery("#temporel").show() : jQuery("#temporel").hide();
	n == 2 ? jQuery("#journal").show() : jQuery("#journal").hide();
	display = n;
}

// function newSet : int -> (int array * Container array)
// Retourne un ensemble aléatoire de valeurs à trier. Celui-ci est sous la forme d'un littéral contenant deux tableaux :
//	* valeur : le tableau des valeurs trier, ordonnées aléatoirement
//	* affichage : tableau contenant les représentations graphiques des valeurs du tableaux, triées par valeur croissante (affichages[n] représente la valeur n).
// L'argument facultatif taille permet de choisir la taille des données à trier. Par défaut il vaut 16. Si celui-ci est précisé, le tableau des représentations n'est pas renvoyé (dans ce cas, nous sommes en mode temporel, il est inutile).
function newSet (taille)
{
	var valeurs = [];
	var affichages = [];
	var b = typeof taille === 'undefined'; // b (pour boolean) indique si il faut renvoyer les représentations
	var t = !b ? taille : 16; // Taille par défaut : 16
	var nDispos = []; // nDispos contient les valeurs disponibles au tirage au sort, on l'initialise avec toutes les valeurs de 1 à t
	for (var i = 0 ; i<t ; i++)
	{
		nDispos[i]=i+1;
	}
	for (var i = 0 ; i<t ; i++)
	{
		// On choisit aléatoirement la valeur du ième élément dans nDispos
		// Javascript ne dispose pas d'une méthode permettant de supprimer directement un élément d'un tableau, j'utilise donc un petit tour de passe-passe (pas des plus efficaces) :
		var r = Math.floor(Math.random()*(t-i));
		for (var j = 0 ; j < r ; j++)
		{
			nDispos.push(nDispos.shift());
		}
		var n = nDispos.shift();
		
		if (b) // Traité uniquement si les représentations graphiques sont nécesaires
		{
			// Le conteneur contient 2 éléments à afficher : la barre (shape) et la valeur correspondante(text, n).
			var conteneur = new createjs.Container();
			var barre = new createjs.Shape();
				barre.graphics.beginFill(couleurDefaut).drawRect(0,0,20,6*n);
				barre.x = 0;
				barre.y = -6*n;
			var texte = new createjs.Text(n, "bold 12px sans-serif", "#000000");
				texte.x = 10;
				texte.y = -(6*n + 12);
				texte.alpha = 0.6;
				texte.textAlign = "center";
			
			// C'est le container qu'on déplacera et non pas la barre ou le texte séparément. Ce sont donc ses propriétés x et y qui nous intéressent pour le positionner.
			conteneur.addChild(barre,texte);
			conteneur.x = 13 + 27*i;
			conteneur.y = 120;
			
			affichages[n] = conteneur;
		}
		
		// Le tableau des valeurs est deux fois plus grand que la taille demandée pour permettre d'effectuer l'algorithme fusion. Les valeurs de t à 2t+1 sont des zones temporaires initialisées à 0.
		valeurs[i] = n;
		valeurs[i+t] = 0;
	}
	valeurs[2*t] = 0; // Valeur temp
	return {valeur:valeurs,affichage:affichages};
}

// function log : string -> void
// Cette fonction prend en argument une chaîne de caractères et l'ajoute au journal.
function log (message)
{
	logContent.append('<p>'+message+'</p>');
}

/** =========================== **/
/** ===== METHODES DE TRI ===== **/
/** =========================== **/

// La classe Tri contient toutes les propriétés et méthodes utiles gérer l'ensemble à trier et le trier.
function Tri (methode, temp, taille)
{
	// Initialisation
	this.taille = (typeof taille === 'number') ? taille : 16; // Taille par défaut : 16
	this.set = (typeof taille === 'number') ? newSet(taille) : newSet();
	this.espaceVide = 2*this.taille; // L'espace vide est l'endroit ou sera déplacé un élément avec la méthode "deplacer". Lors de l'initialisation il s'agit de la zone temporaire.
	this.copies = 0;
	this.comparaisons = 0;
	this.actions = new Array(); // Liste des actions visuelles à effectuer, vide lors de l'initialisation
	this.nbActions = 0; // Longueur de la liste "actions"
	this.derniereAnim = 0; // Instant (en ms) auquel a eu lieu la dernière animation (ou action visuelle)
	
	// Mode de fonctionnement
	this.accelere = false; // Mode de lecture normal par défaut
	this.modeTemporel = (typeof temp === 'boolean') ? temp : false; // Il est utile de savoir dans quel mode d'affichage on se situe pour certaines méthodes.
	this.type = (typeof methode === 'string') ? methode : '5'; // Tri par sélection par défaut, sinon on utilise la valeur passée en argument (de type string).
	this.pasAPas = false; // Mode pas à pas désactivé lors de l'initialisation
	
	// function init : void -> void
	// Réalise les opérations d'initialisation graphique lors de la génération d'un nouveau tri.
	this.init = function()
	{
		// Nettoyage du canvas
		stage.clear();
		stage.removeAllChildren();
		visBoutonStart.attr('value','Commencer');
		// Nettoyage des indicateurs de comparaisons et de copies
		spanComparaisons.text('0');
		spanCopies.text('0');
		// Mise à jour du type de tri et du mode de lecture
		this.type = visChoixTri.val();
		this.accelere = visChoixAccelere.attr('checked');
		// Remplissage du canvas
		stage.addChild(textTab,textTemp,cadreTab);
		stage.addChild(this.type == 4 ? cadreTemp : cadreTemp2);
		for (var i = 1 ; i<17 ; i++)
		{
			stage.addChild(this.set.affichage[i]);
		}
		// Réinitialisation de la zone d'indications : on n'affiche que le texte "Cliquez sur ... pour commencer"
		visHint0.show();
		visHint1.hide().text('');
		visHint2.hide().text('');
	}
	
	/** Méthodes d'animations **/
	
	// function tick : void -> void
	// Cette méthode est appelée par le ticker toutes les 10ms (=1/100fps) et appelle la méthode d'exécution des animations (doAction) avec une période donnée (multiple de 10ms).
	this.tick = function()
	{
		var time = createjs.Ticker.getTime();
		var delta = this.accelere ? 100 : 1000; // Période d'appel de doAction, si ce n'est pas un multiple de 10ms la premiére valeur supérieure multiple de 10ms sera retenue.
		// L'appel n'est effectué que si il reste des animations à traiter, si un temps suffisant s'est écoulé depuis la dernière animation et si on n'est pas en mode pas à pas.
		if (this.nbActions > 0 && time >= this.derniereAnim + delta && !this.pasAPas)
		{
			if (this.doAction() < 2) this.derniereAnim = time; // On met à jour le temps de dernière exécution d'une animation si besoin.
		}
	}
	
	// function addAction : litteral -> void
	// Cette méthode insère une animation dans la file d'actions. Une animation est représentée par un litteral dont les identifiants varient suivant le type d'action :
	//	* type : contient le type de l'animation sous forme d'un string ('colorier', 'deplacer', 'incrCopies', 'incrComparaisons', activerHints', 'text1', 'text2', 'pause'). Cet identifiant est _toujours_ pr?nt.
	//	* n : pour les actions Colorier et Déplacer, il représente la _valeur_ de l'élément à modifier (et non pas son indice). Pour les actions incrCopies et incrComparaisons il s'agit de la valeur ?lacer dans la zone de texte.
	//	* c : pour l'action Colorier il s'agit de la couleur (en hexadecimal par exemple) à utiliser pour colorier.
	//	* m : pour l'action Déplacer c'est la position à donner à l'élément dans le tableau (première ligne : 0 à 15 ; seconde ligne : 16 à 31 ; valeur temporaire : 32).
	//	* text : pour les actions Text1 et Text2 il s'agit du texte à placer dans la zone de texte.
	//	* r : valeur à retourner après l'exécution de l'action. La valeur par défaut est 0, voir la méthode doAction pour plus de précisions.
	// En mode temporel les animations ne sont pas effectuées, on ne les ajoute pas à la file.
	this.addAction = function(action)
	{
		if (!this.modeTemporel)
		{
			this.actions.push(action);
			this.nbActions ++;
		}
		return true;
	}
	
	// function doAction : void -> int
	// Effectue la première animation de la file this.actions.
	// Retourne un entier permettant de préciser si l'animation effectuée doit être succéder d'une pause en mode pas à pas ou bien si l'animation suivante doit être exécutée immédiatement après en mode de lecture normal ou accéléré.
	this.doAction = function()
	{
		var action = this.actions.shift();
		this.nbActions --;
		switch (action.type)
		{
			case 'colorier':
				// EaselJS ne propose pas (à ma connaissance) de méthode pour changer la couleur d'un objet Shape, on recolorie donc par dessus l'ancien rectangle.
				this.set.affichage[action.n].getChildAt(0).graphics.beginFill(action.c).drawRect(0,0,20,6*action.n);
			break;
			
			case 'deplacer':
				// Position de l'élément suivant la valeur de m.
				var xpos = action.m<32 ? 13 + 27*(action.m % 16) : 215;
				var ypos = action.m<16 ? 120 : 270;
				// Animation de l'élément grace au framework TweenJS. J'utilise la fonction sineOut pour le déplacement, modifiable à souhait.
				createjs.Tween.get(this.set.affichage[action.n],{override:true}).to({x:xpos,y:ypos},(this.accelere ? 200 : 700),createjs.Ease.sineOut);
				// Ici la valeur de retour par défaut est différente des autres éléments (une pause après chaque déplacement est souhaitable en mode pas à pas), on force donc un peu (ne pas mettre la même forme qu'en fin de méthode car 0 || 1 = 1 ...):
				return (typeof action.r === 'number') ? action.r : 1;
			break;
			
			case 'incrCopies':
				// Une simple mise à jour de la valeur.
				spanCopies.text(action.n);
			break;
			
			case 'incrComparaisons':
				// Idem
				spanComparaisons.text(action.n);
			break;
			
			case 'activerHints':
				// Cette action n'est appelée qu'au tout début pour changer le texte de la hintbox.
				visHint0.hide();
				visHint1.show();
				visHint2.show();
				return 2;
			break;
			
			case'text1':
				// Mise à jour du texte du haut de la hintbox
				visHint1.text(action.text);
			break;
			
			case 'text2':
				// Mise à jour du texte du bas de la hintbox
				visHint2.text(action.text);
			break;
			
			case 'pause':
				//Permet de maitriser les arrêts de la méthode "pas à pas"
				return 1;
			break;
		}
		// Valeur de retour (action.r) :
		//	* 0 : défaut
		//	* 1 : pause en mode pas à pas
		//	* 2 : exécution immédiate de l'action suivante
		return action.r || 0;
	}
	
	/** Opérations algorithmiques **/
	
	// function incrCopies : bool -> void
	// Met à jour le nombre de copies effectuées lors de l'opération de triage. Aussi bien en mémoire que sur l'affichage.
	// Lorsqu'elle est appelée avec l'argument true l'animation qu'elle enregistre est immédiatement suivi de l'action qui la suit.
	this.incrCopies = function(b)
	{
		this.copies ++;
		this.addAction({type:'incrCopies',n:this.copies,r:b ? 2 : 0});
	}
	
	// Idem
	this.incrComparaisons = function(b)
	{
		this.comparaisons ++;
		this.addAction({type:'incrComparaisons',n:this.comparaisons,r:b ? 2 : 0});
	}
	
	// function deplacer : int -> int -> int -> void
	// Effectue les opérations nécessaires lors du déplacement d'un élément dans le tableau. En mémoire et visuellement. Arguments :
	//	* n : indice dans le tableau de l'élément à déplacer (0-32)
	//	* m : indice dans le tableau de l'emplacement d'arrivée de l'élément. Si celui-ci n'est pas précisé on déplace vers l'espace vide.
	//	* r : retour que doit produire l'appel de doAction lors du traitement de l'animation.
	this.deplacer = function(n,m,r)
	{
		m = (m >= 0 && m <= this.taille*2) ? m : this.espaceVide; // Valeur par défaut de m : espaceVide
		
		// Animation
		this.addAction({type:'deplacer',n:this.set.valeur[n],m:m,r:(typeof r === 'number') ? r : 1});
		
		// Déplacement dans le tableau
		if (this.set.valeur[m] != 0) return false; // On ne déplace pas vers un emplacement déjà utilisé
		this.set.valeur[m] = this.set.valeur[n];
		this.set.valeur[n] = 0;
		this.incrCopies(r==2); // Si r = 2 l'animation de la copie doit elle aussi être immédiate
		this.espaceVide = n;
	}
	
	// function echanger : int -> int -> void
	// Echange les positions des éléments d'indice n et m du tableau à trier.
	this.echanger = function(n,m)
	{
		// n est envoyé vers l'espace vide (temp)
		this.deplacer(n);
		// m est envoyé vers le nouvel espace vide (n)
		this.deplacer(m);
		// l'élément dans la zone temporaire est envoyé vers le nouvel espace vide (m)
		this.deplacer(this.taille*2);
	}
	
	/** Méthodes de tri **/
	
	// function selection : void -> boolean
	// Trie le tableau suivant la méthode du tri par sélection
	this.selection = function()
	{
		var indexMax = 0;
		for (var i = 0; i<this.taille ; i++) // i correspond au nombre d'éléments bien posotionnés (en fin de tableau)
		{
			this.addAction({type:'text1',text:'Phase '+(i+1)+' : trouvons le plus grand élément et déplaçons-le à la position '+(16-i)});
			this.addAction({type:'text2',text:'Pour l\'instant, le premier élément est le maximum.'});
			indexMax = 0;
			this.addAction({type:'colorier',n:this.set.valeur[0],c:couleurMax,r:1});
			// On recherche le maximum entre les positions 0 et taille-i
			for (var j = 1 ; j<this.taille-i ; j++)
			{
				this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurFocus});
				if (this.set.valeur[j] > this.set.valeur[indexMax])
				{
					this.addAction({type:'text2',text:'L\'élément '+(j+1)+' est plus grand que l\'élément '+(indexMax+1)+', il devient donc le max.'});
					this.addAction({type:'colorier',n:this.set.valeur[indexMax],c:couleurDefaut});
					this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurMax});
					indexMax = j;
				}
				else
				{
					this.addAction({type:'text2',text:'L\'élément '+(j+1)+' est plus petit que l\'élément '+(indexMax+1)+'.'});
				}
				this.incrComparaisons();
				this.addAction({type:'pause'});
				if (j != indexMax) this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurDefaut});
			}
			// On échange le maximum avec le dernier élément mal placé.
			this.addAction({type:'text2',text:'Permutons l\'élément '+(16-i)+' avec le maximum (élément '+(indexMax+1)+').'});
			if (indexMax != this.taille-1-i)
			{
				this.echanger(this.taille-1-i,indexMax);
			}
			this.addAction({type:'colorier',n:this.set.valeur[this.taille-1-i],c:couleurValide});
		}
		return true;
	}
	
	// function propagation : void -> boolean
	// Trie le tableau suivant la méthode du tri par propagation
	this.propagation = function()
	{
		for (var i = 0 ; i<this.taille ; i++) // i = nombre d'éléments bien positionnés
		{
			this.addAction({type:'text1',text:'Phase '+(i+1)+' : le plus grand élément se place en position '+(16-i),r:1});
			// On compare les éléments 2 à 2 et on déace le plus grand vers la fin du tableau
			for (var j = 0 ; j < this.taille-1-i ; j++)
			{
				this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurFocus,r:2});
				this.addAction({type:'colorier',n:this.set.valeur[j+1],c:couleurFocus});
				if (this.set.valeur[j] > this.set.valeur[j+1])
				{
					this.addAction({type:'text2',text:'L\'élément '+(j+1)+' est plus grand que l\'élément '+(j+2)+' donc on les permute.',r:1});
					this.echanger(j,j+1);
				}
				else
				{
					this.addAction({type:'text2',text:'L\'élément '+(j+1)+' est plus petit que l\'élément '+(j+2)+' donc on ne les permute pas.',r:1});
				}
				this.incrComparaisons();
				this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurDefaut,r:2});
				this.addAction({type:'colorier',n:this.set.valeur[j+1],c:couleurDefaut});
			}
			// Le dernier élément est bien placé
			this.addAction({type:'colorier',n:this.set.valeur[this.taille-1-i],c:couleurValide});
		}
		return true;
	}
	
	// function insertion : void -> void
	// Trie le tableau suivant la méthode du tri par insertion
	this.insertion = function()
	{
		this.addAction({type:'colorier',n:this.set.valeur[0],c:couleurValide});
		this.addAction({type:'text1',text:'La partie du tableau verte (seulement l\'élément 1 pour l\'instant) est correctement triée.',r:1});
		for (var i = 0 ; i<this.taille-1 ; i++) // i = dernier élément de la partie triée
		{
			this.addAction({type:'colorier',n:this.set.valeur[i+1],c:couleurFocus});
			this.addAction({type:'text1',text:'Phase '+(i+1)+' : insérons l\'élément '+(i+2)+' dans la partie triée.'});
			this.addAction({type:'text2',text:'Plaçons l\'élément '+(i+2)+' dans la zone temporaire.'});
			this.deplacer(i+1);
			var j = i;
			// On déplace les éléments triés jusqu'à en trouver un plus petit que l'élément à insérer
			while (j>=0 && this.set.valeur[2*this.taille] < this.set.valeur[j])
			{
				this.incrComparaisons();
				this.addAction({type:'text2',text:'L\'élément '+(j+1)+' est plus grand que l\'élément temporaire, on le déplace en position '+(j+2)+'.'});
				this.deplacer(j);
				j--;
			}
			// On place l'élement à trier.
			this.addAction({type:'text2',text:j==-1 ? 'L\'élément temporaire est le plus petit, on le copie en position 1.' : 'L\'élément temporaire est plus grand que que l\'élément '+(j+1)+', on a donc trouvé sa position.',r:1});
			this.incrComparaisons();
			this.deplacer(2*this.taille);
			this.addAction({type:'colorier',n:this.set.valeur[j+1],c:couleurValide,r:1});
		}
		return true;
	}
	
	// function rapide : int -> int -> boolean
	// Trie le sous-tableau d'indices compris entre debut et fin suivant la méthode du tri rapide.
	// Cette méthode est récursive.
	this.rapide = function (debut,fin)
	{
		this.addAction({type:'text1',text:'On applique le tri rapide aux éléments de '+(debut+1)+' à '+(fin+1)+'.'});
		this.addAction({type:'text2',text:'L\'élément '+(fin+1)+' sert de pivot.'});
		this.addAction({type:'colorier',n:this.set.valeur[fin],c:couleurMax,r:1});
		// La dernière valeur du sous-tableau servira de valeur pivot.
		var pivot = this.set.valeur[fin];
		// pos correspond à la position que doit prendre la valeur pivot à la fin de l'algorithme
		var pos = debut;
		for (var i = debut ; i<fin ; i++) // On parcourt les éléments du sous-tableau, on a toujours pos <= i
		{
			var n = this.set.valeur[i];
			this.addAction({type:'colorier',n:n,c:couleurFocus});
			if (n < pivot)
			{
				// i a une valeur plus petite que la valeur pivot, on le palce en début de tableau (à la place de pos).
				this.addAction({type:'text2',text:'L\'élément '+(i+1)+' est plus petit que le pivot, on le place dans la première partie du tableau.',r:1});
				if (i != pos) this.echanger(i,pos);
				pos ++;
			}
			else
			{
				// i est plus grand pos, on le laisse en seconde partie de tableau
				this.addAction({type:'text2',text:'L\'élément '+(i+1)+' est plus grand que le pivot, on le laisse dans la seconde partie du tableau.'});
			}
			this.incrComparaisons();
			this.addAction({type:'pause'});
			this.addAction({type:'colorier',n:n,c:couleurDefaut});
		}
		// On place finalement le pivot à pos.
		if (fin != pos) this.echanger(fin,pos);
		this.addAction({type:'colorier',n:this.set.valeur[pos],c:couleurValide});
		// Appels récursifs pour les deux sous-partie du tableau.
		pos != debut ? this.rapide(debut,pos-1) : null;
		pos != fin ? this.rapide(pos+1,fin) : null;
		return true;
	}
	
	// function fusion : int -> int -> void
	// Trie le sous-tableau d'indices compris entre debut et fin suivant la méthode du tri fusion.
	// Cette méthode est récursive.
	this.fusion = function(debut,fin)
	{
		// Réinitialisation des couleurs des éléments (uniquement en visuel)
		for (var i = 1 ; i<17 ; i++)
		{
			this.addAction({type:'colorier',n:i,c:couleurDefaut,r:2});
		}
		var milieu = Math.floor((debut+fin)/2);
		if (debut < milieu) // Si il y a au moins deux éléments dans la première partie, on applique récursivement le tri à cet ensemble
		{
			for (var k = debut ; k < milieu+1 ; k++)
			{
				this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus,r:2});
			}
			this.addAction({type:'text1',text:'Appliquons le tri fusion au sous-ensemble '+(debut+1)+' à '+(milieu+1),r:2});
			this.addAction({type:'text2',text:'&nbsp;',r:1});
			this.fusion(debut,milieu);
		}
		else // Sinon l'élément est trié.
		{
			this.addAction({type:'colorier',n:this.set.valeur[debut],c:couleurFocus,r:2});
			this.addAction({type:'text1',text:'L\'élément '+(debut+1)+' est isolé, il est donc trié',r:2});
			this.addAction({type:'text2',text:'&nbsp;',r:1});
			this.addAction({type:'colorier',n:this.set.valeur[debut],c:couleurDefaut,r:2});
		}
		if (milieu+1 < fin) // Idem pour la seconde partie ...
		{
			for (var k = milieu+1 ; k < fin+1 ; k++)
			{
				this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus,r:2});
			}
			this.addAction({type:'text1',text:'Appliquons le tri fusion au sous-ensemble '+(milieu+2)+' à '+(fin+1),r:2});
			this.addAction({type:'text2',text:'&nbsp;',r:1});
			this.fusion(milieu+1,fin);
		}
		else
		{
			this.addAction({type:'colorier',n:this.set.valeur[fin],c:couleurFocus,r:2});
			this.addAction({type:'text1',text:'L\'élément '+(fin+1)+' est isolé, il est donc trié',r:2});
			this.addAction({type:'text2',text:'&nbsp;',r:1});
			this.addAction({type:'colorier',n:this.set.valeur[debut],c:couleurDefaut,r:2});
		}
		// On fusionne maintenant les deux sous-ensembles.
		// i est l'indice du plus petit élément de la première partie, j celui de la seconde partie
		var i=debut;
		var j=milieu+1;
		// On "donne le focus" aux éléments à fusionner.
		for (var k = debut ; k < fin+1 ; k++)
		{
			this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus,r:2});
		}
		this.addAction({type:'text1',text:'Fusionnons les sous-ensembles '+(debut == milieu ? debut+1 : ((debut+1)+' à '+(milieu+1)))+' et '+(milieu+1 == fin ? (fin+1) : ((milieu+2)+' à '+(fin+1)))});
		// On parcourt les emplacements de destination et on y insère à chaque fois le plus petit élément
		for (var k = debut+this.taille ; k<fin+this.taille+1 ; k++)
		{
			if (i < milieu+1 && j < fin+1) // On vérifie que i et j sont bien où il faut
			{
				this.addAction({type:'text2',text:'Les plus petits éléments de chaque sous-ensemble sont '+(i+1)+' et '+(j+1),r:2});
				// On donne un "focus2" (couleur orange/marron) aux plus petits éléments
				this.addAction({type:'colorier',n:this.set.valeur[i],c:couleurFocus2,r:2});
				this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurFocus2});
				// On place le plus petit élément dans la zone temporaire
				if (this.set.valeur[i] < this.set.valeur[j])
				{
					this.addAction({type:'text2',text:'L\'élément '+(i+1)+' est plus petit que l\'élément '+(j+1)+' donc on le place dans la zone temporaire',r:1});
					this.deplacer(i,k);
					this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus});
					i++;
				}
				else
				{
					this.addAction({type:'text2',text:'L\'élément '+(j+1)+' est plus petit que l\'élément '+(i+1)+' donc on le place dans la zone temporaire',r:1});
					this.deplacer(j,k);
					this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus});
					j++;
				}
				this.incrComparaisons();
			}
			else // Un des deux indices est trop grand, on utilise l'autre
			{
				if (i > milieu) // On déplace j
				{
					this.addAction({type:'text2',text:'Le premier sous-ensemble est vide, on recopie le plus petit élément du second ('+(j+1)+')',r:1});
					this.addAction({type:'colorier',n:this.set.valeur[j],c:couleurFocus2});
					this.deplacer(j,k);
					this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus});
					j++;
				}
				else // On déplace i
				{
					this.addAction({type:'text2',text:'Le second sous-ensemble est vide, on recopie le plus petit élément du premier ('+(i+1)+')',r:1});
					this.addAction({type:'colorier',n:this.set.valeur[i],c:couleurFocus2});
					this.deplacer(i,k);
					this.addAction({type:'colorier',n:this.set.valeur[k],c:couleurFocus});
					i++;
				}
				this.incrComparaisons();
			}
			this.incrComparaisons(); // Trop de comparaisons
		}
		// On recopie l'ensemble trié dans le tableau
		this.addAction({type:'text2',text:'Les deux sous-ensembles ont été fusionnés, on les recopie dans le tableau.',r:1});
		for (var k = debut+this.taille ; k<fin+this.taille+1 ; k++)
		{
			this.deplacer(k,k-this.taille,0);
			this.addAction({type:'colorier',n:this.set.valeur[k-this.taille],c:(debut==0 && fin==this.taille-1 ? couleurValide : couleurDefaut),r:2});
		}
		return true;
	}
	
	/** Da ultimate function **/
	
	// function trier : void -> void
	// Effectue le tri du tableau suivant la méthode choisie.
	this.trier = function()
	{
		// On active les textes d'indication (en haut) en mode visuel
		this.addAction({type:'activerHints'});
		var string = "Tri ";
		// b contient le résultat du tri.
		var b;
		if (!this.modeTemporel) visBoutonStart.attr('value','Pause');
		switch(this.type)
		{
			case "1":
				b = this.propagation();
				string += "par propagation";
			break;
			case "2":
				b = this.insertion();
				string += "par insertion";
			break;
			case "3":
				b = this.rapide(0,this.taille-1);
				string += "par rapide";
			break;
			case "4":
				b = this.fusion(0,this.taille-1);
				string += "fusion";
			break;
			case "5":
				b = this.selection();
				string += "par sélection";
			break;
		}
		if (!this.modeTemporel) // En mode visuel, on enregistre les résultats dans le log. En mode temporel cela se fera dans la définition de l'évènement.
		{
			// Les "\r\n" servent à obtenir des retours à la ligne lorsque l'on récupère le journal dans le presse-papier
			// Les "<br/>" servent à afficher les retours à la ligne dans le journal
			string += " appliqué à un tableau de "+this.taille+" éléments.\r\n<br/>Copies : "+this.copies+"\r\n<br/>Comparaisons : "+this.comparaisons+"\r\n\r\n";
			log(string);
		}
		return b;
	}
}

/** ===== EVENEMENTS GENERAUX ===== **/

/** Changements d'affichage **/
boutonVisuel.on('click', function() {
	if (display != 0)
	{
		// On oublie pas de reset le tri pour éviter les problèmes d'affichage
		tri.actions = new Array();
		tri.nbActions = 0;
		zap(0);
		// On conserve le type de tri :
		tri = new Tri(tri.type);
		tri.init();
		// On n'oublie pas de relier l'instance de tri au Ticker pour voir les animations.
		createjs.Ticker.addListener(tri);
	}
});
boutonTemporel.on('click', function() {
	if (display != 1)
	{
		zap(1);
		
		// On conserve le type de tri. Le second argument (true) précise que l'on est en mode temporel.
		tri = new Tri(tri.type,true);
	}
});
boutonJournal.on('click', function() {
	if (display != 2)
	{
		zap(2);
		
		// Pour que la méthode zclip fonctionne il faut que l'élément auquel elle est attachée (logBoutonCopier ici) soit visible, on effectue donc l'appel lors de l'affichage de la fenêtre du journal pour permettre son fonctionnement.
		logBoutonCopier.zclip({
			path:'ZeroClipboard.swf', // Chemin vers le fichier ZeroClipboard.swf, à adapter
			copy:logContent.text(), // contenu à copier
			afterCopy:function(){ } // annule l'alert apparaissant par défaut
		});
	}
});

/** Evènements visuels **/

// Changement de la méthode de tri
visChoixTri.on('change', function() {
	// On recrée un nouvel ensemble à trier.
	tri.actions = new Array();
	tri.nbActions = 0;
	tri = new Tri(visChoixTri.val());
	tri.init();
	createjs.Ticker.addListener(tri);
});

// Mode accéléré
visChoixAccelere.on('change', function() {
	// Ez
	tri.accelere = visChoixAccelere.attr('checked');
});

// Click sur le bouton "Commencer"
visBoutonStart.on('click', function() {
	if (tri.nbActions > 0) // Si il reste des actions à effectuer ...
	{
		if (tri.pasAPas) // En mode pas à pas on repasse en mode de lecture normal
		{
			tri.pasAPas = false;
		}
		else // Sinon on on fait play/pause
		{
			var b = createjs.Ticker.getPaused();
			visBoutonStart.attr('value', b ? 'Pause' : 'Continuer');
			createjs.Ticker.setPaused(!b);
		}
	}
	else // Sinon on lance le tri.
	{
		tri.actions = new Array();
		tri.nbActions = 0;
		tri.trier();
	}
});

// Click sur le bouton pas à pas
visBoutonStep.on('click', function() {
	// On passe en mode et on avance
	tri.pasAPas = true;
	if (tri.nbActions == 0) // Au cas où on n'a pas lancé le tri avec "commencer"
	{
		tri.trier();
	}
	while (tri.doAction() == 1); // On effectue les actions jusqu'à rencontrer une pause.
});

// Click sur le bouton recommencer
visBoutonRestart.on('click', function() {
	// On recrée un nouveau tri
	tri.actions = new Array();
	tri.nbActions = 0;
	tri = new Tri(tri.type);
	tri.init();
	createjs.Ticker.addListener(tri);
});

/** Evènements temporels **/

// Click sur le bouton commencer
tempBoutonStart.on('click', function() {
	// On récupère la valeurs entrée par l'utilisateur
	var t = parseInt(tempTailleTab.val());
	var n = parseInt(tempNbTab.val());
	var methode = tempChoixTri.val();
	// On initialise les temps de calcul et les variables
	var tempsCalcul = 0;
	var tempsTotal = new Date().getTime();
	var copies = 0;
	var comparaisons = 0;
	var nbTries = 0;
	// On pourrait majorer t*n pour réguler le temps de calcul
	// À chaque itération on crée un nouveau tableau à trier
	for (var i = 0 ; i < n ; i++)
	{
		tri = new Tri(methode,true,t);
		var dt = new Date().getTime(); // Début du calcul
		if (tri.trier()) nbTries ++;
		tempsCalcul += new Date().getTime() - dt; // Fin du calcul
		// On met à jour nos compteurs
		copies += tri.copies;
		comparaisons += tri.comparaisons;
	}
	// Le temps total :
	tempsTotal = new Date().getTime() - tempsTotal;
	// string va contenir le texte à placer dans le log
	string = "Tri ";
	switch (methode)
	{
		case "1":
			string += "par propagation";
		break;
		case "2":
			string += "par insertion";
		break;
		case "3":
			string += "rapide";
		break;
		case "4":
			string += "par fusion";
		break;
		case "5":
			string += "par sélection";
		break;
	}
	// On affiche les résultats à la fin :
	jQuery('dd:nth-child(2)').text(string);
	jQuery('dd:nth-child(4)').text(t);
	jQuery('dd:nth-child(6)').text(nbTries+' sur '+n);
	jQuery('dd:nth-child(8)').text(tempsTotal/1000 + ' secondes');
	jQuery('dd:nth-child(10)').text(tempsCalcul/1000 + ' secondes');
	jQuery('dd:nth-child(12)').text(comparaisons);
	jQuery('dd:nth-child(14)').text(copies);
	// On enregistre dans le log (pour les "\r\n<br/>", cf. ligne 651, méthode trier) :
	string += " appliqué à "+n+" tableau(x) de "+t+" élément(s).\r\n<br/>Temps écoulé : "+(tempsTotal/1000)+" s\r\n<br/>Temps de calcul : "+(tempsCalcul/1000)+" s\r\n<br/>Nombre de comparaisons : "+comparaisons+"\r\n<br/>Nombre de copies : "+copies+"\r\n\r\n";
	log(string);
});

/** Evènements du journal **/
// On click sur le bouton reset, ça efface tout :
logBoutonReset.on('click', function() {
	logContent.text('');
});

/** ===== INITIALISATION ===== **/

// Fenêtre initiale : tri visuel
zap(0);

//Initialisation du canvas
stage = new createjs.Stage(canvas);
createjs.Ticker.setFPS(100); // vérifier que cela fonctionne sur tous les téléphones
createjs.Ticker.addListener(stage);

var tri = new Tri(5); // Par défaut : tri par sélection
tri.init();
createjs.Ticker.addListener(tri);