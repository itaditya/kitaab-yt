<?php
error_reporting(0);
header("Access-Control-Allow-Origin: *");
header('Access-Control-Allow-Methods: POST, GET, DELETE, PUT, PATCH, OPTIONS');
header('Content-Type: application/json');
// get the HTTP method, path and body of the request
$method = $_SERVER['REQUEST_METHOD'];
// $request = explode('/', trim($_SERVER['PATH_INFO'],'/'));

if ($method!= 'POST') {
    echo json_encode(['status' => 404]);
    die();
}
// $id = $_POST['name'];
// $data = json_decode(file_get_contents('php://input'), true);
// echo json_encode($data);
// var_dump($data);
// $headers = ["Content-type" =>  "text/json"];
$keyword = $_POST['keyword'];
$id = $_POST['name'];
$prefix = "https://e7e69236.ngrok.io/parsing/".$id.".tsv";
// echo $id;
$fields = array(
    'name' => $prefix,
    'keyword' => $keyword
);

$payload = json_encode($fields);


$url = "http://35.199.181.28:8000/api/search_key";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
// curl_setopt($ch,CURLOPT_URL, $url);
// curl_setopt($ch,CURLOPT_POST, count($fields));
// curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
curl_close($ch);
echo $result;
// echo json_encode(json_decode($result));
// dd($result);

// echo json_encode(["status" => 200]);

?>
