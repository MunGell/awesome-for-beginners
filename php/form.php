<!doctype html>
<html lang="id">
<head>
<title>penangana form</title>
</head>
<body>
<form action='' method='post' name='input'>
NAMA:<input type='text' name='nama' placeholder='NAMA...'><br>
Sekolah Asal:<input type='text' name='asal' placeholder='ASAL SEKOLAH...'><br>
Tanggal Lahir<input type='date' name='ttl' placeholder='tanggal lahir..'><br>
<input type='submit' name='input' value='kirim'>
</form>
</body>
</html>


<?php

if(isset($_POST['input'])){
 $nama = htmlspecialchars($_POST['nama']);
 $asal = htmlspecialchars($_POST['asal']);
 $tanggal = htmlspecialchars($_POST['ttl']);
}

echo  @$nama."<br>";
echo @$asal."<br>";
echo @$tanggal."<br>";
 ?>
