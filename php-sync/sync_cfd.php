<?php

//
// Connexion a la base
//


function synccfd_connect_db($host, $port, $login, $pass, $db) {
    global $synccfd_mysql_link, $synccfd_mysql_db;    // pour connexions multiples

    if ($port > 0) $host = "$host:$port";
    $synccfd_mysql_link = @mysql_connect($host, $login, $pass);
    $synccfd_mysql_db = $db;
    $ok = @mysql_select_db($db);

    return $ok;
}

function synccfd_abstract_quote($arg_sql) {
    return (is_int($arg_sql)) ? $arg_sql : ("'" . addslashes($arg_sql) . "'");
}

/*
* Calcul del nombre de registres pendents de sincronitzar
*/
function synccfd_check_pending_sync($last_id) {
    $query = "SELECT count(*) as regs_pending
                FROM spip_forms_donnees insc
                WHERE insc.id_donnee > ".synccfd_abstract_quote($last_id).
              " AND insc.id_form = 6";
    $result = mysql_query($query);
    if ($row = mysql_fetch_array($result)) {
        return $row['regs_pending'];
    } else {
        return 0;
    }
}

/*
* Llista de les inscripcions pendents
*/
function synccfd_pending_sync($last_id) {
    $query = "SELECT insc.id_donnee, insc.date, camp.champ, camp.valeur, valor.rang, valor.titre
                    FROM spip_forms_donnees insc, spip_forms_donnees_champs camp
                    LEFT OUTER JOIN spip_forms_champs_choix valor ON valor.champ = camp.champ
                    AND valor.choix = camp.valeur
                    WHERE insc.id_donnee = camp.id_donnee
                    AND insc.id_donnee > ".synccfd_abstract_quote($last_id).
                    "AND insc.id_form = 6
                    AND insc.statut = 'publie'
                    ORDER BY insc.id_donnee, camp.champ";

    $result = mysql_query($query);
    $rows = array();
    while ($row = mysql_fetch_assoc($result)) {
        $rows[] = array_map(utf8_encode, $row);
    }
    return $rows;
}

$action = '';
$last_id = 0;
$app_error = false;
$msg_error = '';

if (isset($_GET["action"])){
    $action = $_GET["action"];
}

if (isset($_GET["last_id"])){
    $last_id = $_GET["last_id"];
}

if (!synccfd_connect_db('localhost' ,'','user' ,'password' ,'database')){
    $msg_error = "La connexi&oacute; a la base de dades no s'ha realitzat amb &egrave;xit";
    $app_error = true;
}

header('Content-Type: application/json; charset=utf-8');

if ($app_error){
    $arr = array ('error' => true , 'msg_error'=> $msg_error);
    echo json_encode($arr);
} else {
    switch ($action) {
        case "check":
            $pending_regs = synccfd_check_pending_sync($last_id);
            $arr = array ('error' => false , 'pending'=> $pending_regs);
            echo json_encode($arr);
            break;
        case "get":
            $arr = array ('error' => false , 'list'=> synccfd_pending_sync($last_id));
            echo json_encode($arr);
            break;
    }
}


?>