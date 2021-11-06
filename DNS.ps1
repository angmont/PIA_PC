<#
.Description

Este script realiza varios comandos relacionados con DNS

Solo es necesario ejecutar el script, lo demás lo pide por medio de Read-Host
#>

$op = Read-Host -prompt "¿Qué opción desea realizar?`n[1] Consulta DNS`n[2] Ver Caché`n[3] Borrar Caché`n[4] Salir`n"
$Path = Get-Location
switch($op){
    1{ 
        $dom = Read-Host -prompt "Inserte el dominio"
        try {
            Resolve-DnsName $dom
        } catch {
            Write-Host "Hubo un error"
        }
    }2{
        try {
            Set-Content -Value (Get-DnsClientCache) -Path $Path"\Informacion_Cache.txt"
            Write-Host "Se almacenó en el archivo Informacion_Cache.txt en la siguiente ruta:"
            Write-Host $Path
        } catch {
            Write-Host "Hubo un error"
        }
    }3{
        Clear-DnsClientCache
    }4{
        exit
    }default{
        Write-Host "Ingreso un valor inválido"
    }
}
