"""
Disease metadata with plain-language remedies and descriptions.
All advice is written so that any farmer or student can understand
it — no chemical jargon, just clear step-by-step actions.
"""

DISEASE_META = {

    # ── Apple ──────────────────────────────────────────────────────────────────
    'Apple___Apple_scab': {
        'plant': 'Apple', 'disease': 'Apple Scab', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Pick up and throw away any fallen leaves around the plant — do not leave them on the ground.\n'
            '2. Buy an anti-fungal spray for apple trees at your local agri-store and spray the leaves.\n'
            '3. Spray every 10 days, especially during rainy weather.\n'
            '4. Always water at the roots — never spray water on the leaves.'
        ),
        'description': (
            'A fungal disease that makes dark, rough patches (like scabs) on leaves and fruit. '
            'Spreads through rain and wind. Can ruin the fruit if not treated.'
        ),
    },

    'Apple___Black_rot': {
        'plant': 'Apple', 'disease': 'Black Rot', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Cut off and remove all rotten or brown-looking branches and leaves. Burn them or throw them far away.\n'
            '2. Spray the whole plant with an anti-fungal spray from your agri-store.\n'
            '3. Make sure no water is sitting near the roots.\n'
            '4. Clean your cutting tools with soap water after use so disease does not spread.'
        ),
        'description': (
            'A fungal disease causing brown and black rotting spots on fruit and leaves. '
            'Spreads fast in warm, wet weather and can destroy the whole harvest if ignored.'
        ),
    },

    'Apple___Cedar_apple_rust': {
        'plant': 'Apple', 'disease': 'Cedar Apple Rust', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Spray an anti-fungal spray on the plant as soon as you see orange spots on leaves.\n'
            '2. If there are cedar or juniper trees nearby, try to remove them — they spread this disease.\n'
            '3. Spray every 7–10 days during spring and rainy weather.\n'
            '4. Remove affected leaves carefully and put them in a bag before throwing away.'
        ),
        'description': (
            'A fungal disease that creates bright orange-yellow spots on apple leaves. '
            'It needs both an apple tree and a nearby cedar/juniper tree to spread.'
        ),
    },

    'Apple___healthy': {
        'plant': 'Apple', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': (
            'Your plant is healthy! 🎉 '
            'Keep watering at the roots (not on leaves). Remove fallen leaves regularly. '
            'Check for new spots every week.'
        ),
        'description': 'The apple plant looks healthy with no signs of disease.',
    },

    # ── Blueberry ──────────────────────────────────────────────────────────────
    'Blueberry___healthy': {
        'plant': 'Blueberry', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Continue regular watering and remove any dead leaves.',
        'description': 'The blueberry plant looks healthy with no signs of disease.',
    },

    # ── Cherry ─────────────────────────────────────────────────────────────────
    'Cherry_(including_sour)___Powdery_mildew': {
        'plant': 'Cherry', 'disease': 'Powdery Mildew', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Home remedy: Mix 1 tablespoon of baking soda + a few drops of dish soap in 1 litre of water. Spray on leaves.\n'
            '2. Or buy a sulfur-based plant spray from your agri-store — it is cheap and works well.\n'
            '3. Give the plant more space — do not let other plants crowd it.\n'
            '4. Water only the soil, never the leaves.'
        ),
        'description': (
            'A fungal disease that makes leaves look covered in white powder or dust. '
            'Appears in warm, dry weather and spreads quickly to young leaves.'
        ),
    },

    'Cherry_(including_sour)___healthy': {
        'plant': 'Cherry', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Continue regular watering and check leaves weekly.',
        'description': 'The cherry plant looks healthy with no signs of disease.',
    },

    # ── Corn ───────────────────────────────────────────────────────────────────
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'plant': 'Corn', 'disease': 'Gray Leaf Spot', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Remove affected lower leaves as soon as you see grey rectangular patches.\n'
            '2. Spray an anti-fungal spray (ask your agri-store for one safe for maize/corn).\n'
            '3. Next season, plant a disease-resistant corn variety — ask your seed supplier.\n'
            '4. Do not plant corn in the same field every year — rotate with another crop.'
        ),
        'description': (
            'A fungal disease creating rectangular grey-brown patches on corn leaves. '
            'Wet and foggy weather helps it spread fast. Can cut harvest by up to 50%.'
        ),
    },

    'Corn_(maize)___Common_rust_': {
        'plant': 'Corn', 'disease': 'Common Rust', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Start spraying an anti-fungal spray as early as possible — do not wait for it to spread.\n'
            '2. Ask your agri-store for a spray that prevents rust disease on corn.\n'
            '3. Remove heavily infected plants to stop spread to healthy ones.\n'
            '4. Next season, buy a rust-resistant corn variety from your seed shop.'
        ),
        'description': (
            'A fungal disease causing raised, rusty-brown bumps on corn leaves. '
            'Spreads through wind and is common in cool, humid weather.'
        ),
    },

    'Corn_(maize)___Northern_Leaf_Blight': {
        'plant': 'Corn', 'disease': 'Northern Leaf Blight', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Spray plants with an anti-fungal spray as soon as you see the long grey patches.\n'
            '2. Remove and burn the worst-affected plants so disease stops spreading.\n'
            '3. Next season, use a disease-resistant corn seed variety.\n'
            '4. Do not plant corn in the same field two years in a row — switch to another crop.'
        ),
        'description': (
            'A fungal disease causing long, grey cigar-shaped patches on corn leaves. '
            'Spreads fast in cool, wet weather and reduces grain production badly.'
        ),
    },

    'Corn_(maize)___healthy': {
        'plant': 'Corn', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Continue normal watering and check for spots weekly.',
        'description': 'The corn plant looks healthy with no signs of disease.',
    },

    # ── Grape ──────────────────────────────────────────────────────────────────
    'Grape___Black_rot': {
        'plant': 'Grape', 'disease': 'Black Rot', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Remove all shrivelled, black rotten berries and infected leaves. Bag and throw away.\n'
            '2. Buy an anti-fungal spray from your agri-store and spray the whole plant before and after flowering.\n'
            '3. Prune branches so air can flow freely through the vine.\n'
            '4. Spray every 10 days during rainy or humid weather.'
        ),
        'description': (
            'A fungal disease causing brown spots on leaves and turning berries into hard black stones. '
            'Very destructive — spreads through rain. Act quickly to save the harvest.'
        ),
    },

    'Grape___Esca_(Black_Measles)': {
        'plant': 'Grape', 'disease': 'Esca (Black Measles)', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Cut off all branches that look dried out, striped, or dead.\n'
            '2. Apply a plant wound sealant paste on the cut area — ask your agri-store for it.\n'
            '3. There is no complete cure. Managing it early helps the plant survive longer.\n'
            '4. Ask your local agriculture officer for help.'
        ),
        'description': (
            'A complex fungal disease inside the vine wood. Creates tiger-stripe patterns on leaves '
            'and can suddenly kill branches. Older vines are more at risk.'
        ),
    },

    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'plant': 'Grape', 'disease': 'Leaf Blight', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Pick off all leaves with dark brown spots and throw them away — do not leave on the ground.\n'
            '2. Spray the plant with a copper-based spray (ask for "Bordeaux mixture" or "copper spray" at agri-store).\n'
            '3. Spray once a week during wet and humid weather.\n'
            '4. Make sure the plant gets good sunlight and is not overcrowded.'
        ),
        'description': (
            'A fungal disease causing dark brown irregular spots on grape leaves. '
            'Appears in warm, humid conditions and can cause early leaf fall.'
        ),
    },

    'Grape___healthy': {
        'plant': 'Grape', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Keep pruning regularly and check for spots after rain.',
        'description': 'The grape plant looks healthy with no signs of disease.',
    },

    # ── Orange ─────────────────────────────────────────────────────────────────
    'Orange___Haunglongbing_(Citrus_greening)': {
        'plant': 'Orange', 'disease': 'Citrus Greening (HLB)', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. There is NO cure. Infected trees must be cut down completely to stop it spreading.\n'
            '2. The disease is spread by a tiny insect called the "citrus psyllid". Spray all nearby trees with an insect-killing spray.\n'
            '3. Buy new, healthy saplings only from a certified nursery.\n'
            '4. Immediately inform your local agriculture department — this can destroy entire orchards.'
        ),
        'description': (
            'A very serious bacterial disease spread by a small jumping insect. '
            'Causes yellowing of leaves, misshapen bitter fruit, and eventually kills the tree. No cure exists.'
        ),
    },

    # ── Peach ──────────────────────────────────────────────────────────────────
    'Peach___Bacterial_spot': {
        'plant': 'Peach', 'disease': 'Bacterial Spot', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Spray the plant with a copper-based spray (ask your agri-store for "copper spray").\n'
            '2. Never water from above — always water at the base/roots only.\n'
            '3. Remove and throw away infected leaves.\n'
            '4. Spray every 7–10 days, especially if rain is expected.'
        ),
        'description': (
            'A bacterial disease causing small dark, water-soaked spots on leaves and fruit. '
            'Spreads easily through rain, wind, and wet conditions.'
        ),
    },

    'Peach___healthy': {
        'plant': 'Peach', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Continue watering at the roots and check leaves weekly.',
        'description': 'The peach plant looks healthy with no signs of disease.',
    },

    # ── Pepper ─────────────────────────────────────────────────────────────────
    'Pepper,_bell___Bacterial_spot': {
        'plant': 'Pepper', 'disease': 'Bacterial Spot', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Spray the plant with a copper-based spray (ask your agri-store for "copper bactericide").\n'
            '2. Pour water directly on the soil — never spray it on the leaves.\n'
            '3. Remove spotted leaves and throw them in the trash — not on the ground.\n'
            '4. Wash your hands after touching infected plants so you don\'t spread it to other plants.'
        ),
        'description': (
            'A bacterial disease causing small dark raised spots on pepper leaves. '
            'Wet conditions and water splashing spread it from plant to plant.'
        ),
    },

    'Pepper,_bell___healthy': {
        'plant': 'Pepper', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Water at the base and keep the area around the plant clean.',
        'description': 'The pepper plant looks healthy with no signs of disease.',
    },

    # ── Potato ─────────────────────────────────────────────────────────────────
    'Potato___Early_blight': {
        'plant': 'Potato', 'disease': 'Early Blight', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Remove infected lower leaves carefully and throw them away — do not compost them.\n'
            '2. Buy an anti-fungal spray from your agri-store (ask for one safe for potatoes) and spray.\n'
            '3. Water only at the roots — never on the leaves.\n'
            '4. Leave enough space between plants so air can flow freely.'
        ),
        'description': (
            'A fungal disease starting on older, lower leaves as dark brown spots with ring patterns (like a target). '
            'Weakens the plant and reduces potato yield if not controlled.'
        ),
    },

    'Potato___Late_blight': {
        'plant': 'Potato', 'disease': 'Late Blight', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Act immediately — this disease can destroy an entire field in just a few days.\n'
            '2. Remove and burn all infected plants right away. Do NOT compost them.\n'
            '3. Spray all remaining plants with an anti-fungal spray immediately.\n'
            '4. Do not water during rainy or cloudy days.\n'
            '5. After harvest, clear all plant remains from the field before the next planting season.'
        ),
        'description': (
            'A very dangerous disease that caused the famous Irish Potato Famine. '
            'Creates dark, water-soaked brown patches on leaves and stems. Spreads extremely fast in cool, wet weather. Immediate action is essential.'
        ),
    },

    'Potato___healthy': {
        'plant': 'Potato', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Keep watering at the base and monitor leaves after rainfall.',
        'description': 'The potato plant looks healthy with no signs of disease.',
    },

    # ── Raspberry ──────────────────────────────────────────────────────────────
    'Raspberry___healthy': {
        'plant': 'Raspberry', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Regular pruning and watering at the base will keep it strong.',
        'description': 'The raspberry plant looks healthy with no signs of disease.',
    },

    # ── Soybean ────────────────────────────────────────────────────────────────
    'Soybean___healthy': {
        'plant': 'Soybean', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Continue normal care and check leaves regularly.',
        'description': 'The soybean plant looks healthy with no signs of disease.',
    },

    # ── Squash ─────────────────────────────────────────────────────────────────
    'Squash___Powdery_mildew': {
        'plant': 'Squash', 'disease': 'Powdery Mildew', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Home remedy: Mix 1 tablespoon of baking soda + a few drops of dish soap in 1 litre of water and spray on leaves.\n'
            '2. Or spray neem oil (available at garden or agri-shops) on the leaves — natural and safe.\n'
            '3. Give the plant more space and air — trim nearby branches if they are crowding it.\n'
            '4. Water only at soil level — never on the leaves.'
        ),
        'description': (
            'A fungal disease making leaves look like they have been dusted with white powder. '
            'Starts on older leaves and spreads in dry weather with cool nights.'
        ),
    },

    # ── Strawberry ─────────────────────────────────────────────────────────────
    'Strawberry___Leaf_scorch': {
        'plant': 'Strawberry', 'disease': 'Leaf Scorch', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Remove all leaves with dark purple-brown spots and throw them in the trash.\n'
            '2. Buy an anti-fungal spray from your agri-store and spray the remaining healthy leaves.\n'
            '3. Water only at the roots — never on the leaves.\n'
            '4. Ensure plants are not overcrowded — give each plant space to breathe.\n'
            '5. After the fruiting season, clean up all fallen leaves from the ground.'
        ),
        'description': (
            'A fungal disease causing small, dark purple spots on the upper surface of strawberry leaves. '
            'Edges of leaves can turn brown and look "burned". Spreads through water splashing on leaves.'
        ),
    },

    'Strawberry___healthy': {
        'plant': 'Strawberry', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': 'Your plant is healthy! 🎉 Water at the soil level and clear dead leaves from around the plant.',
        'description': 'The strawberry plant looks healthy with no signs of disease.',
    },

    # ── Tomato ─────────────────────────────────────────────────────────────────
    'Tomato___Bacterial_spot': {
        'plant': 'Tomato', 'disease': 'Bacterial Spot', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Spray the plant with a copper-based spray — ask for "copper spray" at any agri-store.\n'
            '2. Do not touch or work with plants when leaves are wet — you can accidentally spread the bacteria.\n'
            '3. Remove infected leaves and throw them away in a sealed bag.\n'
            '4. Water only at the base of the plant, not on the leaves.'
        ),
        'description': (
            'A bacterial disease causing small dark round spots on tomato leaves and fruit. '
            'Spreads fast when rain or water splashes on leaves.'
        ),
    },

    'Tomato___Early_blight': {
        'plant': 'Tomato', 'disease': 'Early Blight', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Start from the bottom — remove all lower leaves with dark spots and ring patterns.\n'
            '2. Spray the plant with a copper-based anti-fungal spray (ask your agri-store).\n'
            '3. Water only at the soil level — never spray water on the leaves.\n'
            '4. Spray once every week during humid and rainy weather.'
        ),
        'description': (
            'A common fungal disease starting on older, lower tomato leaves as dark brown spots with a bullseye ring pattern. '
            'Slowly moves upward and can reduce fruit production if not treated.'
        ),
    },

    'Tomato___Late_blight': {
        'plant': 'Tomato', 'disease': 'Late Blight', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. EMERGENCY — act today, not tomorrow.\n'
            '2. Pull out and destroy all severely infected plants. Burn them or seal in garbage bags — do NOT compost.\n'
            '3. Spray the remaining plants with an anti-fungal spray immediately (ask agri-store for "late blight spray for tomatoes").\n'
            '4. Stop watering from above — water only at the roots.\n'
            '5. Spray every 5–7 days during cool, rainy weather.'
        ),
        'description': (
            'A very dangerous disease that can destroy an entire tomato farm in just a few days. '
            'Creates large dark water-soaked brown patches on leaves and attacks fruit and stems. Thrives in cool, wet, cloudy weather.'
        ),
    },

    'Tomato___Leaf_Mold': {
        'plant': 'Tomato', 'disease': 'Leaf Mold', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Open up greenhouse covers or remove shade-nets to let more fresh air in — this disease loves humidity.\n'
            '2. Remove all leaves showing yellow patches on top or grey-green mold underneath.\n'
            '3. Spray an anti-fungal spray on all remaining leaves.\n'
            '4. Water only in the morning so leaves dry out during the day.'
        ),
        'description': (
            'A fungal disease causing yellow patches on the top of tomato leaves and grey-green fuzzy mold underneath. '
            'Most common in greenhouses or enclosed areas with poor airflow and high humidity.'
        ),
    },

    'Tomato___Septoria_leaf_spot': {
        'plant': 'Tomato', 'disease': 'Septoria Leaf Spot', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Remove all infected leaves immediately — start from the bottom and work upward.\n'
            '2. Throw infected leaves in a sealed bag — do not leave on the ground.\n'
            '3. Spray an anti-fungal spray on the whole plant.\n'
            '4. Avoid wetting leaves when watering. Spray every 7–10 days in humid or rainy weather.'
        ),
        'description': (
            'A fungal disease causing many small circular spots with dark edges and a pale center on tomato leaves. '
            'Starts on lower leaves and moves upward. Infected leaves turn yellow and fall off.'
        ),
    },

    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'plant': 'Tomato', 'disease': 'Spider Mites', 'severity': 'Low', 'healthy': False,
        'remedy': (
            '1. Spider mites are tiny bugs — check the underside of leaves for small dots or fine webbing.\n'
            '2. Spray neem oil (a natural plant oil from agri-stores) on the underside of all leaves — safe and effective.\n'
            '3. Or spray the plant with a strong jet of plain water to knock the mites off.\n'
            '4. Repeat every 5–7 days until no more mites are seen.\n'
            '5. Avoid over-fertilising — it can actually make spider mite problems worse.'
        ),
        'description': (
            'A pest attack by tiny spider-like insects living on the underside of tomato leaves. '
            'They cause tiny yellow dots and fine white webbing. Thrive in hot, dry weather.'
        ),
    },

    'Tomato___Target_Spot': {
        'plant': 'Tomato', 'disease': 'Target Spot', 'severity': 'Medium', 'healthy': False,
        'remedy': (
            '1. Remove all leaves showing brown rings (like a bullseye/target pattern) and dispose of them.\n'
            '2. Spray an anti-fungal plant spray on the whole plant.\n'
            '3. Give plants more space — trim nearby leaves so air can flow through.\n'
            '4. Always water at the base. Spray every 7–10 days in humid weather.'
        ),
        'description': (
            'A fungal disease creating round brown spots with ring patterns (like a bullseye) on tomato leaves. '
            'Can spread to fruit too. High humidity and crowded planting encourage it.'
        ),
    },

    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'plant': 'Tomato', 'disease': 'Yellow Leaf Curl Virus', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. This disease is spread by small white flying insects called "whiteflies".\n'
            '2. Buy a whitefly insect-killing spray from your agri-store and spray all plants, especially under the leaves.\n'
            '3. Remove and destroy all plants that are severely curled and yellow — they cannot recover.\n'
            '4. Use yellow sticky traps near your plants to catch whiteflies (available at agri-stores).\n'
            '5. Next season, buy virus-resistant tomato seeds.'
        ),
        'description': (
            'A viral disease spread by tiny white insects (whiteflies). Infected plants have curled, '
            'yellowed leaves and stunted growth. Fruit production drops badly. No cure — prevention is key.'
        ),
    },

    'Tomato___Tomato_mosaic_virus': {
        'plant': 'Tomato', 'disease': 'Mosaic Virus', 'severity': 'High', 'healthy': False,
        'remedy': (
            '1. Remove and destroy all infected plants immediately — they cannot be cured.\n'
            '2. Wash your hands thoroughly with soap after touching infected plants.\n'
            '3. Clean all farming tools (knives, scissors) with bleach water before using on healthy plants — the virus spreads through dirty tools.\n'
            '4. Kill aphids (small green/black bugs) with an insect spray — they carry and spread this virus.\n'
            '5. Next season, buy mosaic-virus-resistant tomato seed varieties.'
        ),
        'description': (
            'A viral disease creating a mosaic pattern of light and dark patches on tomato leaves. '
            'Spreads through touch, dirty tools, and insects like aphids. No chemical cure — infected plants must be removed.'
        ),
    },

    'Tomato___healthy': {
        'plant': 'Tomato', 'disease': 'Healthy', 'severity': 'Healthy', 'healthy': True,
        'remedy': (
            'Your plant is healthy! 🎉 '
            'Keep watering at the base. Remove any yellowing or dead leaves regularly. '
            'Check the underside of leaves for insects every week.'
        ),
        'description': 'The tomato plant looks healthy with no signs of disease.',
    },
}
