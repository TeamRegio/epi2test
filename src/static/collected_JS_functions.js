function switchGeneIDField(){
    var current = document.getElementById("gene_format").value;
    if (current === 'symbol_format') {
        document.getElementById("geneID_symbolic").type = "text";
        document.getElementById("geneID_numeric").type = "hidden";
        document.getElementById("geneHeader").textContent = "Gene Symbol:";
        document.getElementById("container_geneSymbolHeader").style.visibility = "visible";
    }
    if (current === 'id_format') {
    document.getElementById("geneID_symbolic").type = "hidden";
    document.getElementById("geneID_numeric").type = "text";
    document.getElementById("geneHeader").textContent = "Gene ID";
    document.getElementById("container_geneSymbolHeader").style.visibility = "hidden";
    }
}


function chooseButton(clicked_id, containerID){

    var container = document.getElementById(containerID);
    var existent = !!document.getElementById(clicked_id+'added');
    if (existent === false) {
        var button_add = document.createElement("input");
        button_add.type = "button";
        button_add.value = document.getElementById(clicked_id).textContent;
        button_add.id = clicked_id+'added';
        button_add.className = "chosenButtons";
        container.appendChild(button_add);
        button_add.onclick = function(){
            $(this).remove();
        }
    };
}

function ButtonsToInput(containerID, hiddenID){
    var container = document.getElementById(containerID).children;
    var txtc = "";
    var i;
    for (i=0; i < container.length; i++) {
        txtc = txtc + container[i].value + ", ";
    }
    $("#"+hiddenID).val(txtc);
}

function chooseRegion(){
    var container = document.getElementById("container_geneRegions");
    chr = document.getElementById("chrField").value;
    start = document.getElementById("chrStart").value;
    end = document.getElementById("chrEnd").value;
    id_str = chr + "-" + start + "-" + end;
    var existent = !!document.getElementById(id_str);

    if (existent === false) {
        var button_add = document.createElement("input");
        button_add.type = "button";
        button_add.value = "chr" + chr + " " + start + "-" + end;
        button_add.id = id_str;
        button_add.className = "chosenButtons";
        container.appendChild(button_add);
        button_add.onclick = function(){
            $(this).remove();
        }
    }
}