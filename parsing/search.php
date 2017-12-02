<?php
// error_reporting(0);
header("Access-Control-Allow-Origin: *");
header('Access-Control-Allow-Methods: POST, GET, DELETE, PUT, PATCH, OPTIONS');
header('Content-Type: application/json');
// get the HTTP method, path and body of the request
$method = $_SERVER['REQUEST_METHOD'];
// $request = explode('/', trim($_SERVER['PATH_INFO'],'/'));

// if ($method!= 'POST') {
//     echo json_encode(['status' => 404]);
//     die();
// }
// $data = json_decode(file_get_contents('php://input'), true);

$keyword = $_GET['keyword'];
$id = $_GET['id'];

$prefix = "https://e7e69236.ngrok.io/parsing/".$id.".tsv";

$query = '?name='.$prefix.'&keyword='.$keyword;

$url = "http://35.199.181.28:8000/api/search_key".$query;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
// curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
// curl_close($ch);
echo $result;

?>
