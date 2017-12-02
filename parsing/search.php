<?php

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
$data = json_decode(file_get_contents('php://input'), true);
// var_dump($data);
$keyword = $data['keyword'];
$id = $data['id'];
// echo json_encode($data);
$headers = ["Content-type" =>  "text/json"];

$prefix = "https://49afc650.ngrok.io/parsing/".$id.".tsv";

$fields = array(
    'name' => $prefix,
    'keyword' => $keyword
);

$payload = json_encode($fields);

// $fields_string = "";
// foreach($fields as $key=>$value) {
//  $fields_string .= $key.'='.$value.'&';
// }
// rtrim($fields_string, '&');

$url = "http://35.199.154.16:8000/api/search_key";

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
// curl_setopt($ch,CURLOPT_URL, $url);
// curl_setopt($ch,CURLOPT_POST, count($fields));
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);

curl_close($ch);
echo $result;
// echo json_encode(["status" => 200]);

?>
