<?php
require_once 'connectionManager.php';
?>
<html>
<body>

    <table border="1">
        <tr>
            <th>Name</th>
            <th>Quantity Available</th>
            <th>Price</th>
        </tr>
    <?php
                
        // connect to database
        $connMgr = new ConnectionManager();
        $conn = $connMgr->connect();

        // // prepare select
        $sql = "SELECT `productID`,`quantity`,`price` FROM `ordertable`";
        $stmt = $conn->prepare($sql);
        $stmt->execute();

        $stmt->setFetchMode(PDO::FETCH_ASSOC);

        while ($result = $stmt->fetch() ) {
            echo "
            <tr>
                <td>{$result['productID']}</td>
                <td>{$result['quantity']}</td>
                <td>{$result['price']}</td>
            </tr>
            ";
        }

        // close connections
        $stmt = null;
        $conn = null;        

    ?>
    </table>

    <!-- form -->

    <form method = 'POST' action ="checkout.php">
        <h1>Place Your Order Here!</h1>
        Name: <input type = 'text' name = 'name'><br>
        E-mail: <input type = 'text' name = 'email'><br>
        Address: <input type = 'text' name = 'address'><br>
        ProductID: <input type = 'text' name = 'productid'><br>
        Quantity: <input type = 'text' name = 'quantity'><br>

        <input type = 'submit'></input>
    </form>

</body>
</html>
