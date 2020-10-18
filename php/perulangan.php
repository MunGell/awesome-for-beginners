<?php
/* Perulangan */
/* perulangan dalam php terdiri dari 3 atau ada 3 yang pertama for(perulangan for),
Yang kedua while(perulangan while), yang ketiga ada foreach (perulangan foreach) */

//for//
//contoh perulangan for pertama increment++//
 for($i = 1; $i <= 6; $i++){
   echo "$i<br>";
 }

 echo "<hr>";

 //contoh perulangan for kedua decrement--//

for($i = 10; $i >= 1; $i--){
  echo "$i<br>";
}

echo "<hr>";

//contoh kasus perulangan for//

for($i = 1; $i <= 6; $i++){

  echo "<h$i>ini adalah font size $i</h$i>";
}



echo "<hr>";


//while//
//contoh perulangan while pertama increment++//
$a = 1;
while($a <= 9){
echo "Ini adalah angak $a<br>";
$a++;
}

echo "<hr>";


//foreach//
//contoh perulangan foreach pertama//
$nama = [
 "nama" => "Faiz Nurullah",
 "asal" => "Cirebon",
 "umur" => "16 Tahun"

];
foreach($nama as $datanama){
    echo $datanama."<br>";
}






?>
