<html>

<body>
    <form action="./phpcalculator_add.php" method="GET">
        <h2>Addition</h2>
        <label for="add_first">First Number</label>
        <input type="number" id="add_first" name="add_first">
        <br>
        <label for="add_second">Second Number</label>
        <input type="number" id="add_second" name="add_second">
        <br><br>
        <input type="submit" value="Submit">
    </form>
    <form action="./phpcalculator_div.php" method="GET">
        <h2>Division</h2>
        <label for="div_first">First Number</label>
        <input type="number" id="div_first" name="div_first">
        <br>
        <label for="div_second">Second Number</label>
        <input type="number" id="div_second" name="div_second">
        <br><br>
        <input type="submit" value="Submit">
    </form>
    <a href="index.php">Reset</a>
</body>

</html>