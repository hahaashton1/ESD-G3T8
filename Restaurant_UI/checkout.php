<!DOCTYPE html>
<html>
<head>


<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Required meta tags -->
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="viewport" 
    content="width=device-width, initial-scale=1, shrink-to-fit=no">

<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="app.html.css">
<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">  -->
<title>Restaurant UI</title>
<script 
src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<script
src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"
integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
crossorigin="anonymous"></script>

<script 
src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k"
crossorigin="anonymous"></script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {
  font-family: Arial;
  font-size: 17px;
  padding: 8px;
}

* {
  box-sizing: border-box;
}

/* .row {
  display: -ms-flexbox; 
  display: flex;
  -ms-flex-wrap: wrap; 
  flex-wrap: wrap;
  margin: 0 -16px;
}

.col-25 {
  -ms-flex: 25%; 
  flex: 25%;
}

.col-50 {
  -ms-flex: 50%; 
  flex: 50%;
}

.col-75 {
  -ms-flex: 75%; 
  flex: 75%;
}

.col-25,
.col-50,
.col-75 {
  padding: 0 16px;
}  */

#left {
  width: 600px;
  float: left;
  padding: 20px;
}
#right {
  width: 600px;
  float: left;
  padding: 20px;

  /* margin-left: 400px;
  float: right; */

  /* Change this to whatever the width of your left column is*/
}
.clear {
  clear: both;
}


.container {
  background-color: #f2f2f2;
  padding: 5px 20px 15px 20px;
  border: 1px solid lightgrey;
  border-radius: 3px;
}

input[type=text] {
  width: 100%;
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

label {
  margin-bottom: 10px;
  display: block;
}

.icon-container {
  margin-bottom: 20px;
  padding: 7px 0;
  font-size: 24px;
}

.btn {
  background-color: #4CAF50;
  color: white;
  padding: 12px;
  margin: 10px 0;
  border: none;
  width: 100%;
  border-radius: 3px;
  cursor: pointer;
  font-size: 17px;
}

.btn:hover {
  background-color: #45a049;
}

a {
  color: #2196F3;
}

hr {
  border: 1px solid lightgrey;
}

span.price {
  float: right;
  color: grey;
}

.center {
  margin: 40px;
  width: 100%;
  /* border: 3px solid green; */
  padding: 10px;
  display:inline-block;

}

/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other (also change the direction - make the "cart" column go on top) */
@media (max-width: 800px) {
  .row {
    flex-direction: column-reverse;
  }
  .col-25 {
    margin-bottom: 20px;
  }
}


</style>
</head>
<body>

      <!-- <table id="priceTable" class='table table-striped' border='1'>
            <thead class='thead-dark'>
        <tr>
            <th>Region</th>
            <th>Price</th>
        </tr>  
    </table> -->

    <table id="priceTable" class='table table-striped' border='1'>
            <thead class='thead-dark'>
        <tr>
            <th>Region</th>
            <th>Price</th>
        </tr>  
    </table>

    <!-- for loop here -->

    <?
      
    ?>
<script>
  
  
// $('#priceTable').hide();
   


   // Helper function to display error message
   function showError(message) {
       // Hide the table and button in the event of error
       $("#priceTable").hide();
       // $('#addBookBtn').hide();

       // Display an error under the main container
       $("#main-container")
           .append("<label>"+message+"</label>");
   }

   // anonymous async function 
   // - using await requires the function that calls it to be async
     
   $(async() => { 
         // Change serviceURL to your own
       var serviceURL = "http://127.0.0.1:5000/delivery_pricing";

       try {
           const response =
            await fetch(
              serviceURL, { method: 'GET' }
           );
           const data = await response.json();
           var prices = data.prices; //the arr is in data.books of the JSON data

           // array or array.length are falsy
           if (!prices || !prices.length) {
               showError('Books list empty or undefined.');
           } 
           else {
               // for loop to setup all table rows with obtained book data
               var rows = "";
               var foundPrice = "";

               for (const one_price of prices) {
                   eachRow =
                       "<td>" + one_price.region_name + "</td>" +
                       "<td>" + one_price.price + "</td>" ;
                   rows += "<tbody><tr>" + eachRow + "</tr></tbody>";

                   eachPrice = "<option value=" + one_price.region_name +">";
                   foundPrice += eachPrice;
               }
               // add all the rows to the table
               $("#priceTable").append(rows);
              //  $("#delivery_pricing").append( foundPrice );
             

           }

           document.getElementByID("pricing").value = prices[<?$_POST['region']?>];


       } catch (error) {
           // Errors when calling the service; such as network error, 
           // service offline, etc
           showError
           ('There is a problem retrieving books data, please try again later.<br />'+error);
      
   } // error
});

  </script>

<div class = 'center'>
<h2> Checkout Form</h2> 
  <div id="left">
  <!-- <div class="container"> -->

      <form action="/action_page.php">
        <h3>Order Details</h3>

        <label for="name">Name </label>
        <input type="text" name="name" value="<?php echo $_POST['name'];?>" disabled />
        
        <label for="email">Email </label>
        <input type="text" name="email" value="<?php echo $_POST['email'];?>" disabled />
          
        <label for="telegram">Telegram</label>
        <input type="text" name="telegram_id" value="<?php echo $_POST['telegram_id'];?>" disabled />
          
        <label for="quantity">Quantity</label>
        <input type="text" name="quantity" value="<?php echo $_POST['quantity'];?>" disabled />
          
        <label for="address">Address</label>
        <input type="text" name="address" value="<?php echo $_POST['address'];?>" disabled />
          
        <label for="phone">Phone</label>
        <input type="text" name="phone" value="<?php echo $_POST['phone'];?>" disabled />

        <label for="region">Region</label>
        <input type="text" name="region" value="<?php echo $_POST['region'];?>" disabled />

        <label for="pricing">Delivery Pricing</label>
        <input type="text" name="pricing" id="pricing" value="<?php echo $_POST['price'];?>" disabled />
        <?$_POST['price']?>
        
      
      </div>


      
      <div id = 'right'>
        <h3>Payment</h3>

        <label for="cname">Name on Card</label>
        <input type="text" id="cname" name="cardname" placeholder="John More Doe">
        <label for="ccnum">Credit card number</label>
        <input type="text" id="ccnum" name="cardnumber" placeholder="1111-2222-3333-4444">
        <label for="expmonth">Exp Month</label>
        <input type="text" id="expmonth" name="expmonth" placeholder="September">
        <label for="expyear">Exp Year</label>
        <input type="text" id="expyear" name="expyear" placeholder="2018">
        <label for="cvv">CVV</label>
        <input type="text" id="cvv" name="cvv" placeholder="352">
   
  <input type="submit" value="Continue to checkout" class="btn">
  </form>
  </div>
  </div>
  

</body>
</html>

