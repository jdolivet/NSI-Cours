jQuery.noConflict();

/** Variables */
var turing = {
    binaire: "",
    ok:false,
    lecture:false,
    interval:false,
    m:0,
    e:"e1",
    i:0,
    j:0,
    c:-1,
    x:false,
    left:0,
    tableau: [],
    machines: [],
    chaine:  jQuery('#grain-turing-chaine'),
    input: jQuery('#grain-turing-input'),
    select: jQuery('#grain-turing-select'),
    tbody: jQuery('#grain-turing-tbody'),
    pasapas: jQuery('#grain-turing-pasapas'),
    commencer: jQuery('#grain-turing-commencer'),
    texte : jQuery('#grain-turing-texte'),
    range : jQuery('#grain-turing-range'),
    turing : jQuery('#grain-turing'),
    leftInit: 350
};

/** Machines */
turing.machines[0] = new Array(
    new Array('e1', '', '', 'gauche', 'e2'),
    new Array('e2', '0', '0', 'gauche', 'e2'),
    new Array('e2', '1', '1', 'gauche', 'e2'),
    new Array('e2', '', '', 'droite', 'e3'),
    new Array('e3', '0', '1', 'droite', 'fin'),
    new Array('e3', '1', '0', 'droite', 'e3'),
    new Array('e3', '', '1', 'droite', 'fin')
);
turing.machines[1] = new Array(
    new Array('e1', '', '', 'gauche', 'e2'),
    new Array('e2', '0', '0', 'gauche', 'e2'),
    new Array('e2', '1', '1', 'gauche', 'e2'),
    new Array('e2', '', '', 'droite', 'e3'),
    new Array('e3', '0', '1', 'droite', 'e3'),
    new Array('e3', '1', '0', 'droite', 'fin'),
    new Array('e3', '', '', 'droite', 'fin')
);
turing.machines[2] = new Array(
    new Array('e1', '', '', 'gauche', 'e2'),
    new Array('e2', '0', '0', 'gauche', 'e2'),
    new Array('e2', '1', '1', 'gauche', 'e2'),
    new Array('e2', '', '0', 'gauche', 'fin')
);
turing.machines[3] = new Array(
    new Array('e1', '', '', 'gauche', 'e2'),
    new Array('e2', '0', '1', 'gauche', 'e2'),
    new Array('e2', '1', '0', 'gauche', 'e2'),
    new Array('e2', '', '', 'gauche', 'fin')
);
turing.machines[4] = new Array(
    new Array('e1', '', '', 'gauche', 'e2'),
    new Array('e2', '0', '0', 'gauche', 'e2'),
    new Array('e2', '1', '0', 'droite', 'e3'),
    new Array('e2', '', '', 'droite', 'e4'),
    new Array('e3', '0', '0', 'droite', 'e3'),
    new Array('e3', '', '0', 'gauche', 'e2'),
    new Array('e4', '0', '1', 'droite', 'e4'),
    new Array('e4', '', '', 'droite', 'fin')
);
turing.machines[5] = new Array(
    new Array('e1', '', '', 'gauche', 'e2'),
    new Array('e2', '0', '', 'gauche', 'e3'),
    new Array('e2', '1', '', 'gauche', 'e6'),
    new Array('e2', '', '', 'gauche', 'OUI'),
    new Array('e3', '0', '0', 'gauche', 'e3'),
    new Array('e3', '1', '1', 'gauche', 'e3'),
    new Array('e3', '', '', 'droite', 'e4'),
    new Array('e4', '0', '', 'droite', 'e5'),
    new Array('e4', '1', '1', 'gauche', 'NON'),
    new Array('e4', '', '', 'gauche', 'OUI'),
    new Array('e5', '0', '0', 'droite', 'e5'),
    new Array('e5', '1', '1', 'droite', 'e5'),
    new Array('e5', '', '', 'gauche', 'e2'),
    new Array('e6', '0', '0', 'gauche', 'e6'),
    new Array('e6', '1', '1', 'gauche', 'e6'),
    new Array('e6', '', '', 'droite', 'e7'),
    new Array('e7', '0', '0', 'gauche', 'NON'),
    new Array('e7', '1', '', 'droite', 'e5'),
    new Array('e7', '', '', 'gauche', 'OUI')
);

/** Compatibilité Firefox*/
if(jQuery.browser.mozilla) {
    turing.mozilla = function () {
        var div = jQuery('<select id="grain-turing-select" title="Vitesse de défilement"></select>');
        for(var i = 1 ; i <= turing.range.attr("max") ; i++)
            div.append('<option value="'+i+'">'+i+'</option>');
        turing.range.replaceWith(div);
        turing.range = div;
    };
    turing.mozilla();
}

/** Vérification du nombre binaire*/
turing.verifier = function () {
    turing.input.val( turing.input.val().replace(/[^01]/g, ""));
    if(turing.m == 4)
        turing.input.val( turing.input.val().replace(/[^1]/g, ""));
};
turing.input.keyup( function(event) {
    turing.verifier();
    if(event.which == 13)
        turing.lireInput();
});

/** Interruption */
turing.interruption = function() {
    turing.ok = false;
    turing.commencer.attr("disabled","disabled");
    turing.range.attr("disabled","disabled");
    turing.pasapas.attr("disabled","disabled");
};

/** Générer tableau*/
turing.genTable = function () {
    turing.m = turing.select.val();
    turing.tbody.empty();
    for(var i = 0; i < turing.machines[turing.m].length ; i++) {
        var div = jQuery('<tr id="grain-turing-tbody-tr'+i+'"></tr>');
        for(var j = 0 ; j < 5 ; j ++) {
            var t = turing.machines[turing.m][i][j];
            if(t === '')
                t = 'VIDE';
            div.append('<td id="grain-turing-tbody-tr'+i+'-td'+j+'">'+t+'</td>');
        }
        turing.tbody.append(div);
    }
    var e = turing.machines[turing.m][turing.machines[turing.m].length-1][0];
    var c = 1;
    for(i = turing.machines[turing.m].length - 2 ; i >= 0 ; i-- ) {
        if(turing.machines[turing.m][i][0] == e) {
            jQuery('#grain-turing-tbody-tr'+(i+1)+'-td'+0+'').hide();
            c++;
        }
        else{
            jQuery('#grain-turing-tbody-tr'+(i+1)+'-td'+0+'').attr('rowspan',c);
            e=turing.machines[turing.m][i][0];
            c=1;
        }
    }
    turing.verifier();
    turing.interruption();
};
turing.genTable();
turing.select.change(turing.genTable);


/** Générer la chaine */
turing.majChaine = function () {
    turing.tableau = turing.binaire.split('');
    
    turing.chaine.empty();
    for(var i = -30 ; i < turing.tableau.length + 30 ; i++) {
        var div = jQuery('<div id="grain-turing-chaine-'+i+'">'+(turing.tableau[i] || '')+'</div>');
        div.css("left",(i*25)+"px");
        turing.chaine.append(div);
    }
    turing.chaine.css("left", (turing.leftInit+25)+"px");
};
turing.majChaine();

/** Enregistrement du nombre binaire */
turing.lireInput = function () {
    turing.verifier();
    turing.binaire = turing.input.val();
    turing.initialisation();
};
jQuery("#grain-turing-btnInput").click(turing.lireInput);

/** Initialisation */
turing.initialisation = function() {
    turing.e = "e1";
    turing.i = 0;
    turing.j = 0;
    turing.c = -1;
    turing.ok = true;
    turing.lecture = false;
    clearInterval(turing.interval);
    turing.commencer.val('Commencer');
    turing.commencer.removeAttr("disabled");
    turing.range.removeAttr("disabled");
    turing.pasapas.removeAttr("disabled");
    turing.majChaine();
    turing.etape();
};


/** Commencer/Pause */
turing.start =  function () {
    if(!turing.ok)
        return false;
    turing.lecture = !turing.lecture;
    if(turing.lecture)
        turing.interval = setInterval(turing.etape, 1500/turing.range.val());
    else
        clearInterval(turing.interval);
    turing.commencer.val((turing.lecture ? 'Pause' : 'Commencer'));
    turing.chaine.css("left", (turing.leftInit - turing.c*25)+"px");
};
turing.commencer.click(turing.start);
turing.range.change(function () {
    turing.start();
    turing.start();
});


/** Etape */
turing.etape = function () {
    if(!turing.ok){
        clearInterval(turing.interval);
        return false;
    }
    turing.tbody.find('.encours').removeClass("encours");
    var i = turing.i;
    var j = turing.j;
    var b = turing.machines[turing.m][i];
    var c = turing.chaine.find('#grain-turing-chaine-'+turing.c);
    switch(j) {
        case 0:
            turing.texte.html("Etat de départ : "+turing.e);
            for(var id = 0 ; id < turing.machines[turing.m].length ; id ++) {
                b = turing.machines[turing.m][id];
                if(b[0] == turing.e)
                    jQuery('#grain-turing-tbody-tr'+id+'-td'+j+'').addClass("encours");
            }
            break;
        case 1:
            turing.texte.html("Symbole lu : \""+((c.html() !== '') ? c.html() : 'VIDE')+"\"");
            for(i = 0 ; i < turing.machines[turing.m].length ; i ++) {
                b = turing.machines[turing.m][i];
                if(b[0] == turing.e && b[1] == c.html()) {
                    jQuery('#grain-turing-tbody-tr'+i+'-td'+j+'').addClass("encours");
                    turing.i = i;
                    break;
                }
            }
            break;
        case 2:
            turing.texte.html("Symbole écrit : \""+((b[2] !== '') ? b[2] : 'VIDE')+"\"");
            jQuery('#grain-turing-tbody-tr'+i+'-td'+j+'').addClass("encours");
            c.html(b[2]);
            break;
        case 3:
            turing.texte.html("Mouvement du ruban : vers la "+b[3]);
            jQuery('#grain-turing-tbody-tr'+i+'-td'+j+'').addClass("encours");
            c.removeClass("encours");
            if(b[3] == 'gauche')
                turing.c++;
            else
                turing.c--;
            turing.chaine.css("left", (turing.leftInit - turing.c*25)+"px");
            break;
        case 4:
            turing.texte.html("Nouvel état : "+b[4]);
            jQuery('#grain-turing-tbody-tr'+i+'-td'+j+'').addClass("encours");
            turing.e = b[4];
            if(!turing.e.match(/^e[0-9]+$/)) {
                turing.interruption();
                clearInterval(turing.interval);
            }
            break;
    }
    turing.j++;
    if(turing.j>4)
        turing.j = 0;
    return true;
};
turing.pasapas.click(turing.etape);


