<html>
    <body>
        <h1>text your order</h1><br>

    
    <form action="/cdata" method="post" name="order">
        <div class="signin">
        <label for="name" >Name</label>
        <input type="text" placeholder="Name" name="name" id="name" required><br><br>
        <label for="shop name">shop Name</label>
        <input type="text" placeholder="shop name" name="shopname" id="shopname" required><br><br>
        <label for="location">Location</label>
        <input type="text" placeholder="Location"name = "location" id="Location"><br>
        <!--<select  id="name" name="location">
           <option value="coimbatore">ukkadam</option>
            <option value="">gadhipuram</option>
            <option value="">annur</option>
            <option value="">thudiyalur</option>
            <option value="">siganallur</option>
            <option value="">ganapathi</option>-->
            
        </select> 
        <br><br>
        <label for="number">mobile number</label>
        <input type="integer" placeholder="number" name="mobile no" id="number"  maxlength="10" required>
        <br><br>
        <!--<label for="order menu">order menu</label>
       <input type="text" placeholder="iteam" id="number"> -->
       <br><br>
       <a href=""><button> submit</button></a>
       
        </div>
    </form>
    </body>
</html>
<style>
    body{
        background-image: url(https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_960_720.jpg);
        background-position: center;
        background-size: cover;
        text-align: left;
        size: 20px 30px;
        color: aqua;
    }
    .signin{
    
    background-position: center;
    text-align: center;
    text-size-adjust: 20px 30px;
    box-sizing: 20px 30px;
    tab-size: 20px 30px;
    color: rgb(59, 13, 212);
    
    
    }
    input {
        size: 30px 20px;
    }
    
        
        

    
</style>
