<?php
$username = "admin";
$password = array("password");
$myPDO = new PDO('sqlite:database_toBeFinished.db');
$stmt = $myPDO->prepare("SELECT * FROM users WHERE username = ?");
$stmt->execute(array("$username"));
if($row = $stmt->fetch()) {
	$databasePassword = $row[1];
	echo $databasePassword;
	echo "\n";
	echo $password;
	echo "\n";
	$md5_password = md5("$password");
	echo $md5_password;
	echo "\n";
	if($databasePassword == md5("$password")) {
           echo "Successful";
	}
	else{
	   echo "Fail";
	}
}
else{
	echo "No such username";
}
?>
