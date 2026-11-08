---
name: cine
description: Diretor de cena e prompts cinematográficos com 34 comandos para geração de imagem e vídeo.
---

# `/cine` & `@cine` — Visual Director & Prompt Menu Skill

Use `/cine` or `@cine` whenever you want to select visual parameters or direct image/video generation.

## How to Use `/cine`

1. **Interactive Menu**: Type `/cine` alone to display the full interactive menu of 34 visual slash commands categorized by Camera, Climate, Style, and Product Display.
2. **Direct Selection**: Type `/cine` followed by any combination of commands and your subject description:
   - Example 1: `/cine /GoldenHour /LuxuryAd um carro esportivo preto`
   - Example 2: `/cine /dollyin /NeonCity /slomotion corrida de rua`
   - Example 3: `/cine /explodedview smartphone moderno`

## Catalog Categories

- **Camera (`/cine camera`)**: `/flythrough`, `/dollyin`, `/dollyout`, `/pan`, `/tilt`, `/zoom`, `/establishing`, `/closeup`, `/wideangle`, `/pov`, `/overhead`, `/aerial`, `/DroneView`.
- **Climate/Time (`/cine clima`)**: `/timelapse`, `/hyperlapse`, `/slomotion`, `/daytonight`, `/seasonchange`, `/GoldenHour`, `/RainyNight`, `/SnowWorld`, `/Fog`, `/Autumn`.
- **Style (`/cine estilo`)**: `/StudioPro`, `/MovieScene`, `/NeonCity`, `/Magazine`, `/OldMoney`, `/VintageFilm`, `/LowAngleHero`, `/DoubleExposure`, `/ProfHeadshot`, `/LuxuryAd`, `/MiniWorld`.
- **Product (`/cine produto`)**: `/teardown`, `/explodedview`, `/reveal`.

## Integration Pipeline

When `/cine` or `@cine` is called:
1. Parse the selected visual directives using `node C:\Users\Administrator\.gemini\config\sidecars\cine-director.js`.
2. Generate image using `generate_image` or generate video via `gemini-omni-1.1-flash` / `higgsfield-effects`.
3. Apply `@eco` token optimization rules.
