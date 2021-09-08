<?php
$dsn = 'mysql:dbname=u410296026_tuvionline;host=localhost';
$user = 'u410296026_admin';
$password = 'Admin123';
 
try
{
	$pdo = new PDO($dsn,$user,$password);
	$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e)
{
	echo "PDO error".$e->getMessage();
	die();
}
?>
