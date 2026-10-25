---
name: cinema-prompt-studio
description: Studio Prompt Director Skill for Antigravity (Cinemastudio & Image/Video Generators). Translates 34 visual slash-commands (camera moves, climate, lighting styles, product teardown/exploded views) into technical prompts for generate_image, gemini-omni-flash-api, and higgsfield-effects.
---

# Cinema Prompt Studio — Visual Direction Skill

Use this skill when generating images (`generate_image`), video shorts (`gemini-omni-1.1-flash`), or cinematic sequences (`higgsfield-effects`) using short slash commands.

## 34 Visual Directives Catalog

### 🎥 1. Movimentos e Enquadramentos de Câmera
- `/flythrough`: Motion flying through a complex scene/landscape.
- `/dollyin`: Smooth optical/camera push-in toward subject.
- `/dollyout`: Smooth optical/camera pull-back away from subject.
- `/pan`: Horizontal panning camera motion (left to right / right to left).
- `/tilt`: Vertical tilting camera motion (up or down).
- `/zoom`: Optical zoom in or zoom out.
- `/establishing`: Wide establishing shot setting up the location/atmosphere.
- `/closeup`: Macro tight detail shot on faces, textures, or objects.
- `/wideangle`: Ultra-wide lens field of view (14mm-24mm).
- `/pov`: First-person point-of-view perspective.
- `/overhead`: Top-down 90-degree zenith view (birds-eye / knolling).
- `/aerial`: General high-altitude aerial view.
- `/DroneView`: Smooth low-altitude fpv drone sweep shot.

### 🌅 2. Tempo, Transformação e Clima
- `/timelapse`: Accelerated time progression with static camera.
- `/hyperlapse`: Accelerated time progression with dynamic moving camera.
- `/slomotion`: High-speed 60fps/120fps slow-motion capture.
- `/daytonight`: Seamless day-to-night lighting transition.
- `/seasonchange`: Visual transition across spring, summer, autumn, winter.
- `/GoldenHour`: Warm golden sunlight, soft shadows, warm highlights.
- `/RainyNight`: Wet reflective asphalt, neon reflections, rain droplets.
- `/SnowWorld`: Heavy snowfall, frost textures, cold blue-white palette.
- `/Fog`: Heavy atmospheric volumetric fog and mist.
- `/Autumn`: Autumn foliage, warm amber/crimson color palette.

### 🎨 3. Estilos Visuais e Retratos
- `/StudioPro`: Professional softbox lighting, clean rim light, studio backdrop.
- `/MovieScene`: 35mm anamorphic film look, cinematic letterbox, color grading.
- `/NeonCity`: Cyberpunk urban night, neon lights, high-contrast glow.
- `/Magazine`: Editorial fashion magazine cover aesthetic, sharp focus.
- `/OldMoney`: Elegant classic aesthetic, understated luxury, tweed/beige tones.
- `/VintageFilm`: Grainy 70s analog film texture, muted colors, light leaks.
- `/LowAngleHero`: Low-angle hero shot looking up to convey power/imposence.
- `/DoubleExposure`: Artistic dual-image overlay composition.
- `/ProfHeadshot`: Corporate headshot lighting, soft bokeh background.
- `/LuxuryAd`: High-end commercial lighting, golden accents, reflection polish.
- `/MiniWorld`: Tilt-shift miniature diorama aesthetic.

### ⚙️ 4. Exibição de Produtos e Efeitos Específicos
- `/teardown`: Complete visual disassembly of hardware/equipment.
- `/explodedview`: Floating 3D exploded view with separated components in mid-air.
- `/reveal`: Dramatic lighting reveal / emergence of a hero product or subject.

## Automation Pipeline

When any of these 34 slash-commands are mentioned in a prompt:
1. Map commands to exact prompt descriptors.
2. Inject into `generate_image` or `gemini-omni-1.1-flash` / `higgsfield-effects`.
3. Combine seamlessly with `@eco` token-saving principles.
