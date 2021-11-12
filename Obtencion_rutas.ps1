$ruta = Read-Host -prompt "Inserte la ruta a analizar`n"
Write-Host ' '

try{
    $archivos = Get-ChildItem $ruta -Recurse | Where-Object {$_.PSIsContainer -eq $false} | Select-Object Fullname
    $rutas = $archivos.Fullname
}catch{
    Write-Host 'Ruta errónea'
    exit
}
$op = Read-Host -prompt "¿Qué hash desea realizar?`n[1] Md5`n[2] Sha512`n[3] Sha256`n`n"
switch($op){
    1{ 
        $num = 'md5'
    }2{
        $num = 'sha512'
        }
    }3{
        $num = 'sha256'

    }default{
        Write-Host "Ingreso un valor inválido"
        exit
    }
}
foreach ($file in $rutas){
    $name = Split-Path $file -leaf
    python Hashes.py $file $name $num
    #Write-Host $file
    }

#Python = 'python.exe'
#$script = 'C:\Users\amont\Downloads\Hashes.py'
#$rutas | & $Python $script