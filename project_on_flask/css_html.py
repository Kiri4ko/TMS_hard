home_page_buttons = """
<!DOCTYPE html>
<html>
<head>
<style>

h2 {
  text-align: center;
  text-transform: uppercase;
  color: #4CAF50;
}


.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
</head>
<body>

<h2>WELCOME MAN</h2>

<a href="/iam/" class="button"> I'm </a>
<a href="/you/" class="button"> YOU </a>
<a href="/currency-rate/" class="button"> Currency rate </a>
<a href="/weather/" class="button"> Weather </a>


</body>
</html>
"""

iam_background = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.hero-image {
  background-image: url('https://ichef.bbci.co.uk/news/640/cpsprodpb/1999/production/_92935560_robot976.jpg');
  background-color: #cccccc;
  height: 500px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

.hero-text {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
</style>
</head>
<body>

<div class="hero-image">
  <div class="hero-text">
    <h1 style="font-size:50px">I am DD8 </h1>
    <h3>And I'm a ROBOT</h3>
    <button>Hear me</button>
  </div>
</div>

</body>
</html>
"""

form_weather = """
    <form action="http://127.0.0.1:5000/weather/city/" method="POST">
      <label for="city">City:</label><br>
      <input type="text" id="city" name="city" ><br>
      <input type="submit" value="View">
    </form> 
    """
form_exchange = """
    <form action="http://127.0.0.1:5000/currency-rate/currency-exchange/" method="POST">
      <label for="from_currency">From currency:</label><br>
      <input type="text" id="from_currency" name="from_currency" ><br>
      <label for="to_currency">To currency:</label><br>
      <input type="text" id="to_currency" name="to_currency" ><br>
      <label for="amount">Amount currency:</label><br>
      <input type="text" id="amount" name="amount" ><br>
      <input type="submit" value="View">
    </form>
    """
