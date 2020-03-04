<?php

class ConnectionManager {

    function connect() {
        $servername = "localhost";
        $port = 3306;
        $username = "root";
        $password = "";
        $dbname = "esm_db";
        
        // Create connection
        $url = "mysql:host=$servername;port=$port;dbname=$dbname";
        $conn = new PDO($url, $username, $password);     
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
        
        // if fail, exception will be thrown
    }
     
}


// $url = "mysql:host=$servername;port=$port;dbname=$dbname";
