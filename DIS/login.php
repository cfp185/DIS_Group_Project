<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login Page</title>
    <style>
        /* Your existing CSS styles */
    </style>
</head>
<body>
    <center><h1>Student Login Form</h1></center>

    <?php
    // Establish a database connection
    $host = 'localhost';
    $dbName = 'users';
    $user = 'dmitriy';
    $password = 'i_love_dis123';

    try {
        $db = new PDO("mysql:host=$host;dbname=$dbName", $user, $password);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch(PDOException $e) {
        die("Connection failed: " . $e->getMessage());
    }

    // Handle form submission
    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Validate inputs and prevent SQL injection
        // You should implement more robust validation and sanitization logic here
        $username = htmlspecialchars($username);
        $password = htmlspecialchars($password);

        // Execute SQL query to check user credentials
        $query = "SELECT * FROM users WHERE username = :username AND password = :password";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $password);
        $stmt->execute();

        // Check if a matching user is found
        if ($stmt->rowCount() > 0) {
            // Successful login
            echo "Login successful!";
        } else {
            // Failed login
            echo "Invalid username or password!";
        }
    }
    ?>

    <form action="login.php" method="POST">
        <div class="container">
            <label>Username:</label>
            <input type="text" placeholder="Enter Username" name="username" required>
            <label>Password:</label>
            <input type="password" placeholder="Enter Password" name="password" required>
            <button type="submit">Login</button>
            <input type="checkbox" checked="checked"> Remember me
            <button type="button" class="cancelbtn">Cancel</button>
            Forgot <a href="{{ url_for('too_bad') }}">password?</a>
        </div>
    </form>
</body>
</html>