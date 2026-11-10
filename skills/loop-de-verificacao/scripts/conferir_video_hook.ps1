# Stop Hook para Windows (PowerShell)
# O agente só encerra a sessão quando o render mais recente em render/ for aprovado.
# Código de saída 2: bloqueia a parada e repassa o motivo para o agente continuar.
# Código de saída 0: autoriza a parada.

$projectDir = if ($env:CLAUDE_PROJECT_DIR) { $env:CLAUDE_PROJECT_DIR } else { Get-Location }
Set-Location $projectDir

$videoItem = Get-ChildItem -Path "render\*.mp4" -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (-not $videoItem) {
    exit 0
}

$videoPath = $videoItem.FullName
$aprovadoFile = Join-Path $projectDir "conferencia\APROVADO"

if ((Test-Path $aprovadoFile) -and ((Get-Item $aprovadoFile).LastWriteTime -gt $videoItem.LastWriteTime)) {
    exit 0
}

$extraArgs = @()
if (Test-Path "roteiro.txt") {
    $ouvidoFile = "ouvido.txt"
    if ((-not (Test-Path $ouvidoFile)) -or ((Get-Item $ouvidoFile).LastWriteTime -lt $videoItem.LastWriteTime)) {
        [Console]::Error.WriteLine("Transcreva o render $($videoItem.Name) em ouvido.txt antes de terminar, para conferência comparar com o roteiro.txt.")
        exit 2
    }
    $extraArgs += @("--roteiro", "roteiro.txt", "--ouvido", "ouvido.txt")
}

New-Item -ItemType Directory -Force -Path ".claude" | Out-Null
$logPath = ".claude\ultima-conferencia.txt"

$proc = Start-Process -FilePath "python" -ArgumentList (@("conferir_video.py", "`"$($videoItem.FullName)`"", "--formato", "1080x1920") + $extraArgs) -RedirectStandardOutput $logPath -RedirectStandardError $logPath -PassThru -Wait

if ($proc.ExitCode -eq 0) {
    New-Item -ItemType Directory -Force -Path "conferencia" | Out-Null
    Set-Content -Path $aprovadoFile -Value "APROVADO em $(Get-Date -Format 'o')"
    exit 0
} else {
    if (Test-Path $logPath) {
        $lines = Get-Content $logPath -Tail 25
        [Console]::Error.WriteLine(($lines -join "`n"))
    }
    [Console]::Error.WriteLine("`nO render $($videoItem.Name) NÃO passou na conferência. Leia conferencia/RELATORIO.md, abra as folhas e os cortes, conserte e renderize de novo.")
    exit 2
}
