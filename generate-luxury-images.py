#!/usr/bin/env python3
"""
GET A BIKE - LUXURY IMAGE GENERATION SYSTEM
Generates premium, million-dollar aesthetic images for the website

Requires: TOGETHER_API_KEY environment variable
"""

import os
import requests
import base64
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

# Configuration
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")
OUTPUT_DIR = Path("public/assets")
IMAGE_WIDTH = 1536
IMAGE_HEIGHT = 1024

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# HERO IMAGES - Luxury Showroom Backgrounds
# ============================================================================

HERO_IMAGES = [
    {
        "filename": "hero-poster.jpg",
        "prompt": """Ultra-wide cinematic photograph of a premium luxury bicycle showroom interior. 
Sleek obsidian black walls with warm gold accent track lighting. 
High-end carbon fiber road bikes displayed on minimalist illuminated white pedestals like art gallery pieces.
Polished black marble floor with subtle gold veining, reflecting the bikes.
Floor-to-ceiling windows with soft natural light filtering through sheer curtains.
Exclusive members-only boutique atmosphere. Dramatic side lighting creating depth.
Architectural photography style, Hasselblad medium format quality, 8k resolution.
Color palette: deep black, warm gold accents, subtle white highlights.
Professional interior design photography, shallow depth of field, luxurious and exclusive mood.""",
        "width": 1792,
        "height": 1024,
    },
    {
        "filename": "hero-showroom-2.jpg",
        "prompt": """Dramatic low angle interior shot of ultra-premium bike gallery. 
Tall ceiling with suspended gold accent lights. 
Rows of pristine carbon fiber bicycles in matte black, white, and metallic finishes.
Glass display cases with cycling accessories. Polished concrete with gold terrazzo.
Contemporary architecture with curved walls. Golden hour light streaming through clerestory windows.
Minimalist luxury aesthetic, Architectural Digest quality, 8k professional photography.
Color scheme: black, gold, cream, warm wood tones. Sophisticated and aspirational atmosphere.""",
        "width": 1792,
        "height": 1024,
    },
]

# ============================================================================
# BIKE PRODUCT IMAGES - Premium Individual Shots
# ============================================================================

BIKE_IMAGES = [
    {
        "filename": "bike-1.jpg",
        "bike": "Trek Madone SLR 9",
        "prompt": """Professional product photography of a Trek Madone SLR 9 road bike.
Matte deep navy blue carbon fiber frame with subtle metallic flake.
Gold accent decals and highlights on frame. Shimano Dura-Ace Di2 groupset visible.
Carbon deep-section wheels with gold rim accents. 
Pure white cyclorama studio background. Dramatic rim lighting creating glow around the frame.
3/4 front angle view showcasing the aero design. Perfect studio conditions, dust-free, pristine.
Automotive advertising photography style, 8k ultra-sharp detail.
Product photography lighting: soft key light, dramatic fill, black negative fill for contrast.
Every component in perfect condition, showroom quality.""",
    },
    {
        "filename": "bike-2.jpg",
        "bike": "Specialized S-Works Tarmac",
        "prompt": """Professional product photography of Specialized S-Works Tarmac road bicycle.
Glossy metallic black carbon frame with iridescent rainbow flake in clear coat.
Gold anodized stem and handlebar accents. SRAM Red eTap AXS components in polished silver.
Roval Rapide CLX wheels in satin carbon. Pure white studio background.
Side profile view with slight front angle. Perfect lighting showing frame contours.
Studio photography with softbox and beauty dish setup. 8k commercial photography.
Automotive quality product shot, sharp focus throughout, luxury sports car aesthetic.""",
    },
    {
        "filename": "bike-3.jpg",
        "bike": "Cervélo R5 Disc",
        "prompt": """Professional product photography of Cervélo R5 Disc road bike.
Matte stealth black carbon frame with red accent decals. 
Ultegra Di2 electronic groupset, carbon wheels with white sidewall tires.
Minimalist studio setup with gradient gray background from dark to light.
Angled 3/4 view from drivetrain side. Rim lighting accentuating frame tubes.
Dust-free pristine condition, every detail sharp. 
Professional cycling catalog photography, 8k resolution.
Clean, technical, precise aesthetic. High-end sports equipment photography.""",
    },
    {
        "filename": "bike-4.jpg",
        "bike": "3T Exploro Racemax",
        "prompt": """Professional product photography of 3T Exploro Racemax gravel bike.
Raw carbon fiber frame showing weave texture with matte clear coat.
Tan sidewall WTB tires, SRAM Eagle AXS drivetrain in rainbow titanium finish.
Minimalist white studio background. Dramatic low angle shot emphasizing adventure capability.
Dirt and dust free, pristine condition. Studio lighting with soft shadows.
Gravel bike magazine cover quality. 8k ultra-detailed photography.
Rugged yet refined aesthetic, premium outdoor equipment style.""",
    },
    {
        "filename": "bike-5.jpg",
        "bike": "Specialized Turbo Levo",
        "prompt": """Professional product photography of Specialized Turbo Levo electric mountain bike.
Stealth black carbon frame with integrated battery. Gold FOX suspension fork accents.
Premium e-MTB with discrete motor integration. Carbon wheels with Maxxis tires.
Dark gradient studio background from charcoal to black. Dramatic side lighting.
Front 3/4 angle showing the electric components subtly integrated.
Futuristic yet elegant presentation. 8k professional product photography.
Tech-luxury aesthetic, Apple product photography style. Clean, sophisticated, powerful.""",
    },
    {
        "filename": "bike-6.jpg",
        "bike": "Santa Cruz Hightower",
        "prompt": """Professional product photography of Santa Cruz Hightower mountain bike.
Matte olive green carbon frame with gold linkages. 
XX1 AXS Reserve build with carbon wheels and gold spoke nipples.
Kashima coated FOX suspension. Studio white background.
Aggressive stance shot from low angle. Rim lighting on suspension components.
Premium MTB catalog photography. 8k resolution, tack sharp.
Adventure-ready yet refined aesthetic. Professional cycling industry photography.""",
    },
    {
        "filename": "bike-7.jpg",
        "bike": "Canyon Grail CF SLX",
        "prompt": """Professional product photography of Canyon Grail CF SLX gravel bike.
Stealth black frame with integrated cockpit. GRX Di2 groupset.
Double-decker handlebar unique design visible. 45mm tan sidewall tires.
Pure white studio background, minimalist presentation.
Side profile view showing the unique handlebar. Clean studio lighting.
Contemporary product photography aesthetic. 8k sharp detail.
Innovative yet elegant, premium European design style.""",
    },
    {
        "filename": "bike-8.jpg",
        "bike": "BMC Roadmachine 01",
        "prompt": """Professional product photography of BMC Roadmachine 01 endurance road bike.
Glossy metallic dark gray frame with champagne gold accents.
SRAM Force AXS groupset with gold chain. Zipp carbon wheels.
White studio cyclorama background. 3/4 front angle showing endurance geometry.
Dramatic studio lighting with gold rim accents highlighted.
Swiss precision aesthetic, luxury watch advertising style. 8k commercial photography.
Refined, sophisticated, endurance racing elegance.""",
    },
]

# ============================================================================
# CUSTOMER AVATARS - Professional Headshots
# ============================================================================

AVATAR_IMAGES = [
    {
        "filename": "avatar-1.jpg",
        "name": "Marcus Chen",
        "prompt": """Professional corporate headshot portrait of an Asian-American man, 42 years old, athletic fit cyclist build.
Confident warm smile showing teeth. Short black hair with subtle gray at temples, neatly styled.
Clean shaven, healthy tanned skin from outdoor activities.
Wearing premium black cycling jersey with subtle gold accents.
Soft studio lighting, Rembrandt lighting pattern. Neutral warm gray background.
Shallow depth of field, 85mm lens equivalent bokeh.
Executive headshot photography style, approachable yet professional.
8k portrait photography, skin texture detail, warm and trustworthy expression.
Corporate headshot meets athletic lifestyle aesthetic.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "avatar-2.jpg",
        "name": "Sarah Williams",
        "prompt": """Professional lifestyle headshot of a Caucasian woman, 38 years old, fit athletic build.
Genuine warm smile, crinkled eyes showing authenticity. 
Blonde hair in a stylish ponytail, sun-kissed healthy skin with light freckles.
Wearing navy blue premium cycling kit, pearl earrings.
Natural window lighting, soft and flattering. Clean white studio background.
Lifestyle portrait photography style, approachable and energetic.
8k high resolution, professional makeup, healthy vibrant appearance.
Athletic yet feminine, gran fondo rider aesthetic. Confident and friendly expression.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "avatar-3.jpg",
        "name": "David Rodriguez",
        "prompt": """Professional portrait headshot of a Hispanic man, 48 years old, lean cyclist physique.
Well-groomed salt and pepper beard and mustache, short styled hair.
Warm intelligent expression, slight confident smile, distinguished appearance.
Wearing charcoal gray polo shirt with subtle texture.
Professional studio lighting with soft key and fill. Neutral gray background.
Executive portrait photography style, successful and accomplished vibe.
8k detail, character and wisdom in expression.
Cat 1 racer aesthetic, serious cyclist, knowledgeable and trustworthy appearance.""",
        "width": 1024,
        "height": 1024,
    },
]

# ============================================================================
# INSTAGRAM GALLERY IMAGES - Lifestyle & Detail Shots
# ============================================================================

INSTAGRAM_IMAGES = [
    {
        "filename": "insta-1.jpg",
        "prompt": """Macro detail photography of premium road bike drivetrain close-up.
Gold bicycle chain on black ceramic speed pulleys. Carbon fiber rear derailleur cage.
Intricate mechanical detail, shallow depth of field.
Dark moody background, dramatic side lighting highlighting metallic surfaces.
Luxury watch photography style applied to bike components.
8k extreme detail, dust-free, pristine condition.
Artistic mechanical photography, industrial beauty.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "insta-2.jpg",
        "prompt": """Close-up of premium road bike cockpit detail. 
Carbon fiber handlebar with gold anodized stem. Black leather bar tape with gold stitching.
Integrated GPS computer mount. Hydraulic brake lines neatly routed.
Studio lighting on gradient black background.
Automotive detail photography aesthetic. 8k macro detail.
Luxury craftsmanship showcase, precision engineering beauty.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "insta-3.jpg",
        "prompt": """Golden hour lifestyle shot of cyclist silhouette on premium road bike.
Rolling California hills in background. Warm orange and gold sunset light.
Lens flare creating dreamy atmosphere. Rider in premium black kit.
Asphalt road stretching into distance. Inspirational cycling photography.
8k landscape with subject, epic and aspirational mood.
Strava-worthy shot, cycling lifestyle dream imagery.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "insta-4.jpg",
        "prompt": """Premium road bike leaning against artisan coffee shop exterior.
Urban cycling culture aesthetic. Matte black bike, gold accents.
Exposed brick wall background. Morning soft light.
Cycling cap on handlebars. Espresso cup visible.
Hipster meets luxury aesthetic. 8k lifestyle photography.
Coffee ride culture, weekend warrior vibe, aspirational urban lifestyle.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "insta-5.jpg",
        "prompt": """Overhead drone shot of group ride on scenic mountain road.
Four cyclists in colorful premium kits. Winding road through forest.
Morning mist in valleys. Epic scale and grandeur.
Peloton formation, camaraderie and adventure.
Aerial perspective photography. 8k resolution.
Cycling community, group ride inspiration, adventure awaits mood.""",
        "width": 1024,
        "height": 1024,
    },
    {
        "filename": "insta-6.jpg",
        "prompt": """Detail shot of premium cycling shoes and carbon bike.
White S-Works or equivalent shoes with gold cleats.
Carbon crank arm and chainring visible. Clean asphalt surface.
Composition showing power transfer elegance.
Product photography lighting. 8k detail.
Watts and style, power and elegance, serious cyclist aesthetic.""",
        "width": 1024,
        "height": 1024,
    },
]

# ============================================================================
# ADDITIONAL LUXURY ASSETS
# ============================================================================

ADDITIONAL_IMAGES = [
    {
        "filename": "og-image.jpg",
        "prompt": """Social media banner image for luxury bike shop.
Split composition: left side premium bike showroom interior, right side dramatic bike detail.
"Get A Bike Bakersfield" elegant typography space (text will be added separately).
Black and gold color scheme. Sophisticated luxury brand aesthetic.
High-end automotive advertising style. 8k marketing asset.
Premium, exclusive, million-dollar brand feel.""",
        "width": 1792,
        "height": 1024,
    },
    {
        "filename": "workshop-detail.jpg",
        "prompt": """Professional bike mechanic working on premium road bike in immaculate workshop.
Clean organized tool wall in background. Mechanic wearing black uniform with gold logo space.
Carbon bike on professional repair stand. Workshop lighting bright and even.
Documentary photography style but polished. 8k professional.
Craftsmanship, expertise, premium service aesthetic.""",
        "width": 1536,
        "height": 1024,
    },
    {
        "filename": "fitting-session.jpg",
        "prompt": """Professional bike fitting session in progress. 
Expert fitter measuring client on premium road bike on trainer.
Retul or equivalent motion capture system visible. 
Clean modern fitting studio with white walls. Professional lighting.
Client in premium cycling kit, focused expression.
Healthcare meets luxury retail aesthetic. 8k photography.
Professional service, expertise, personalized attention mood.""",
        "width": 1536,
        "height": 1024,
    },
]

# ============================================================================
# IMAGE GENERATION FUNCTION
# ============================================================================

def generate_image(prompt, filename, width=IMAGE_WIDTH, height=IMAGE_HEIGHT):
    """Generate a single image using Together AI API"""
    
    if not TOGETHER_API_KEY:
        print(f"❌ Skipping {filename} - No API key found")
        return False
    
    output_path = OUTPUT_DIR / filename
    
    # Skip if already exists
    if output_path.exists():
        print(f"⏭️  Skipping {filename} - already exists")
        return True
    
    print(f"🎨 Generating: {filename}")
    
    try:
        response = requests.post(
            "https://api.together.xyz/v1/images/generations",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "black-forest-labs/FLUX.1-pro",  # High quality model
                "prompt": prompt,
                "width": width,
                "height": height,
                "steps": 50,
                "n": 1,
                "response_format": "b64_json",
            },
            timeout=120,
        )
        
        response.raise_for_status()
        data = response.json()
        
        if "data" in data and len(data["data"]) > 0:
            image_data = base64.b64decode(data["data"][0]["b64_json"])
            
            with open(output_path, "wb") as f:
                f.write(image_data)
            
            print(f"✅ Saved: {filename}")
            return True
        else:
            print(f"❌ Failed: {filename} - No image data in response")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error generating {filename}: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error for {filename}: {e}")
        return False


def generate_all_images():
    """Generate all images in batches"""
    
    print("=" * 70)
    print("GET A BIKE - LUXURY IMAGE GENERATION SYSTEM")
    print("=" * 70)
    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}")
    print(f"API Key present: {'Yes' if TOGETHER_API_KEY else 'No'}")
    print()
    
    if not TOGETHER_API_KEY:
        print("⚠️  WARNING: TOGETHER_API_KEY environment variable not set!")
        print("Set it with: export TOGETHER_API_KEY='your-key-here'")
        print()
        return
    
    # Combine all images to generate
    all_images = []
    
    # Add hero images
    for img in HERO_IMAGES:
        all_images.append((img["prompt"], img["filename"], img.get("width", IMAGE_WIDTH), img.get("height", IMAGE_HEIGHT)))
    
    # Add bike images
    for img in BIKE_IMAGES:
        all_images.append((img["prompt"], img["filename"], IMAGE_WIDTH, IMAGE_HEIGHT))
    
    # Add avatar images
    for img in AVATAR_IMAGES:
        all_images.append((img["prompt"], img["filename"], img.get("width", 1024), img.get("height", 1024)))
    
    # Add Instagram images
    for img in INSTAGRAM_IMAGES:
        all_images.append((img["prompt"], img["filename"], img.get("width", 1024), img.get("height", 1024)))
    
    # Add additional images
    for img in ADDITIONAL_IMAGES:
        all_images.append((img["prompt"], img["filename"], img.get("width", IMAGE_WIDTH), img.get("height", IMAGE_HEIGHT)))
    
    print(f"Total images to generate: {len(all_images)}")
    print("-" * 70)
    print()
    
    # Generate images with progress tracking
    success_count = 0
    fail_count = 0
    
    for i, (prompt, filename, width, height) in enumerate(all_images, 1):
        print(f"[{i}/{len(all_images)}] ", end="")
        if generate_image(prompt, filename, width, height):
            success_count += 1
        else:
            fail_count += 1
        
        # Small delay to avoid rate limiting
        sleep(0.5)
    
    print()
    print("=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print(f"✅ Successful: {success_count}")
    print(f"❌ Failed: {fail_count}")
    print(f"📁 Output: {OUTPUT_DIR.absolute()}")
    print()


def generate_single_category(category):
    """Generate images for a specific category"""
    
    if not TOGETHER_API_KEY:
        print("❌ No API key found. Set TOGETHER_API_KEY environment variable.")
        return
    
    categories = {
        "hero": [(img["prompt"], img["filename"], img.get("width", IMAGE_WIDTH), img.get("height", IMAGE_HEIGHT)) for img in HERO_IMAGES],
        "bikes": [(img["prompt"], img["filename"], IMAGE_WIDTH, IMAGE_HEIGHT) for img in BIKE_IMAGES],
        "avatars": [(img["prompt"], img["filename"], img.get("width", 1024), img.get("height", 1024)) for img in AVATAR_IMAGES],
        "instagram": [(img["prompt"], img["filename"], img.get("width", 1024), img.get("height", 1024)) for img in INSTAGRAM_IMAGES],
        "extra": [(img["prompt"], img["filename"], img.get("width", IMAGE_WIDTH), img.get("height", IMAGE_HEIGHT)) for img in ADDITIONAL_IMAGES],
    }
    
    if category not in categories:
        print(f"❌ Unknown category: {category}")
        print(f"Available: {', '.join(categories.keys())}")
        return
    
    images = categories[category]
    print(f"Generating {len(images)} {category} images...")
    print()
    
    for prompt, filename, width, height in images:
        generate_image(prompt, filename, width, height)
        sleep(0.5)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Generate specific category
        category = sys.argv[1].lower()
        generate_single_category(category)
    else:
        # Generate all images
        generate_all_images()
