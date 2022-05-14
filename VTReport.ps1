
 Param( 
    [Parameter(Mandatory)][String] $apikey,
    [Parameter(Mandatory)][String] $target,
    [Parameter(Mandatory)][String] $result,
    [ValidateSet("y","n")][String] $premium
    )


$data = Get-ChildItem $target | Get-FileHash
$counter = 0
$Results = @()
$files = @()

Start-Transcript -Path $result
foreach($hash in $data.Hash){
    if (($counter -cgt 0) -and ($counter%4 -ceq 0) -and ($premium -ine ("y"))){
        Start-Sleep -Seconds 60
    }

    $body = @{resource = $hash ; apikey = $apikey }
    $VTReport = Invoke-RestMethod -Method 'POST' -Uri 'https://www.virustotal.com/vtapi/v2/file/report' -Body $body
    if ($VTReport.response_code -eq 1){
        $Results += $VTReport.scan_date +"`t"+ $hash +"`t"+ $VTReport.positives+'/'+$VTReport.total +"`t"+ $data.Path[$counter]
    } elseif($VTReport -ceq '') {
        "Ingresaste una APIkey no premium usando el parámetro premium. El proceso se ha detenido" | Out-File $result -Encoding utf8
        Exit
    } else {
        $files += $data.Path[$counter] 
    }
    $counter += 1
}

foreach($file in $files){
    $body = @{ file='@file'; apikey=$apiKey }
    $VTReport = Invoke-RestMethod -Method 'POST' -Uri 'https://www.virustotal.com/vtapi/v2/file/scan' -Body $body
    if ($VTReport.response_code -eq 1){

        $Results += "Sent for scan...   " +"`t"+ (Get-FileHash $file).Hash +"`t"+ ' N/A ' +"`t"+ $file
    } else {
        $Results += "There was an error " +"`t"+ (Get-FileHash $file).Hash +"`t"+ ' N/A ' +"`t"+ $file
    }
}

#$Results | Out-File $result -Encoding ascii
#foreach($j in $Results)
#{
#    Write-Host $j
#}
Write-Host ($Results | Format-Table | Out-String)
Stop-Transcript
<#
.Synopsis 
    Obtiene reportes de VirusTotal.

.DESCRIPTION
    Obtiene los reportes desde VirusTotal para todos los archivos y subdirectorios de un directorio.

.NOTES
    Es necesario una APIkey de VirusTotal, si su APIkey es premium, puede establecerlo en los parametros.
    Las direcciones de la carpeta TARGET, y el archivo de RESULTADOS deben ser direcciones absolutas.

.EXAMPLE
    Get-VTReport -apikey "0123456789abcdefbbcd6521e6ef85735a6ce32aa97ef63404a0758e73082fa4" -target "C:\Users\Usuario1\Desktop\Target" -result "C:\Users\Usuario1\Desktop\res.txt" -premium y

.EXAMPLE
    Get-VTReport -result "C:\Users\Usuario1\Desktop\res.txt" -target "C:\Users\Usuario1\Desktop\Target" -apikey "0123456789abcdefbbcd6521e6ef85735a6ce32aa97ef63404a0758e73082fa4" -premium n

.EXAMPLE
    Get-VTReport -target "C:\Users\Usuario1\Desktop\Target" -result "C:\Users\Usuario1\Desktop\res.txt" -apikey "0123456789abcdefbbcd6521e6ef85735a6ce32aa97ef63404a0758e73082fa4"

#>