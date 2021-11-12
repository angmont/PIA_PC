$ruta = Get-Location
Write-Host $ruta
Write-Host ' '
$archivos = Get-ChildItem $ruta -Recurse | Where-Object {$_.PSIsContainer -eq $false} | Select-Object Fullname
$rutas = $archivos.Fullname

foreach ($file in $rutas){
    $name = Split-Path $file -leaf
    python $script $file $name
    #Write-Host $file
    }

#Python = 'python.exe'
#$script = 'C:\Users\amont\Downloads\Hashes.py'
#$rutas | & $Python $script