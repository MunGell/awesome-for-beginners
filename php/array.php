<?php
/*array*/
//membuat array bisa//
// $variabel = array('', '', '', ...); //
// $variabel = ['', '', '', ...]; //
// $varibael[0] = "Isi variabel atau array"; //

//cara menampilkan array//
// echo $variabel[0]; /(array dimulai dari 0)/

//contoh array//
$mobil = array('Avanza', 'carry', 'Aplhard');
echo $mobil[0]."<br>";


//contoh//
$makanan = array('mie goreng', 'Pizza Hut', 'Nasi goreng' );

echo $makanan[0]."<br>";
echo $makanan[1]."<br>";
echo $makanan[2]."<br>";

echo "<hr>";




//contoh 2//

$minuman = ['Teh', 'Kopi', 'Susu', 'Soda'];

echo $minuman[0]."<br>";
echo $minuman[1]."<br>";
echo $minuman[2]."<br>";
echo "<hr>";

//atau memanfaatkan perulangan for//

for($i = 0; $i < count($minuman); $i++){

  echo $minuman[$i]."<br>";
}

echo "<hr>";



//atau memanfaatakan perulangan foreach//

foreach ($minuman as $haus) {
echo $haus."<br>";
}

echo "<hr>";

//array asossiatif//
//array yang tidak menggunakan angka sebagai sebagai pemanggil melainkan kata kunci//
//contoh 3//

$buku = [
 "penulis" => "Muh.Ridwan",
 "judul"  => "Laskar pelangi",
 "rilis" => "2021"
];

//cara menampilakan / memanggil array assosiatif adalah//

echo "Penulis= ".$buku["penulis"];
echo "<br>judul= ".$buku["judul"];
echo "<br>Tahun Rilis= ".$buku["rilis"];

echo "<hr>";

//contoh 4//
$mobil = [
"merek" => "Toyota",
"harga" => 150000000,
"ciptaan" => "japan"
];

echo "Merk Mobil = ".$mobil["merek"];
echo "<br> Harganya = ".$mobil["harga"];
echo "<br> Dari = ".$mobil["ciptaan"];







?>
