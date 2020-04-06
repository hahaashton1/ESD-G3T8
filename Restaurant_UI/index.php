<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="viewport" 
        content="width=device-width, initial-scale=1, shrink-to-fit=no">

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
  </head>

  <body>

  <style type="text/css" media="screen">
      /* * {
        margin: 0; 
        padding: 0;
      }

      div#banner { 
        position: absolute; 
        top: 0; 
        left: 0; 
        background-color: #FDD7C2; 
        width: 100%; 
      }
      div#banner-content { 
        width: 1000px; 
        margin: 0 auto; 
        padding: 10px; 
        border: 1px solid #000;
      }
      div#main-content { 
        padding-top: 20px;
      } */

                  
      @font-face {
          font-family: Clip;
          src: url("https://acupoftee.github.io/fonts/Clip.ttf");
        }
    

        .sign {
          position: absolute;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 90%;
          height: 10%;
          transform: translate(-50%, -50%);
          letter-spacing: 2;
          left: 50%;
          top: 3%;
          font-family: "Clip";
          text-transform: uppercase;
          font-size: 2em;
          color: #ffe6ff;
          text-shadow: 0 0 0.6rem #ffe6ff, 0 0 1.5rem #ff65bd,
            -0.2rem 0.1rem 1rem #ff65bd, 0.2rem 0.1rem 1rem #ff65bd,
            0 -0.5rem 2rem #ff2483, 0 0.5rem 3rem #ff2483;
          animation: shine 0.5s forwards, flicker 1s infinite;
        }

        .sign2 {
          background-color: #FFB03B;
          min-height: 15px;

          position: absolute;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 10%;
          transform: translate(-50%, -50%);
          letter-spacing: 2;
          left: 50%;
          top: 12%;
          font-family: "Clip";
          text-transform: lowercase;
          font-size: 2em;
          color: #000000;
        }
        
        
        @keyframes blink {
          0%,
          22%,
          36%,
          75% {
            color: #ffe6ff;
            text-shadow: 0 0 0.6rem #ffe6ff, 0 0 1.5rem #ff65bd,
              -0.2rem 0.1rem 1rem #ff65bd, 0.2rem 0.1rem 1rem #ff65bd,
              0 -0.5rem 2rem #ff2483, 0 0.5rem 3rem #ff2483;
          }
          28%,
          33% {
            color: #ff65bd;
            text-shadow: none;
          }
          82%,
          97% {
            color: #ff2483;
            text-shadow: none;
          }
        }
    
        .fast-flicker {
          animation: shine 3s forwards, blink 1s 1s infinite;
        }
        
        @keyframes shine {
          0% {
            color: #6b1839;
            text-shadow: none;
          }
          100% {
            color: #ffe6ff;
            text-shadow: 0 0 0.6rem #ffe6ff, 0 0 1.5rem #ff65bd,
              -0.2rem 0.1rem 1rem #ff65bd, 0.2rem 0.1rem 1rem #ff65bd,
              0 -0.5rem 2rem #ff2483, 0 0.5rem 3rem #ff2483;
          }
        }
        
        @keyframes flicker {
          from {
            opacity: 1;
          }
        
          4% {
            opacity: 0.9;
          }
        
          6% {
            opacity: 0.85;
          }
        
          8% {
            opacity: 0.95;
          }
        
          10% {
            opacity: 0.9;
          }
        
          11% {
            opacity: 0.922;
          }
        
          12% {
            opacity: 0.9;
          }
        
          14% {
            opacity: 0.95;
          }
        
          16% {
            opacity: 0.98;
          }
        
          17% {
            opacity: 0.9;
          }
        
          19% {
            opacity: 0.93;
          }
        
          20% {
            opacity: 0.99;
          }
        
          24% {
            opacity: 1;
          }
        
          26% {
            opacity: 0.94;
          }
        
          28% {
            opacity: 0.98;
          }
        
          37% {
            opacity: 0.93;
          }
        
          38% {
            opacity: 0.5;
          }
        
          39% {
            opacity: 0.96;
          }
        
          42% {
            opacity: 1;
          }
        
          44% {
            opacity: 0.97;
          }
        
          46% {
            opacity: 0.94;
          }
        
          56% {
            opacity: 0.9;
          }
        
          58% {
            opacity: 0.9;
          }
        
          60% {
            opacity: 0.99;
          }
        
          68% {
            opacity: 1;
          }
        
          70% {
            opacity: 0.9;
          }
        
          72% {
            opacity: 0.95;
          }
        
          93% {
            opacity: 0.93;
          }
        
          95% {
            opacity: 0.95;
          }
        
          97% {
            opacity: 0.93;
          }
        
          to {
            opacity: 1;
          }
        }
  </style>

<?php
    $link = mysqli_connect("localhost", "root", "", "Twitter_API");

    if($link === false){
      die("ERROR: Could not connect. " . mysqli_connect_error());
    }

    // $sql = "SELECT * FROM 'tweets2' WHERE 'id' = 1";
    $sql = "SELECT `id`, `tweets` FROM `tweets` WHERE `id` = 1";
    if($result = mysqli_query($link, $sql)){
      if(mysqli_num_rows($result) > 0){
        
          echo "<div class='sign'>";
      
          while($row = mysqli_fetch_array($result)){
                  echo "<span class='fast-flicker'>PROMOTION:</span></div>";
                  
                  echo "<div class = 'sign2'>" . $row['tweets'] . "</div>";
          }
          
          // Free result set
          mysqli_free_result($result);
          echo "</span></div>";
        }
    }

    ?>

    <br><br>
    <br><br>
  <!-- menu -->
  
  </section>
  <section id="menu-list" class="section-padding">
    <!-- <div class="container"> -->
      <!-- <div class="row"> -->
        <div class="col-md-12 text-center marb-35">
          <h1 class="header-h">Welcome to 1 Cupcake</h1>
          <h2>Menu List</h2>  

          <!-- <div class="breakfast menu-restaurant "> -->

            <span class ="clearfix">
              <a class="menu-title" style="bold" >Food Item Name:</a>
              <a class="menu-price">Vanilla Cupcake - $3</a>
            </span>
            <div>
              <img src="photo/cupcake.jpg" class ="photo" alt="cupcake" height="200" width="250" >
            </div>
            
            </div>
          </div>
            </div>
        </div>

      </div>
    </div>
  </section>
 

  <section id="contact" class="section-padding">
    <!-- <div class="container">
      <div class="row"> -->
        <div class="col-md-12 text-center">
          <h1 class="header-h">Place your order</h1>
          <p class="header-p">Please fill in your order details</p>
        </div>
      </div>
      <div class="row msg-row">
        <div class="col-md-4 col-sm-4 mr-15">
          <div class="media-2">
            <div class="media-left">
              <div class="contact-phone bg-1 text-center"><span class="phone-in-talk fa fa-phone"></span></div>
            </div>
            <div class="media-body">
              <h4 class="dark-blue regular">Phone Numbers</h4>
              <p class="light-blue regular alt-p">+440 875369208 - <span class="contacts-sp">Phone Booking</span></p>
            </div>
          </div>
          <div class="media-2">
            <div class="media-left">
              <div class="contact-email bg-14 text-center"><span class="hour-icon fa fa-clock-o"></span></div>
            </div>
            <div class="media-body">
              <h4 class="dark-blue regular">Opening Hours</h4>
              <p class="light-blue regular alt-p"> Monday to Friday 09.00 - 24:00</p>
              <p class="light-blue regular alt-p">
                Friday and Sunday 08:00 - 03.00
              </p>
            </div>
          </div>
        </div>


        <div class="col-md-8 col-sm-8">
          <form id = "orderForm" action="checkout.php" class="contactForm" method = "POST" target = "formresponse">
            <div id="sendmessage">Your booking request has been sent. Thank you!</div>
            <div id="errormessage"></div>

            <div class="col-md-6 col-sm-6 contact-form pad-form">
              <div class="form-group label-floating is-empty">
                <input type="text" name="name" class="form-control" id="name" placeholder="Your Name" data-rule="minlen:4" data-msg="Please enter at least 4 chars" />
                <div class="validation"></div>
              </div>
            </div>
            <div class="col-md-6 col-sm-6 contact-form pad-form">
              <div class="form-group">
                <input type="email" class="form-control label-floating is-empty" name="email" id="email" placeholder="Your Email" data-rule="email" data-msg="Please enter a valid email" />
                <div class="validation"></div>
              </div>
            </div>

            <div class="col-md-6 col-sm-6 contact-form pad-form">
              <div class="form-group">
                <input type="text" class="form-control label-floating is-empty" name="telegram_id" id="telegram_id" placeholder="Telegram Handle" data-rule="email" data-msg="Please enter a valid telegram handle" />
                <div class="validation"></div>
              </div>
            </div>

            
            <div class="col-md-6 col-sm-6 contact-form pad-form">
              <div class="form-group label-floating is-empty">
                <input type="number" name="quantity" class="form-control" id="quantity"s placeholder="Quantity" data-rule="number" data-msg="Please enter at least 4 chars" />
                <div class="validation"></div>
              </div>
            </div>

            <div class="col-md-6 col-sm-6 contact-form">
              <div class="form-group">
                <input type="address" class="form-control label-floating is-empty" name="address" id="address" placeholder="Address" data-rule="required" data-msg="This field is required" />
                <div class="validation"></div>
              </div>
            </div>
            <div class="col-md-6 col-sm-6 contact-form">
              <div class="form-group">
                <input type="tel" class="form-control label-floating is-empty" name="phone" id="phone" placeholder="Phone" data-rule="required" data-msg="This field is required" />
                <div class="validation"></div>
              </div>
            </div>
            <div class="col-md-6 col-sm-6 contact-form">
              <div class="form-group">
                <input type="text" class="form-control label-floating is-empty" name="postalCode" id="postalCode" placeholder="Postal Code" data-rule="number" data-msg="This field is required" />
                <div class="validation"></div>
              </div>
            </div>
        
              <div class="col-md-6 col-sm-6 contact-form">
                <div class="form-group">
                  <input list="delivery_pricing" name = "region" id ="region" >
                  <datalist id="delivery_pricing" >
                  </datalist>
                </div>
              </div>

          <script>
              $("#region").change(function(){

              var region=$("#region").val();
              var value = $('#delivery_pricing option').filter(function() {
                return this.value == region;
              }).data('value');

              var msg = value ? value : 'No Match';
              document.getElementById("priceval").value = msg;

              // alert(msg);

              });
          

          </script>

                      
          <div class="col-md-6 col-sm-6 contact-form">
            <div class="form-group">
              <input type = "hidden" name = "price" id = "priceval">
            </div>
          </div>  




            <div class="col-md-12 btnpad">
              <div class="contacts-btn-pad">
                <button class = 'contacts-btn' >

                  

                  <a id = 'submitBtn' name = 'submit'>Submit Order</a>
                </button>
              </div>
            </div>
          </form>

        </div>
        </div>


        <div id="main-container" class="container">
        <!-- <h1 class="display-4">Delivery Pricing</h1> -->
        <!-- <table id="priceTable" class='table table-striped' border='1'>
            <thead class='thead-dark'>
        <tr>
            <th>Region</th>
            <th>Price</th>
        </tr>  
    </table> -->
    </div>  
    <label id="error" class="text-danger"></label>
  
    </body>    

        </div>
      </div>
    </div>
  </section>
  <!-- / contact -->
  <!-- footer -->

  <footer>
    
  </footer>



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
            var dict = new Object();

            try {
                const response =
                 await fetch(
                   serviceURL, { method: 'GET' }
                );
                const data = await response.json();
                // console.log(data.prices[0])

                var prices = data.prices; //the arr is in data.books of the JSON data
     
                // array or array.length are falsy
                if (!prices || !prices.length) {
                    showError('Books list empty or undefined.');
                } 
                else {
                    // for loop to setup all table rows with obtained book data
                    var rows = "";
                    var foundPrice = "";
                    // var selectedPrice = "";

                    for (const one_price of prices) {
                         
                        // eachRow =
                        //     "<td>" + one_price.region_name + "</td>" +
                        //     "<td>" + one_price.price + "</td>" ;
                        // rows += "<tbody><tr>" + eachRow + "</tr></tbody>";


                        eachRegion = "<option data-value = " + one_price.price + ">" + one_price.region_name +"</option>";
                        $("#delivery_pricing").append( eachRegion );

                        // eachPrice = "<option value =" + one_price.region_name + ">" + one_price.price +"</option>";
                        // $("#price").append( eachPrice 
                        dict[one_price.region_name] = one_price.price;
                        
                        
                    }

                    $("#priceTable").append(rows);
                }
            } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                showError
                ('There is a problem retrieving books data, please try again later.<br />'+error);
           
        } // error
    });
</script>
 

    
</script> 
</body>
</html>

