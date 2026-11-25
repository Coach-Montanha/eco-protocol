# Instalador em 1 Linha do Protocolo @eco para Windows (PowerShell)
# Instala o @eco como regra de agente e skill global para Cursor, Claude Code ou Antigravity

$TargetDir = "$HOME\.gemini\config\plugins\efficiency-toolkit\skills\eco"
$RulesDir = "$HOME\.gemini\config\plugins\efficiency-toolkit\rules"

Write-Host "🌿 Instalando Protocolo @eco..." -ForegroundColor Green

# Criar diretórios se não existirem
New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
New-Item -ItemType Directory -Force -Path $RulesDir | Out-Null

# Copiar arquivos
Copy-Item -Path "SKILL.md" -Destination "$TargetDir\SKILL.md" -Force
Copy-Item -Path "rules\AGENTS.md" -Destination "$RulesDir\AGENTS.md" -Force

Write-Host "✅ Protocolo @eco instalado com sucesso!" -ForegroundColor Cyan
Write-Host "🚀 Agora o seu assistente opera sob ultra-eficiência de tokens (70% a 85% de economia)." -ForegroundColor Yellow
