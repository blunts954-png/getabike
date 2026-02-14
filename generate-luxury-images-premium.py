#!/usr/bin/env python3
"""
GET A BIKE - LUXURY IMAGE GENERATION (PIL VERSION)
Generates premium placeholder images with luxury black & gold aesthetic
No API key required - uses PIL/Pillow for high-quality graphics
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
import math
import random
from pathlib import Path

# Create output directories
OUTPUT_DIR = Path("public/assets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# LUXURY COLOR PALETTE - Black & Gold Theme
COLORS = {
    'bg_black': '#050505',
    'bg_dark': '#0a0a0a',
    'bg_card': '#111111',
    'bg_elevated': '#1a1a1a',
    'gold': '#c9a962',
    'gold_light': '#e8d5a3',
    'gold_dark': '#9a7b3d',
    'gold_alpha': (201, 169, 98, 255),
    'white': '#ffffff',
    'gray_100': '#f5f5f5',
    'gray_300': '#d4d4d4',
    'gray_500': '#737373',
    'gray_600': '#525252',
    'gray_700': '#404040',
    'gray_800': '#262626',
    'gray_900': '#171717',
    'carbon': '#1a1a2e',
    'carbon_fiber': '#2d2d3a',
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient(width, height, color1, color2, direction='diagonal'):
    """Create smooth gradient background"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    c1 = hex_to_rgb(color1)
    c2 = hex_to_rgb(color2)
    
    for y in range(height):
        for x in range(width):
            if direction == 'diagonal':
                ratio = (x + y) / (width + height)
            elif direction == 'vertical':
                ratio = y / height
            elif direction == 'horizontal':
                ratio = x / width
            elif direction == 'radial':
                cx, cy = width // 2, height // 2
                max_dist = math.sqrt(cx**2 + cy**2)
                dist = math.sqrt((x - cx)**2 + (y - cy)**2)
                ratio = dist / max_dist
            else:
                ratio = y / height
            
            r = int(c1[0] + (c2[0] - c1[0]) * ratio)
            g = int(c1[1] + (c2[1] - c1[1]) * ratio)
            b = int(c1[2] + (c2[2] - c1[2]) * ratio)
            draw.point((x, y), fill=(r, g, b))
    
    return img

def add_noise(img, intensity=0.02):
    """Add subtle film grain noise"""
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if random.random() < intensity:
                r, g, b = pixels[x, y]
                noise = random.randint(-10, 10)
                pixels[x, y] = (
                    max(0, min(255, r + noise)),
                    max(0, min(255, g + noise)),
                    max(0, min(255, b + noise))
                )
    return img

def add_vignette(img, strength=0.4):
    """Add luxury vignette effect"""
    width, height = img.size
    vignette = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(vignette)
    
    for y in range(height):
        for x in range(width):
            # Distance from center (normalized 0-1)
            cx, cy = width / 2, height / 2
            dx = abs(x - cx) / cx
            dy = abs(y - cy) / cy
            dist = max(dx, dy)
            
            # Vignette intensity
            val = int(255 * (1 - dist * strength))
            draw.point((x, y), fill=max(0, min(255, val)))
    
    vignette = vignette.filter(ImageFilter.GaussianBlur(width // 4))
    img = Image.composite(img, Image.new('RGB', (width, height), (0, 0, 0)), vignette)
    return img

def draw_glow_line(draw, x1, y1, x2, y2, color, width_line=2, glow_radius=10):
    """Draw glowing line for luxury effect"""
    # Draw glow
    for r in range(glow_radius, 0, -2):
        alpha = int(50 * (r / glow_radius))
        glow_color = (*hex_to_rgb(color), alpha)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width_line + r*2)
    # Draw core line
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width_line)

def draw_luxury_bike_frame(draw, cx, cy, scale=1.0, frame_color='gold', accent_color='gold_light'):
    """Draw a stylized luxury road bike frame"""
    frame_rgb = hex_to_rgb(COLORS[frame_color])
    accent_rgb = hex_to_rgb(COLORS[accent_color])
    
    # Wheel positions
    rear_wheel_x = cx - int(120 * scale)
    front_wheel_x = cx + int(120 * scale)
    wheel_y = cy + int(20 * scale)
    wheel_radius = int(70 * scale)
    
    # Draw wheels (thin line circles with gold)
    for wheel_x in [rear_wheel_x, front_wheel_x]:
        # Tire
        draw.ellipse(
            [wheel_x - wheel_radius, wheel_y - wheel_radius,
             wheel_x + wheel_radius, wheel_y + wheel_radius],
            outline=COLORS['gray_800'], width=3
        )
        # Rim with gold accent
        draw.ellipse(
            [wheel_x - wheel_radius + 8, wheel_y - wheel_radius + 8,
             wheel_x + wheel_radius - 8, wheel_y + wheel_radius - 8],
            outline=COLORS['gold'], width=2
        )
        # Spokes (subtle)
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = wheel_x + int((wheel_radius - 8) * math.cos(rad))
            y1 = wheel_y + int((wheel_radius - 8) * math.sin(rad))
            x2 = wheel_x + int(8 * math.cos(rad))
            y2 = wheel_y + int(8 * math.sin(rad))
            draw.line([(x1, y1), (x2, y2)], fill=COLORS['gray_700'], width=1)
    
    # Frame triangle points
    bottom_bracket = (cx, cy + int(40 * scale))
    seat_cluster = (cx - int(20 * scale), cy - int(60 * scale))
    head_tube_top = (cx + int(80 * scale), cy - int(50 * scale))
    head_tube_bottom = (cx + int(75 * scale), cy - int(10 * scale))
    rear_dropout = (rear_wheel_x, wheel_y - int(10 * scale))
    
    # Draw frame tubes with gradient effect
    tube_width = max(2, int(6 * scale))
    
    # Chain stays
    draw.line([bottom_bracket, rear_dropout], fill=COLORS['gold'], width=tube_width)
    # Seat stays
    draw.line([seat_cluster, rear_dropout], fill=COLORS['gold'], width=tube_width)
    # Seat tube
    draw.line([bottom_bracket, seat_cluster], fill=COLORS['gold'], width=tube_width + 2)
    # Down tube
    draw.line([bottom_bracket, head_tube_bottom], fill=COLORS['gold'], width=tube_width + 2)
    # Top tube
    draw.line([seat_cluster, head_tube_top], fill=COLORS['gold'], width=tube_width)
    # Head tube
    draw.line([head_tube_bottom, head_tube_top], fill=COLORS['gold_dark'], width=tube_width + 3)
    
    # Fork
    fork_crown = head_tube_bottom
    front_dropout = (front_wheel_x, wheel_y - int(10 * scale))
    draw.line([fork_crown, (fork_crown[0] + 15, fork_crown[1] + 30)], fill=COLORS['gold'], width=tube_width)
    draw.line([(fork_crown[0] + 15, fork_crown[1] + 30), front_dropout], fill=COLORS['gold'], width=tube_width)
    
    # Handlebars
    bar_y = head_tube_top[1] - int(30 * scale)
    draw.line([head_tube_top, (head_tube_top[0], bar_y)], fill=COLORS['gray_600'], width=3)
    draw.line([(head_tube_top[0] - 20, bar_y), (head_tube_top[0] + 20, bar_y)], fill=COLORS['gray_600'], width=3)
    
    # Seat post and saddle
    seat_y = seat_cluster[1] - int(25 * scale)
    draw.line([seat_cluster, (seat_cluster[0], seat_y)], fill=COLORS['gray_600'], width=3)
    draw.line([(seat_cluster[0] - 15, seat_y), (seat_cluster[0] + 15, seat_y)], fill=COLORS['gray_500'], width=4)
    
    # Crank (simplified)
    draw.ellipse([bottom_bracket[0] - 10, bottom_bracket[1] - 10,
                  bottom_bracket[0] + 10, bottom_bracket[1] + 10],
                 fill=COLORS['gray_700'])
    draw.line([bottom_bracket, (bottom_bracket[0] + 20, bottom_bracket[1] + 15)], 
              fill=COLORS['gray_500'], width=4)
    
    # Gold accent highlights on frame
    highlight_offset = 2
    draw.line([seat_cluster, head_tube_top], fill=COLORS['gold_light'], width=1)

def generate_hero_image():
    """Generate premium hero/showroom background"""
    print("[ART] Generating hero-showroom-2.jpg...")
    
    width, height = 1792, 1024
    
    # Create dark gradient background
    img = create_gradient(width, height, COLORS['bg_black'], COLORS['bg_dark'], 'diagonal')
    draw = ImageDraw.Draw(img)
    
    # Add subtle grid pattern (floor)
    floor_y = height * 0.65
    for i in range(-20, 25):
        x = width // 2 + i * 80
        # Perspective lines
        draw.line([(x, floor_y), (width // 2 + i * 200, height)], 
                  fill=COLORS['gray_900'], width=1)
    
    # Add horizontal lines
    for y in range(int(floor_y), height, 40):
        draw.line([(0, y), (width, y)], fill=COLORS['gray_900'], width=1)
    
    # Draw luxury bikes silhouettes
    bike_positions = [
        (width * 0.2, floor_y - 80, 0.8),
        (width * 0.5, floor_y - 100, 1.0),
        (width * 0.8, floor_y - 80, 0.8),
    ]
    
    for bx, by, scale in bike_positions:
        draw_luxury_bike_frame(draw, int(bx), int(by), scale)
    
    # Add gold accent lights (ceiling spots)
    for i in range(5):
        x = width * 0.15 + i * width * 0.18
        # Light cone effect
        for r in range(100, 0, -5):
            alpha = int(10 * (r / 100))
            color = (*hex_to_rgb(COLORS['gold']), alpha)
            draw.ellipse([x - r, 0, x + r, r * 2], fill=None, outline=COLORS['gold_dark'])
    
    # Add vignette
    img = add_vignette(img, 0.5)
    
    # Add noise for texture
    img = add_noise(img, 0.01)
    
    img.save(OUTPUT_DIR / 'hero-showroom-2.jpg', 'JPEG', quality=95)
    print("[OK] Saved hero-showroom-2.jpg")

def generate_bike_product(index, name, color_scheme='gold'):
    """Generate premium bike product shot"""
    filename = f"bike-{index}.jpg"
    print(f"[ART] Generating {filename} ({name})...")
    
    width, height = 1024, 768
    
    # Create clean gradient background (studio look)
    img = create_gradient(width, height, COLORS['bg_card'], COLORS['bg_elevated'], 'vertical')
    draw = ImageDraw.Draw(img)
    
    # Center position
    cx, cy = width // 2, height // 2 + 50
    
    # Draw bike frame
    scale = 1.5
    draw_luxury_bike_frame(draw, cx, cy, scale, color_scheme)
    
    # Add subtle shadow beneath bike
    shadow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.ellipse([cx - 200, cy + 120, cx + 200, cy + 160], 
                        fill=(0, 0, 0, 80))
    img = Image.alpha_composite(img.convert('RGBA'), shadow).convert('RGB')
    
    # Add subtle vignette
    img = add_vignette(img, 0.3)
    
    img.save(OUTPUT_DIR / filename, 'JPEG', quality=95)
    print(f"[OK] Saved {filename}")

def generate_avatar(index, name):
    """Generate professional avatar placeholder"""
    filename = f"avatar-{index}.jpg"
    print(f"[ART] Generating {filename} ({name})...")
    
    size = 512
    img = Image.new('RGB', (size, size), hex_to_rgb(COLORS['bg_card']))
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for y in range(size):
        ratio = y / size
        r = int(17 + (26 - 17) * ratio)
        g = int(17 + (26 - 17) * ratio)
        b = int(17 + (26 - 17) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    
    # Draw stylized person silhouette
    cx, cy = size // 2, size // 2
    
    # Head
    head_radius = 80
    draw.ellipse([cx - head_radius, cy - head_radius - 30,
                  cx + head_radius, cy + head_radius - 30],
                 fill=hex_to_rgb(COLORS['gray_700']))
    
    # Gold accent ring
    draw.ellipse([cx - head_radius - 5, cy - head_radius - 35,
                  cx + head_radius + 5, cy + head_radius - 25],
                 outline=hex_to_rgb(COLORS['gold']), width=3)
    
    # Shoulders
    draw.ellipse([cx - 140, cy + 60, cx + 140, cy + 220],
                 fill=hex_to_rgb(COLORS['gray_800']))
    
    # Gold accent line
    draw.line([(cx - 60, cy + 150), (cx + 60, cy + 150)],
              fill=hex_to_rgb(COLORS['gold']), width=2)
    
    # Add subtle vignette
    img = add_vignette(img, 0.4)
    
    img.save(OUTPUT_DIR / filename, 'JPEG', quality=95)
    print(f"[OK] Saved {filename}")

def generate_instagram(index, style='detail'):
    """Generate Instagram post image"""
    filename = f"insta-{index}.jpg"
    print(f"[ART] Generating {filename}...")
    
    size = 1024
    img = Image.new('RGB', (size, size), hex_to_rgb(COLORS['bg_dark']))
    draw = ImageDraw.Draw(img)
    
    if style == 'detail':
        # Macro detail style - drivetrain closeup
        cx, cy = size // 2, size // 2
        
        # Draw chainring
        for r in range(200, 50, -20):
            color_val = 40 + (200 - r) // 3
            draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                        fill=(color_val, color_val, color_val + 10))
        
        # Gold chain
        chain_radius = 140
        for angle in range(0, 360, 15):
            rad = math.radians(angle)
            x = cx + int(chain_radius * math.cos(rad))
            y = cy + int(chain_radius * math.sin(rad))
            draw.ellipse([x - 4, y - 4, x + 4, y + 4], 
                        fill=hex_to_rgb(COLORS['gold']))
        
        # Gold accents
        draw.ellipse([cx - 60, cy - 60, cx + 60, cy + 60],
                    outline=hex_to_rgb(COLORS['gold']), width=3)
        
    elif style == 'lifestyle':
        # Road stretching into distance
        horizon_y = size // 3
        
        # Sky gradient
        for y in range(horizon_y):
            ratio = y / horizon_y
            r = int(5 + 20 * ratio)
            g = int(5 + 15 * ratio)
            b = int(10 + 30 * ratio)
            draw.line([(0, y), (size, y)], fill=(r, g, b))
        
        # Road
        road_top = size * 0.4
        for y in range(horizon_y, size):
            progress = (y - horizon_y) / (size - horizon_y)
            road_width = size * 0.1 + (size * 0.8) * progress
            left = (size - road_width) // 2
            right = left + road_width
            gray = int(30 + 40 * progress)
            draw.line([(left, y), (right, y)], fill=(gray, gray, gray))
        
        # Gold sunset line
        draw.line([(0, horizon_y), (size, horizon_y)], 
                  fill=hex_to_rgb(COLORS['gold']), width=3)
    
    else:
        # Bike silhouette
        draw_luxury_bike_frame(draw, size // 2, size // 2 + 100, 1.5)
    
    # Add vignette
    img = add_vignette(img, 0.4)
    
    img.save(OUTPUT_DIR / filename, 'JPEG', quality=95)
    print(f"[OK] Saved {filename}")

def generate_og_image():
    """Generate Open Graph social sharing image"""
    print("[ART] Generating og-image.jpg...")
    
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), hex_to_rgb(COLORS['bg_black']))
    draw = ImageDraw.Draw(img)
    
    # Background gradient
    for y in range(height):
        ratio = y / height
        r = int(5 + 15 * ratio)
        g = int(5 + 15 * ratio)
        b = int(5 + 20 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Draw bikes on left side
    draw_luxury_bike_frame(draw, 300, 400, 1.2)
    
    # Gold accent line separator
    draw.line([(width // 2, 100), (width // 2, height - 100)],
              fill=hex_to_rgb(COLORS['gold']), width=2)
    
    # Gold decorative elements
    draw.rectangle([width - 100, 0, width, 10], fill=hex_to_rgb(COLORS['gold']))
    draw.rectangle([width - 50, height - 10, width, height], fill=hex_to_rgb(COLORS['gold']))
    
    # Add vignette
    img = add_vignette(img, 0.3)
    
    img.save(OUTPUT_DIR / 'og-image.jpg', 'JPEG', quality=95)
    print("[OK] Saved og-image.jpg")

def main():
    """Generate all luxury images"""
    print("=" * 70)
    print("GET A BIKE - LUXURY IMAGE GENERATION (PREMIUM EDITION)")
    print("=" * 70)
    print()
    
    # Generate hero image
    generate_hero_image()
    
    # Generate bike product images
    bikes = [
        ("Trek Madone SLR 9", 'gold'),
        ("Specialized S-Works Tarmac", 'gold'),
        ("Cervélo R5 Disc", 'gold'),
        ("3T Exploro Racemax", 'gold'),
        ("Specialized Turbo Levo", 'gold'),
        ("Santa Cruz Hightower", 'gold'),
        ("Canyon Grail CF SLX", 'gold'),
        ("BMC Roadmachine 01", 'gold'),
    ]
    
    for i, (name, color) in enumerate(bikes, 1):
        generate_bike_product(i, name, color)
    
    # Generate avatars
    avatars = ["Marcus Chen", "Sarah Williams", "David Rodriguez"]
    for i, name in enumerate(avatars, 1):
        generate_avatar(i, name)
    
    # Generate Instagram images
    styles = ['detail', 'lifestyle', 'bike', 'detail', 'lifestyle', 'bike']
    for i, style in enumerate(styles, 1):
        generate_instagram(i, style)
    
    # Generate OG image
    generate_og_image()
    
    print()
    print("=" * 70)
    print("ALL IMAGES GENERATED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\n📁 Output directory: {OUTPUT_DIR.absolute()}")
    print(f"[COUNT] Total images: 19")
    print()
    print("Next steps:")
    print("  1. Copy hero-showroom-2.jpg to hero-poster.jpg")
    print("  2. Run 'npm run build' to rebuild the site")
    print("  3. Deploy to hosting")
    print()

if __name__ == "__main__":
    main()
