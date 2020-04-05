<!DOCTYPE html>
<html>
<head>
<? session_start();?>
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


<script>
  
  
// $('#priceTable').hide();
   


  //  // Helper function to display error message
  //  function showError(message) {
  //      // Hide the table and button in the event of error
  //      $("#priceTable").hide();
  //      // $('#addBookBtn').hide();

  //      // Display an error under the main container
  //      $("#main-container")
  //          .append("<label>"+message+"</label>");
  //  }

   // anonymous async function 
   // - using await requires the function that calls it to be async
     
//    $(async() => { 
//          // Change serviceURL to your own
//        var serviceURL = "http://127.0.0.1:5000/delivery_pricing";

//        try {
//            const response =
//             await fetch(
//               serviceURL, { method: 'GET' }
//            );
//            const data = await response.json();
//            var prices = data.prices; //the arr is in data.books of the JSON data

//            // array or array.length are falsy
//            if (!prices || !prices.length) {
//                showError('Books list empty or undefined.');
//            } 
//            else {
//                // for loop to setup all table rows with obtained book data
//                var rows = "";
//                var foundPrice = "";

//                for (const one_price of prices) {
//                    eachRow =
//                        "<td>" + one_price.region_name + "</td>" +
//                        "<td>" + one_price.price + "</td>" ;
//                    rows += "<tbody><tr>" + eachRow + "</tr></tbody>";

//                    eachPrice = "<option value=" + one_price.region_name +">";
//                    foundPrice += eachPrice;
//                }
//                // add all the rows to the table
//                $("#priceTable").append(rows);
//               //  $("#delivery_pricing").append( foundPrice );
             

//            }

//            document.getElementByID("pricing").value = prices[<?$_POST['region']?>];


//        } catch (error) {
//            // Errors when calling the service; such as network error, 
//            // service offline, etc
//            showError
//            ('There is a problem retrieving books data, please try again later.<br />'+error);
      
//    } // error
// // });

  // var myFunction = document.getElementById("myFunction");
  // myFunction.onclick function() {
  //   alert("Transaction completed");
  //   // window.location(href = 'index.php');
  // }


//   $("#formbutton").click(function() { 
//     $(async() => {     

// //event.preventDefault();

//             // var telegram_id = $('#telegram_id').val();
//             // var email = $('#email').val();
//             // var name = $('#name').val();
//             // var quantity = $('#quantity').val();
//             // var price = $('#price').val();
//             // var address = $('#address').val();
//             // var phone = $('#phone').val();
//             // var postalCode = $('#postalCode').val();



//             console.log(name);



//             var serviceURL = "http://127.0.0.1:5000/order";

//             try {
//                 const response =
//                     await fetch(
//                         serviceURL, {
//                         method: 'POST',
//                         headers: { "Content-Type": "application/json" },
//                         body: JSON.stringify({ telegram_id: telegram_id, email: email, name:name, quantity:quantity, price:price, address:address, phone:phone, postalCode: postalCode })
//                     });
//                 const data = await response.json();
//                 //var books = data.books; //the arr is in data.books of the JSON data
//                 //console.log("This is happening");
//                 console.log(data)

//                 // array or array.length are falsy
//             } catch (error) {
//                 // Errors when calling the service; such as network error, 
//                 // service offline, etc
//                   showError('ERRRRRRRRRRRRRRROR.<br />'+error);
              
//             } // error
//             });
//   })

  </script>
 <?
  // if(isset($_POST['submit'])){
  // $_SESSION['name'] = $_POST['name'];
  // $_SESSION['email'] = $_POST['email'];
  // $_SESSION['telegram_id'] = $_POST['telegram_id'];
  // $_SESSION['quantity'] = $_POST['quantity'];
  // $_SESSION['address'] = $_POST['address'];
  // $_SESSION['phone'] = $_POST['phone'];
  // $_SESSION['region'] = $_POST['region'];
  // $_SESSION['pricing'] = $_POST['pricing'];

  // $_SESSION['cardname'] = $_POST['cardname'];
  // $_SESSION['cardnumber'] = $_POST['cardnumber'];
  // $_SESSION['expmonth'] = $_POST['expmonth'];
  // $_SESSION['expyear'] = $_POST['expyear'];
  // $_SESSION['cvv'] = $_POST['cvv'];


  // header("Location: subtotal.php");
  // exit();
?>

<div class = 'center'>
<h2> Checkout Form</h2> 
  <div id="left">
  <!-- <div class="container"> -->

      <!-- <form id="checkoutForm"> -->
        <h3>Order Details</h3>
        <form id = 'form1' action = "subtotal.php" method = 'POST'>
        <label for="name">Name </label>
        <input type="text" id = 'name' name="name" value="<?php echo $_POST['name'];?>" readonly />
        
        <label for="email">Email </label>
        <input type="text" name="email" value="<?php echo $_POST['email'];?>" readonly />
          
        <label for="telegram">Telegram</label>
        <input type="text" name="telegram_id" value="<?php echo $_POST['telegram_id'];?>" readonly />
          
        <label for="quantity">Quantity</label>
        <input type="text" name="quantity" value="<?php echo $_POST['quantity'];?>" readonly />
          
        <label for="address">Address</label>
        <input type="text" name="address" value="<?php echo $_POST['address'];?>" readonly />
          
        <label for="phone">Phone</label>
        <input type="text" name="phone" value="<?php echo $_POST['phone'];?>" readonly />

        <label for="region">Region</label>
        <input type="text" name="region" value="<?php echo $_POST['region'];?>" readonly />

        <label for="pricing">Delivery Pricing</label>
        <input type="text" name="pricing" id="pricing" value="<?php echo $_POST['price'];?>" readonly />
        
      
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
 
        <button type="submit" id = "formbutton">Continue to checkout</button>

        </form>

       
  </div>
  </div>
  

</body>
</html>

