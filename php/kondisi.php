<?php

echo "<center><h2>Branching Php</h2></center>";

/*contoh pertama*/
$ujian = 90;

if($ujian > 80){

 echo "selamat kamu pengayaan!";

}
else{
  echo "Kamu Remedial Banyak Belajar lagi ya...";
}

echo "<hr>";

/*contoh kedua*/
$ujian = 80;

if($ujian > 70){

echo "udah ganteng pinter lagi !";

}else{
  echo "Goblok Lhuu...";
}

/*contoh ketiga*/
$nama= "Richard";
$nilai = 99;

if($nilai >= 100){
$grade = "Si Jenius";
}
elseif($nilai > 90){
  $grade = "A";
}elseif($nilai > 80){
  $grade = "B";
}elseif($nilai > 70){
$grade = "C";

}else{
  echo "Anak Haram kamu !!!";
}

echo "Selamat $nama kamu telah melakukan pekerjaan yang great job ! dengan predikat $grade <br>";
echo "<hr>";




/* contoh switch */
 $month = 3;
 switch ($month) {
   case '1':
    echo "January";
     break;
      case '2';
      echo "February";
      break;
      case '3';
      echo "March";
      break;
      case '4';
      echo "April";
      break;
      case '5';
      echo "May";
      break;
      case '6';
      echo "June";
      break;
      case '7';
      echo "Jule";
      break;
      case '8';
      echo "Agustus";
      break;
      case '9';
      echo "September";
      break;
      case '10';
      echo "Oktober";
      break;
      case '11';
      echo "November";
      break;
      case '12';
      echo "Desember";
      break;

        default:
        echo "Ups....";
          break;


echo "<hr>";
 }








?>
