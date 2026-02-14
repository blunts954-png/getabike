#!/usr/bin/env python3
"""
Generate high-quality placeholder images for Get A Bike website
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math
import random

# Create output directories
os.makedirs("public/assets", exist_ok=True)

# Color palette - professional, cycling-themed
COLORS = {
    'bg_dark': '#0a0a0f',
    'bg_card': '#141419',
    'accent_red': '#e63946',
    'accent_blue': '#00a8e8',
    'accent_gold': '#f4a261',
    'text_white': '#ffffff',
    'text_gray': '#a0a0a0',
    'metal': '#4a5568',
    'carbon': '#1a1a2e',
    'tire': '#0f0f15',
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_bg(width, height, color1, color2, direction='vertical'):
    """Create a gradient background"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    c1 = hex_to_rgb(color1)
    c2 = hex_to_rgb(color2)
    
    for y in range(height):
        if direction == 'vertical':
            ratio = y / height
        else:
            ratio = y / height  # For simplicity, using vertical logic
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img

def draw_bike_frame(draw, cx, cy, scale=1.0, frame_color='#e63946', accent_color='#00a8e8'):
    """Draw a stylized road/gravel bike frame"""
    s = scale
    
    # Wheel positions
    rear_wheel = (cx - 120*s, cy + 40*s)
    front_wheel = (cx + 120*s, cy + 40*s)
    bottom_bracket = (cx - 20*s, cy + 40*s)
    seat_cluster = (cx - 30*s, cy - 60*s)
    head_tube_top = (cx + 70*s, cy - 50*s)
    head_tube_bottom = (cx + 75*s, cy - 10*s)
    
    # Wheels
    for wheel_pos in [rear_wheel, front_wheel]:
        # Tire
        draw.ellipse([wheel_pos[0]-45*s, wheel_pos[1]-45*s, 
                      wheel_pos[0]+45*s, wheel_pos[1]+45*s], 
                     outline=hex_to_rgb(COLORS['tire']), width=int(6*s))
        # Rim
        draw.ellipse([wheel_pos[0]-35*s, wheel_pos[1]-35*s, 
                      wheel_pos[0]+35*s, wheel_pos[1]+35*s], 
                     outline=hex_to_rgb(COLORS['metal']), width=int(3*s))
        # Spokes
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = wheel_pos[0] + math.cos(rad) * 10*s
            y1 = wheel_pos[1] + math.sin(rad) * 10*s
            x2 = wheel_pos[0] + math.cos(rad) * 32*s
            y2 = wheel_pos[1] + math.sin(rad) * 32*s
            draw.line([(x1, y1), (x2, y2)], fill=hex_to_rgb(COLORS['metal']), width=int(1*s))
    
    # Frame - using bezier-like curves
    frame_rgb = hex_to_rgb(frame_color)
    
    # Chainstay
    draw.line([rear_wheel, bottom_bracket], fill=frame_rgb, width=int(5*s))
    # Seatstay
    draw.line([rear_wheel, seat_cluster], fill=frame_rgb, width=int(4*s))
    # Seat tube
    draw.line([bottom_bracket, seat_cluster], fill=frame_rgb, width=int(5*s))
    # Down tube
    draw.line([bottom_bracket, head_tube_bottom], fill=frame_rgb, width=int(6*s))
    # Top tube
    draw.line([seat_cluster, head_tube_top], fill=frame_rgb, width=int(5*s))
    # Head tube
    draw.line([head_tube_top, head_tube_bottom], fill=frame_rgb, width=int(6*s))
    
    # Fork
    draw.line([front_wheel, head_tube_bottom], fill=hex_to_rgb(COLORS['carbon']), width=int(4*s))
    
    # Handlebars
    hb_x, hb_y = head_tube_top[0] + 15*s, head_tube_top[1] - 5*s
    draw.line([(hb_x, hb_y), (hb_x + 20*s, hb_y - 10*s)], fill=hex_to_rgb(COLORS['metal']), width=int(3*s))
    
    # Seat post and saddle
    seat_top = (seat_cluster[0] - 5*s, seat_cluster[1] - 25*s)
    draw.line([seat_cluster, seat_top], fill=hex_to_rgb(COLORS['carbon']), width=int(4*s))
    # Saddle
    draw.line([(seat_top[0] - 15*s, seat_top[1]), (seat_top[0] + 15*s, seat_top[1])], 
              fill=hex_to_rgb(COLORS['tire']), width=int(5*s))
    
    # Crank/Chainring
    draw.ellipse([bottom_bracket[0]-12*s, bottom_bracket[1]-12*s,
                  bottom_bracket[0]+12*s, bottom_bracket[1]+12*s],
                 outline=hex_to_rgb(COLORS['metal']), width=int(3*s))

def generate_bike_image(filename, bike_name, bike_type, specs, price, frame_color, bg_gradient):
    """Generate a premium bike card image"""
    width, height = 640, 480
    
    # Create gradient background
    img = create_gradient_bg(width, height, bg_gradient[0], bg_gradient[1])
    draw = ImageDraw.Draw(img)
    
    # Add subtle noise/texture overlay
    for _ in range(1000):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        draw.point((x, y), fill=(255, 255, 255, 10))
    
    # Draw bike
    draw_bike_frame(draw, 320, 220, scale=1.2, frame_color=frame_color)
    
    # Add text
    try:
        # Try to use default font
        font_title = ImageFont.truetype("arial.ttf", 36)
        font_specs = ImageFont.truetype("arial.ttf", 20)
        font_price = ImageFont.truetype("arial.ttf", 42)
        font_badge = ImageFont.truetype("arial.ttf", 16)
    except:
        font_title = ImageFont.load_default()
        font_specs = font_title
        font_price = font_title
        font_badge = font_title
    
    # Badge
    badge_text = "CERTIFIED PRE-OWNED"
    badge_width = 200
    badge_height = 28
    draw.rounded_rectangle([30, 30, 30+badge_width, 30+badge_height], 
                           radius=4, fill=hex_to_rgb(COLORS['accent_red']))
    draw.text((40, 33), badge_text, fill=hex_to_rgb(COLORS['text_white']), font=font_badge)
    
    # Bike name
    draw.text((30, 320), bike_name, fill=hex_to_rgb(COLORS['text_white']), font=font_title)
    
    # Specs
    draw.text((30, 370), specs, fill=hex_to_rgb(COLORS['text_gray']), font=font_specs)
    
    # Price - right aligned
    price_width = draw.textlength(price, font=font_price)
    draw.text((width - 30 - price_width, 360), price, fill=hex_to_rgb(COLORS['accent_red']), font=font_price)
    
    img.save(filename, quality=95)
    print(f"Generated: {filename}")

def generate_avatar(filename, name, role, color_scheme):
    """Generate a professional avatar image"""
    width, height = 200, 200
    
    # Background
    img = Image.new('RGB', (width, height), hex_to_rgb(COLORS['bg_card']))
    draw = ImageDraw.Draw(img)
    
    # Draw stylized person
    cx, cy = width // 2, height // 2 + 10
    
    # Background circle
    draw.ellipse([20, 20, 180, 180], fill=hex_to_rgb(color_scheme))
    
    # Head
    head_y = cy - 30
    draw.ellipse([cx-35, head_y-35, cx+35, head_y+35], fill=(240, 220, 200))
    
    # Hair (stylized)
    hair_color = (60, 40, 30) if random.random() > 0.5 else (120, 80, 50)
    draw.arc([cx-40, head_y-45, cx+40, head_y+20], start=0, end=180, fill=hair_color, width=15)
    
    # Body/Shoulders
    draw.ellipse([cx-60, cy+20, cx+60, cy+80], fill=(80, 80, 90))
    
    img.save(filename, quality=95)
    print(f"Generated: {filename}")

def generate_instagram_tile(filename, type_name, bg_colors):
    """Generate Instagram lifestyle image"""
    width, height = 400, 400
    
    img = create_gradient_bg(width, height, bg_colors[0], bg_colors[1])
    draw = ImageDraw.Draw(img)
    
    # Add stylized cycling elements
    if 'trail' in filename:
        # Mountain trail scene
        # Mountains
        draw.polygon([(0, 250), (100, 150), (200, 200), (300, 120), (400, 250), (400, 400), (0, 400)], 
                     fill=hex_to_rgb('#1a1a2e'))
        # Sun
        draw.ellipse([280, 50, 350, 120], fill=hex_to_rgb(COLORS['accent_gold']))
    elif 'road' in filename:
        # Road cycling scene
        # Road
        draw.polygon([(0, 300), (400, 300), (400, 400), (0, 400)], fill=hex_to_rgb('#2d3748'))
        # Road lines
        draw.line([(200, 320), (200, 400)], fill=hex_to_rgb(COLORS['accent_gold']), width=4)
        # Sky gradient effect
    elif 'shop' in filename:
        # Shop interior
        # Shelves
        for y in [150, 250, 350]:
            draw.line([(50, y), (350, y)], fill=hex_to_rgb(COLORS['metal']), width=3)
    else:
        # Generic cycling - bike silhouette
        draw_bike_frame(draw, 200, 200, scale=0.8, frame_color=COLORS['accent_red'])
    
    # Vignette effect
    for i in range(50):
        alpha = int(255 * (i / 50) * 0.3)
        draw.rectangle([i, i, width-i, height-i], outline=(0, 0, 0))
    
    img.save(filename, quality=90)
    print(f"Generated: {filename}")

def generate_hero_poster(filename):
    """Generate hero poster image"""
    width, height = 1920, 1080
    
    # Dark dramatic gradient
    img = create_gradient_bg(width, height, '#050508', '#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Add dramatic lighting effect
    for i in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height//2)
        size = random.randint(1, 3)
        draw.ellipse([x, y, x+size, y+size], fill=(255, 255, 255, 30))
    
    # Draw hero bike (larger, more detailed)
    draw_bike_frame(draw, width//2, height//2 + 100, scale=2.5, frame_color=COLORS['accent_red'])
    
    img.save(filename, quality=95)
    print(f"Generated: {filename}")

def generate_video_thumbnail(filename):
    """Generate video thumbnail with play button"""
    width, height = 640, 360
    
    img = create_gradient_bg(width, height, '#0a0a0f', '#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Draw multiple bike silhouettes
    positions = [(150, 200), (320, 180), (490, 200)]
    colors = [COLORS['accent_red'], COLORS['accent_blue'], COLORS['accent_gold']]
    
    for pos, color in zip(positions, colors):
        draw_bike_frame(draw, pos[0], pos[1], scale=0.8, frame_color=color)
    
    # Play button
    cx, cy = width // 2, height // 2
    triangle_size = 40
    draw.regular_polygon((cx, cy, triangle_size), 3, rotation=90, 
                         fill=hex_to_rgb(COLORS['accent_red']))
    
    img.save(filename, quality=95)
    print(f"Generated: {filename}")

if __name__ == "__main__":
    print("Generating high-quality bike shop images...")
    
    # Generate bike images
    bikes = [
        ("bike-1.jpg", "Jamis Renegade S4", "Gravel", "Gravel | 54cm | Shimano GRX", "$1,899", 
         COLORS['accent_red'], ('#0a0a0f', '#1a1a1e')),
        ("bike-2.jpg", "Bianchi Oltre XR3", "Road", "Road | 56cm | Ultegra", "$2,950", 
         COLORS['accent_blue'], ('#0a0a0f', '#1a1a2e')),
        ("bike-3.jpg", "Specialized Turbo Vado", "Electric", "Electric | M | 70mi Range", "$2,499", 
         COLORS['accent_gold'], ('#0a0a0f', '#1e1a0a')),
        ("bike-4.jpg", "3T Exploro Racemax", "Gravel", "Gravel | 58cm | SRAM Rival", "$3,200", 
         '#e76f51', ('#0a0a0f', '#1a0f0a')),
    ]
    
    for bike in bikes:
        generate_bike_image(f"public/assets/{bike[0]}", *bike[1:])
    
    # Generate avatars
    avatars = [
        ("avatar-1.jpg", "Alex R.", "Road Rider", COLORS['accent_blue']),
        ("avatar-2.jpg", "Jamie L.", "Gravel Enthusiast", COLORS['accent_gold']),
        ("avatar-3.jpg", "Morgan K.", "Commuter", COLORS['accent_red']),
    ]
    
    for avatar in avatars:
        generate_avatar(f"public/assets/{avatar[0]}", *avatar[1:])
    
    # Generate Instagram tiles
    insta_tiles = [
        ("insta-1.jpg", "trail", ('#1a1a2e', '#0a0a0f')),
        ("insta-2.jpg", "road", ('#0f172a', '#1e293b')),
        ("insta-3.jpg", "shop", ('#1a1a1e', '#0a0a0f')),
        ("insta-4.jpg", "ride", ('#1e1a0a', '#0a0a0f')),
        ("insta-5.jpg", "event", ('#0f0f15', '#1a1a2e')),
        ("insta-6.jpg", "community", ('#1a0f0a', '#0a0a0f')),
    ]
    
    for tile in insta_tiles:
        generate_instagram_tile(f"public/assets/{tile[0]}", *tile[1:])
    
    # Generate hero poster and video thumbnail
    generate_hero_poster("public/assets/hero-poster.jpg")
    generate_video_thumbnail("public/assets/video-placeholder.jpg")
    
    print("\n✅ All images generated successfully!")
