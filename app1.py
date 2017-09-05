<html>
<head>	<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<title>home</title>
  <style>
  {
  color: #b8b8b8 !important;
}
/* HEADER */
#nav-right{
  float:right;
}
.nav>li>a:focus, .nav>li>a:hover {
    text-decoration: none;
    background-color: #fff;
    color: #7079c6 !important;
}
.nav-pills>li.active>a{
    color: #7178c6 !important;
    font-weight: bold;
    background-color: #fff;
}
.nav-pills>li.active>a:hover{
  background-color: #fff;
}
.navbar-nav>li>a {
    padding-top: 20px;
}
.navbar-toggle {
  border: 2px solid #7178c6;
}
.icon-bar {
  color: #7178c6;
  border-color: #7178c6;
  background-color: #7178c6;
}
#nav-right button{
      font-size: 10px;
      margin-top: 15px;
      margin-bottom: 15px;
      margin-left: 10px;
      background-color: #fff;
      border-radius: 4px;
      border: 1px solid;
      padding: 5px 9px;
}
#nav-right{
  margin-right: 15px;
}
#navtop{
  font-size: 10px !important;
}
.fa {
    padding-right: 10px;
    font-size: 14px;
    color: #9a9a9a !important;
}
#logo a img{
    margin-top: -25px;
    margin-bottom: 30px;
}
#main-navigation{
    font-size: 12px !important;
    font-weight: bold;
}
#main-navigation .nav>li>a{
  padding-left:0;
  padding-right:0;
}
#main-navigation .container{
  max-width: 720px;
}
/* MEDIA QUERIES FOR TOP NAV*/
@media screen and (max-width:768px){
  #nav-left{
    text-align: center;
  }
  #nav-left:after{
    display: block;
    content: "";
    clear: both;
  }
  #nav-left li{
    float:left;
    width: 31%;
    padding:1%;
  }
  #nav-right{
    display: block;
    content: "";
    clear: both;
  }
  #nav-right{
    text-align: center;
    width:100%;
  }
  #nav-right li {
    float: left;
    width:23%;
    padding: 1%;
  }
  #logo a img {
    margin-top: 0;
    margin-bottom: 0;
}
#main-navigation ul li{
  border-top: 1px solid #7178c6;
  width: 100%;
}
}
/* MEDIA QUERIES FOR TOP NAV END*/
/* HEADER END*/


/* SLIDER */
#Container_Carousel .rows .col-xs-12{
  margin:0;
  padding:0;
}

#Container_Carousel{
  margin:0;
  padding:0;
  width:100%;
  max-height: 850px;
}

.item img{
  width:100%;
  max-height: 850px;
}

.carousel,.item,.active{
  height:100%;
}

.carousel-inner{
  height:100%;
}

.carousel-control.left, .carousel-control.right {
    background-image:none;
}
.glyphicon-circle-arrow-left {
  position: absolute;
  top: 50%;
  font-size: 50px;
  opacity: 0.5;
  left: 50px;
}
.glyphicon-circle-arrow-right {
  position: absolute;
  top: 50%;
  font-size: 50px;
  opacity: 0.5;
  right: 50px;
}
/* SLIDER END*/

  </style> 
  </head>
   
 
 
  
  
  
  <body> 
  <nav id="navtop">
        <div class="container-fluid">
      <!--header navbar top left -->
              <ul class="nav navbar-nav" id="nav-left">
                <li><a href="#">
                  <i class="fa fa-user" aria-hidden="true"></i>MY ACCOUNT</a>
                </li>
                <li><a href="#">
                  <i class="fa fa-check-square-o" aria-hidden="true"></i>CHECK OUT</a>
                </li>
                <li><a href="#">
                  <i class="fa fa-heart-o" aria-hidden="true"></i>MY WISHLIST</a>
                </li>
              </ul>
      <!--header navbar top right -->
              <ul class="nav navbar-nav nav-pills" id="nav-right">
                <li>
                  <a href="#">
                        <i class="fa fa-search" aria-hidden="true"></i>SEARCH</a>
                </li>
                <li>
                  <a href="#">
                        <i class="fa fa-shopping-bag" aria-hidden="true"></i>MYBAG</a>
                </li>

                <li><button type="btn btn-default navbar-btn">ENG</button></li>

                <li><button type="btn btn-default navbar-btn">USD</button></li>
              </ul>

          </div>
        </nav>
      <!--header navbar LOGO -->
        <div class="text-center" id="logo">
              <a href="#" ><img src="https://s22.postimg.org/owyv8ip5d/logo.jpg" alt="logo" /></a>
        </div>
      <!-- TOOGLE MAIN NAVIGATION -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#main-navigation" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>

      <!--  MAIN NAVIGATION -->
        <div class="collapse navbar-collapse" id="main-navigation">
          <div class="container">

          <ul class="nav nav-justified nav-pills">
              <li class="active"><a href="#">HOMEPAGE</a></li>
              <li><a href="#">PROJECT</a></li>
              <li><a href="#">SANCTION FUNDS</a></li>
              <li><a href="#">TOURIST PLACE</a></li>
              <li><a href="#">MAINTAINANCE</a></li>
              
          </ul>
          </div>
        </div>
<!--header navbar END -->

<!-- SLIDER START-->
<div id="Container_Carousel">
					<div class="rows">

						   <div class="col-lg-12  col-md-12 col-sm-12 col-xs-12" >

								  <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
										  <!-- Indicators -->
										  <ol class="carousel-indicators">
											<li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
											<li data-target="#carousel-example-generic" data-slide-to="1"></li>
											<li data-target="#carousel-example-generic" data-slide-to="2"></li>
										  </ol>

										  <!-- Wrapper for slides -->
										  <div class="carousel-inner">
											<div class="item active">
											  <img src="https://s22.postimg.org/yszy85uxd/banner.jpg" alt="First Slide">
											</div>

											<div class="item">
											 <img src="https://s22.postimg.org/yszy85uxd/banner.jpg" alt="Second Slide">
											</div>

												<div class="item">
											 <img src="https://s22.postimg.org/yszy85uxd/banner.jpg" alt="Third Slide">
											</div>

										  </div>

										  <!-- Controls -->
										  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
											<span class="glyphicon glyphicon-circle-arrow-left"></span>
										  </a>
										  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
											<span class="glyphicon glyphicon-circle-arrow-right"></span>
										  </a>
								</div>

						   </div>
					</div>
		</div>
    <div class="clear"></div>

<!-- SLIDER END-->
<script src="https://use.fontawesome.com/f12e4a6b3c.js"></script>
<html>
