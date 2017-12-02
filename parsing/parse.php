<?php

$service_url = "https://www.youtube.com/api/timedtext?expire=1512230718&v=0Y6s2kKpULU&caps=asr&hl=en_US&signature=7367116D83569F9A2138652600245F30788F50AA.C2E4BAFA13242EBC0B41C959C6D5EA89ED6004A4&sparams=asr_langs%2Ccaps%2Cv%2Cexpire&asr_langs=de%2Cko%2Cja%2Cnl%2Cen%2Cpt%2Ces%2Cru%2Cit%2Cfr&key=yttt1&kind=asr&lang=en&fmt=srv3";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $service_url);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_HEADER, 0);

curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);

$trans = [];

$pXML = new SimpleXMLElement($response);

$i = 0;

foreach ($pXML->body->p as $oEntry => $value) {
    if ($i % 2 == 0) {
        $str = "";
        if (count($value->s) > 0) {
            foreach ($value->s as $key => $words) {
                $str.=$words;
            }
        } else {
            $str.=$value;
        }
        $trans[] = [(int)$value->attributes()->t, $str];
    }
    $i+=1;
}
// var_dump($trans);
$create = "";

foreach ($trans as $fields) {
    $create .=  implode("\t", $fields);
    $create .= "\n";
}
if ($fp = fopen("Quick Easy Homemade Pizza Cooking Italian with Joe.tsv", 'w+')) {
    fwrite($fp, $create);
    fclose($fp);
}
echo $create;

?>
