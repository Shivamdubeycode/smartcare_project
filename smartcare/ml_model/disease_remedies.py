
"""
Comprehensive Disease Remedies Database
Contains detailed treatment and prevention strategies for 38+ plant diseases
With FLEXIBLE KEY MATCHING to handle any format
"""

import re


# Main remedy database - using flexible keys
DISEASE_REMEDIES = {
    # APPLE DISEASES
    "apple apple scab": {
        "description": "Fungal disease causing dark, scabby lesions on leaves and fruit.",
        "symptoms": [
            "Olive-green to dark brown spots on leaves",
            "Scabby lesions on fruit",
            "Premature leaf drop",
            "Distorted or cracked fruit"
        ],
        "treatment": [
            "Remove and destroy infected leaves and fruit",
            "Apply fungicides (captan, myclobutanil) at bud break",
            "Prune trees to improve air circulation",
            "Apply lime sulfur during dormant season"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Maintain proper tree spacing",
            "Remove fallen leaves in autumn",
            "Avoid overhead watering"
        ],
        "organic_solutions": [
            "Neem oil spray every 7-14 days",
            "Baking soda solution (1 tbsp per gallon water)",
            "Sulfur-based fungicides",
            "Compost tea foliar spray"
        ]
    },
    
    "apple black rot": {
        "description": "Fungal disease causing fruit rot and leaf spots.",
        "symptoms": [
            "Purple spots on leaves with light centers",
            "Black, circular lesions on fruit",
            "Fruit mummification",
            "Cankers on branches"
        ],
        "treatment": [
            "Remove mummified fruit and infected branches",
            "Apply fungicides during bloom and fruit development",
            "Prune out cankers during dry weather",
            "Destroy all infected plant material"
        ],
        "prevention": [
            "Maintain tree vigor with proper fertilization",
            "Prune for good air circulation",
            "Remove all fruit mummies before spring",
            "Avoid wounding trees"
        ],
        "organic_solutions": [
            "Copper-based fungicides",
            "Bordeaux mixture",
            "Remove infected tissue immediately",
            "Maintain orchard sanitation"
        ]
    },
    
    "apple cedar apple rust": {
        "description": "Fungal disease requiring both apple and cedar trees to complete lifecycle.",
        "symptoms": [
            "Bright orange-yellow spots on upper leaf surface",
            "Small spots on fruit",
            "Premature leaf drop",
            "Reduced fruit quality"
        ],
        "treatment": [
            "Apply fungicides from pink bud through summer",
            "Remove nearby cedar trees if possible",
            "Rake and destroy fallen leaves",
            "Use myclobutanil or propiconazole fungicides"
        ],
        "prevention": [
            "Plant resistant apple varieties",
            "Maintain distance from cedar trees (500+ ft)",
            "Regular fungicide applications in spring",
            "Monitor weather for infection periods"
        ],
        "organic_solutions": [
            "Sulfur sprays starting at bud break",
            "Neem oil applications",
            "Improve tree nutrition",
            "Remove cedar trees within 1 mile radius if possible"
        ]
    },
    
    # TOMATO DISEASES
    "tomato bacterial spot": {
        "description": "Bacterial disease causing dark spots on leaves and fruit.",
        "symptoms": [
            "Small, dark, greasy-looking spots on leaves",
            "Raised spots on fruit with white halos",
            "Leaf yellowing and drop",
            "Reduced fruit quality and yield"
        ],
        "treatment": [
            "Remove infected plants immediately",
            "Apply copper-based bactericides",
            "Use biological controls (Bacillus subtilis)",
            "Avoid working in wet plants"
        ],
        "prevention": [
            "Use disease-free seed and transplants",
            "Crop rotation (3-4 years)",
            "Avoid overhead watering",
            "Disinfect tools between plants"
        ],
        "organic_solutions": [
            "Copper spray (fixed copper)",
            "Bacillus subtilis biological spray",
            "Compost tea applications",
            "Maintain plant spacing for air flow"
        ]
    },
    
    "tomato early blight": {
        "description": "Fungal disease causing target-spot lesions on lower leaves.",
        "symptoms": [
            "Dark brown spots with concentric rings (target pattern)",
            "Yellowing around lesions",
            "Lower leaves affected first",
            "Fruit spots near stem end"
        ],
        "treatment": [
            "Apply fungicides at first sign of disease",
            "Use chlorothalonil, mancozeb, or copper fungicides",
            "Remove infected lower leaves immediately",
            "Mulch around plants to prevent soil splash"
        ],
        "prevention": [
            "Practice 3-year crop rotation",
            "Stake and prune plants for air circulation",
            "Apply mulch around plants",
            "Water at base of plants, not overhead"
        ],
        "organic_solutions": [
            "Copper fungicides (organic approved)",
            "Neem oil spray every 7-14 days",
            "Baking soda spray (1 tsp per quart water with dish soap)",
            "Remove affected leaves immediately and destroy"
        ]
    },
    
    "tomato late blight": {
        "description": "Devastating fungal disease that can destroy entire crops quickly.",
        "symptoms": [
            "Water-soaked lesions on leaves",
            "White mold growth on undersides of leaves",
            "Brown lesions on stems",
            "Firm, brown rot on fruit"
        ],
        "treatment": [
            "Remove and destroy infected plants IMMEDIATELY",
            "Apply fungicides preventively (chlorothalonil, mancozeb)",
            "Do NOT compost infected material - burn or bag it",
            "Act quickly as disease spreads rapidly in hours"
        ],
        "prevention": [
            "Plant resistant varieties when possible",
            "Ensure excellent air circulation between plants",
            "Avoid overhead watering completely",
            "Monitor weather for blight-favorable conditions (cool, wet)"
        ],
        "organic_solutions": [
            "Copper fungicides (preventive only, not curative)",
            "Remove infected plants at first sign",
            "Improve air flow dramatically",
            "Use only certified disease-free seed potatoes/transplants"
        ]
    },
    
    "tomato leaf mold": {
        "description": "Fungal disease common in humid greenhouse conditions.",
        "symptoms": [
            "Pale green to yellow spots on upper leaf surface",
            "Olive-green to brown mold on lower leaf surface",
            "Leaves curl and die",
            "Thrives in high humidity above 85%"
        ],
        "treatment": [
            "Improve ventilation immediately",
            "Apply fungicides (chlorothalonil, copper)",
            "Remove heavily infected leaves",
            "Reduce humidity below 85%"
        ],
        "prevention": [
            "Maintain humidity below 85%",
            "Ensure excellent ventilation",
            "Space plants adequately (2-3 feet apart)",
            "Plant resistant varieties"
        ],
        "organic_solutions": [
            "Improve air circulation with fans",
            "Reduce humidity through ventilation",
            "Neem oil sprays",
            "Baking soda solution spray"
        ]
    },
    
    "tomato septoria leaf spot": {
        "description": "Fungal disease causing numerous small spots on leaves.",
        "symptoms": [
            "Small, circular spots with dark borders",
            "Gray to tan centers with black specks (fungal fruiting bodies)",
            "Lower leaves affected first",
            "Premature leaf drop and defoliation"
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, mancozeb)",
            "Remove infected lower leaves",
            "Mulch heavily to prevent splash-up from soil",
            "Avoid overhead watering"
        ],
        "prevention": [
            "Practice 3-year crop rotation",
            "Stake plants for better air flow",
            "Apply thick organic mulch around plants",
            "Remove all plant debris at season end"
        ],
        "organic_solutions": [
            "Copper fungicides",
            "Neem oil applications weekly",
            "Remove affected foliage promptly",
            "Maintain excellent plant hygiene"
        ]
    },
    
    "tomato spider mites": {
        "description": "Tiny arachnids that suck plant sap, causing stippling and webbing.",
        "symptoms": [
            "Yellow stippling (tiny dots) on leaves",
            "Fine webbing visible on undersides of leaves",
            "Bronzed or silvered appearance of leaves",
            "Plant stress and reduced yield"
        ],
        "treatment": [
            "Spray with insecticidal soap thoroughly",
            "Use horticultural oil spray",
            "Apply miticides if infestation is severe",
            "Increase humidity around plants"
        ],
        "prevention": [
            "Regular monitoring of leaf undersides",
            "Avoid water stress (mites love dry conditions)",
            "Encourage beneficial insects (ladybugs, lacewings)",
            "Avoid dusty conditions"
        ],
        "organic_solutions": [
            "Neem oil spray on all leaf surfaces",
            "Insecticidal soap spray",
            "Strong water spray to dislodge mites",
            "Release predatory mites (Phytoseiulus persimilis)"
        ]
    },
    
    "tomato target spot": {
        "description": "Fungal disease causing concentric ring lesions.",
        "symptoms": [
            "Brown lesions with concentric rings",
            "Spots on leaves, stems, and fruit",
            "Yellow halo around spots",
            "Premature defoliation"
        ],
        "treatment": [
            "Apply fungicides (azoxystrobin, chlorothalonil)",
            "Remove infected plant parts",
            "Improve air circulation",
            "Mulch to prevent splash from soil"
        ],
        "prevention": [
            "Crop rotation with non-solanaceous crops",
            "Proper plant spacing (2-3 feet)",
            "Avoid overhead irrigation",
            "Remove all plant debris after harvest"
        ],
        "organic_solutions": [
            "Copper-based fungicides",
            "Neem oil spray",
            "Maintain overall plant health",
            "Practice good sanitation"
        ]
    },
    
    "tomato yellow leaf curl virus": {
        "description": "Viral disease transmitted by whiteflies causing severe leaf curling.",
        "symptoms": [
            "Severe upward leaf curling",
            "Yellowing of leaf margins",
            "Stunted plant growth",
            "Dramatically reduced or no fruit set"
        ],
        "treatment": [
            "Remove infected plants immediately and destroy",
            "Control whitefly vectors aggressively",
            "NO CURE available once plants are infected",
            "Use reflective mulches to deter whiteflies"
        ],
        "prevention": [
            "Use resistant varieties (HR varieties)",
            "Control whiteflies with insecticides or oils",
            "Use insect-proof netting (50-mesh) in greenhouses",
            "Remove infected plants promptly to prevent spread"
        ],
        "organic_solutions": [
            "Yellow sticky traps for whitefly monitoring and control",
            "Neem oil for whitefly control",
            "Remove and destroy infected plants immediately",
            "Plant marigolds as companion plants (repel whiteflies)"
        ]
    },
    
    "tomato mosaic virus": {
        "description": "Viral disease causing mottled leaves and reduced yield.",
        "symptoms": [
            "Mottled light and dark green patterns on leaves",
            "Leaf distortion and curling",
            "Stunted plant growth",
            "Reduced fruit quality and yield"
        ],
        "treatment": [
            "Remove infected plants immediately",
            "Disinfect all tools with 10% bleach solution",
            "No chemical treatment available for viruses",
            "Prevent spread to healthy plants"
        ],
        "prevention": [
            "Use resistant varieties",
            "Disinfect tools regularly between plants",
            "Wash hands thoroughly before handling plants",
            "Don't smoke near plants (tobacco mosaic virus relation)"
        ],
        "organic_solutions": [
            "Remove infected plants at first sign",
            "Sanitize all tools between uses",
            "Control aphid vectors with organic sprays",
            "Use only certified virus-free seed"
        ]
    },
    
    # POTATO DISEASES
    "potato early blight": {
        "description": "Fungal disease causing target-spot lesions on potato leaves.",
        "symptoms": [
            "Dark brown spots with concentric rings (target pattern)",
            "Lower leaves affected first",
            "Yellowing around lesions",
            "Can affect tubers with dark, sunken spots"
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, mancozeb) at first sign",
            "Remove infected foliage promptly",
            "Improve air circulation around plants",
            "Ensure adequate potassium fertilization"
        ],
        "prevention": [
            "Practice 3-4 year crop rotation",
            "Use certified disease-free seed potatoes",
            "Avoid overhead irrigation",
            "Hill soil around plants properly"
        ],
        "organic_solutions": [
            "Copper fungicides",
            "Maintain optimal plant vigor with compost",
            "Proper plant spacing (12-15 inches)",
            "Remove infected plant material immediately"
        ]
    },
    
    "potato late blight": {
        "description": "Devastating disease that caused the Irish Potato Famine.",
        "symptoms": [
            "Water-soaked lesions on leaves appearing quickly",
            "White fuzzy growth on undersides of leaves",
            "Rapid plant collapse (can occur in 2-3 days)",
            "Brown, firm rot on tubers"
        ],
        "treatment": [
            "Apply fungicides IMMEDIATELY (chlorothalonil, mancozeb)",
            "Remove infected plants and destroy (do not compost)",
            "Harvest tubers before disease reaches them if possible",
            "Destroy all infected material by burning or deep burial"
        ],
        "prevention": [
            "Plant resistant varieties (check local recommendations)",
            "Use only certified disease-free seed potatoes",
            "Ensure excellent drainage",
            "Monitor weather for blight-favorable conditions (cool, wet)"
        ],
        "organic_solutions": [
            "Copper fungicides (preventive applications only)",
            "Remove infected plants at first sign",
            "Improve air circulation dramatically",
            "Avoid overhead watering completely"
        ]
    },
    
    # CORN DISEASES
    "corn cercospora leaf spot": {
        "description": "Fungal disease causing distinctive gray lesions on corn leaves.",
        "symptoms": [
            "Rectangular gray or tan lesions between leaf veins",
            "Lesions may have yellow halos",
            "Severe cases cause extensive leaf blighting",
            "Reduced photosynthesis and yield loss"
        ],
        "treatment": [
            "Apply fungicides at first sign of disease",
            "Use strobilurins or triazole fungicides",
            "Rotate crops annually with non-host crops",
            "Till under crop residue after harvest"
        ],
        "prevention": [
            "Plant resistant hybrids",
            "Rotate with non-host crops (3-4 year rotation with soybeans)",
            "Bury crop residue through tillage",
            "Avoid excessive nitrogen fertilization"
        ],
        "organic_solutions": [
            "Crop rotation with legumes",
            "Maintain excellent field sanitation",
            "Use disease-resistant varieties",
            "Proper plant spacing for air flow (8-10 inches)"
        ]
    },
    
    "corn common rust": {
        "description": "Fungal disease producing rust-colored pustules on corn leaves.",
        "symptoms": [
            "Small, circular to elongate pustules on leaves",
            "Rust-colored (cinnamon-brown) spore pustules",
            "Pustules present on both upper and lower leaf surfaces",
            "Severe infections can reduce yields significantly"
        ],
        "treatment": [
            "Apply fungicides if disease is severe before tasseling",
            "Use triazole or strobilurin fungicides",
            "Monitor disease progression carefully",
            "Consider fungicide application if infection before tasseling"
        ],
        "prevention": [
            "Plant resistant hybrids (check resistance ratings)",
            "Plant early to avoid peak disease pressure",
            "Maintain balanced fertilization",
            "Scout fields regularly for early detection"
        ],
        "organic_solutions": [
            "Remove heavily infected plants if practical",
            "Sulfur dust applications",
            "Neem oil spray (limited effectiveness)",
            "Maintain plant health through composting and proper nutrition"
        ]
    },
    
    "corn northern leaf blight": {
        "description": "Fungal disease causing long, cigar-shaped lesions on corn leaves.",
        "symptoms": [
            "Elliptical, grayish-green to tan lesions 1-6 inches long",
            "Lesions are cigar-shaped",
            "Lesions may merge causing extensive leaf death",
            "Can cause severe yield loss in susceptible hybrids"
        ],
        "treatment": [
            "Apply fungicides at first sign during V8-VT growth stage",
            "Use QoI (strobilurin) or triazole fungicides",
            "Multiple applications may be needed in severe cases",
            "Focus applications on upper canopy leaves"
        ],
        "prevention": [
            "Plant resistant hybrids (very important)",
            "Practice two-year crop rotation minimum",
            "Bury crop residue through tillage",
            "Maintain balanced fertilization (avoid excess nitrogen)"
        ],
        "organic_solutions": [
            "Crop rotation with soybeans or other non-hosts",
            "Thorough tillage to bury residue",
            "Use resistant varieties (most important)",
            "Maintain adequate plant spacing"
        ]
    },
    
    # GRAPE DISEASES
    "grape black rot": {
        "description": "Serious fungal disease of grapes causing complete fruit mummification.",
        "symptoms": [
            "Tan leaf spots with dark borders",
            "Black, shriveled fruit (mummies) that persist on vines",
            "Fruit lesions start as light brown spots",
            "Complete fruit rot in severe cases leads to total crop loss"
        ],
        "treatment": [
            "Apply fungicides from bud break to 6 weeks after bloom",
            "Use mancozeb, myclobutanil, or captan fungicides",
            "Remove all mummified fruit from vines and ground",
            "Prune out infected canes during winter dormancy"
        ],
        "prevention": [
            "Practice excellent sanitation (remove all mummies annually)",
            "Prune vines for good air circulation and sunlight penetration",
            "Begin preventive fungicide applications at bud swell",
            "Continue fungicide program through vulnerable period"
        ],
        "organic_solutions": [
            "Copper-based fungicides (Bordeaux mixture)",
            "Bordeaux mixture applications",
            "Sulfur sprays during growing season",
            "Remove all mummified fruit annually (critical)"
        ]
    },
    
    # PEPPER DISEASES  
    "pepper bacterial spot": {
        "description": "Bacterial disease causing leaf and fruit spots on peppers.",
        "symptoms": [
            "Dark, greasy spots on leaves",
            "Raised spots on fruit",
            "Yellow halos around lesions",
            "Premature leaf drop and defoliation"
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove severely infected plants",
            "Avoid handling wet plants",
            "Use biological controls (Bacillus subtilis)"
        ],
        "prevention": [
            "Use disease-free transplants only",
            "Practice 3-year crop rotation",
            "Avoid overhead watering",
            "Space plants for good air flow (18-24 inches)"
        ],
        "organic_solutions": [
            "Fixed copper sprays weekly",
            "Bacillus subtilis biological spray",
            "Maintain excellent sanitation",
            "Remove infected material promptly"
        ]
    },
    
    # OTHER CROPS
    "orange citrus greening": {
        "description": "Devastating bacterial disease spread by Asian citrus psyllid.",
        "symptoms": [
            "Yellowing of leaves (blotchy mottle pattern)",
            "Misshapen, bitter fruit",
            "Premature fruit drop",
            "Tree decline and eventual death"
        ],
        "treatment": [
            "Remove infected trees immediately and destroy",
            "Control psyllid vectors with systemic insecticides",
            "No cure currently available for infected trees",
            "Report to local agricultural authorities"
        ],
        "prevention": [
            "Control Asian citrus psyllid aggressively",
            "Use only certified disease-free nursery stock",
            "Remove infected trees promptly to prevent spread",
            "Apply systemic insecticides for psyllid control"
        ],
        "organic_solutions": [
            "Focus on aggressive psyllid control",
            "Neem oil for psyllid control",
            "Remove and destroy infected trees immediately",
            "Monitor trees regularly for symptoms"
        ]
    },
    
    "squash powdery mildew": {
        "description": "Fungal disease causing white powdery coating on squash leaves.",
        "symptoms": [
            "White powdery spots on upper leaf surfaces",
            "Spots enlarge and merge covering entire leaf",
            "Leaf yellowing and eventual death",
            "Reduced fruit production and quality"
        ],
        "treatment": [
            "Apply fungicides (sulfur, potassium bicarbonate)",
            "Remove heavily infected leaves",
            "Improve air circulation around plants",
            "Apply fungicides early in infection cycle"
        ],
        "prevention": [
            "Plant resistant varieties when available",
            "Ensure good air flow between plants",
            "Avoid overhead watering",
            "Space plants properly (3-4 feet apart)"
        ],
        "organic_solutions": [
            "Baking soda spray (1 tbsp per gallon water)",
            "Neem oil spray weekly",
            "Milk spray solution (1:9 milk to water ratio)",
            "Sulfur dust applications"
        ]
    },
    
    "strawberry leaf scorch": {
        "description": "Fungal disease causing purple to brown spots on strawberry leaves.",
        "symptoms": [
            "Purple spots with white to gray centers",
            "Spots may merge together",
            "Leaf margins turn brown (scorch appearance)",
            "Reduced plant vigor and yield"
        ],
        "treatment": [
            "Remove infected leaves promptly",
            "Apply fungicides (myclobutanil, captan)",
            "Improve drainage in planting area",
            "Thin plants for better air flow"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Ensure excellent drainage",
            "Avoid overhead watering",
            "Remove old leaves in spring before new growth"
        ],
        "organic_solutions": [
            "Copper fungicides",
            "Remove infected foliage immediately",
            "Improve air circulation between plants",
            "Maintain optimal plant nutrition"
        ]
    },
    
    "peach bacterial spot": {
        "description": "Bacterial disease affecting peach leaves and fruit.",
        "symptoms": [
            "Small purple spots on leaves",
            "Spots may have yellow halos",
            "Holes in leaves (shot-hole appearance)",
            "Spots and lesions on fruit"
        ],
        "treatment": [
            "Apply copper sprays during dormant season",
            "Remove infected twigs and branches",
            "Improve air circulation through proper pruning",
            "Apply bactericides in early spring"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Prune trees for good air flow",
            "Avoid overhead irrigation",
            "Remove and destroy fallen leaves"
        ],
        "organic_solutions": [
            "Copper spray during dormancy",
            "Bordeaux mixture applications",
            "Remove infected branches promptly",
            "Maintain overall tree health"
        ]
    },
    
    # HEALTHY PLANTS
    "healthy": {
        "description": "Plant appears healthy with no signs of disease.",
        "symptoms": [
            "Vibrant green foliage",
            "Normal growth patterns",
            "No spots, lesions, or discoloration",
            "Good fruit or flower production"
        ],
        "treatment": [
            "No treatment needed",
            "Continue regular care and monitoring",
            "Monitor for any changes",
            "Maintain preventive practices"
        ],
        "prevention": [
            "Continue proper watering schedule",
            "Maintain balanced fertilization",
            "Ensure good air circulation",
            "Regular monitoring for pests and diseases"
        ],
        "organic_solutions": [
            "Maintain healthy soil with compost additions",
            "Practice crop rotation",
            "Use companion planting strategies",
            "Regular inspection and monitoring"
        ]
    }
}


def normalize_disease_name(name):
    """
    Normalize disease name for flexible matching
    Removes special characters, extra spaces, converts to lowercase
    """
    if not name:
        return ""
    
    # Convert to lowercase
    normalized = name.lower()
    
    # Replace common separators with spaces
    normalized = normalized.replace('___', ' ')
    normalized = normalized.replace('__', ' ')
    normalized = normalized.replace('_', ' ')
    normalized = normalized.replace('-', ' ')
    
    # Remove parentheses and contents
    normalized = re.sub(r'\([^)]*\)', '', normalized)
    
    # Remove special characters except spaces
    normalized = re.sub(r'[^a-z0-9\s]', '', normalized)
    
    # Remove extra spaces
    normalized = ' '.join(normalized.split())
    
    return normalized.strip()


def get_remedy(disease_name):
    """
    Get remedy information for a disease with FLEXIBLE MATCHING
    
    Args:
        disease_name: str - Disease name in any format
    
    Returns:
        dict - Remedy information
    """
    if not disease_name:
        return _get_default_remedy("Unknown disease")
    
    # Normalize the input disease name
    normalized_input = normalize_disease_name(disease_name)
    
    # Try exact match first (normalized)
    if normalized_input in DISEASE_REMEDIES:
        return DISEASE_REMEDIES[normalized_input]
    
    # Try matching against all database keys (normalized)
    for key, remedy in DISEASE_REMEDIES.items():
        normalized_key = normalize_disease_name(key)
        
        # Exact match after normalization
        if normalized_input == normalized_key:
            return remedy
        
        # Partial match (contains)
        if normalized_input in normalized_key or normalized_key in normalized_input:
            return remedy
    
    # Check for "healthy" keyword
    if 'healthy' in normalized_input:
        return DISEASE_REMEDIES.get('healthy', _get_default_remedy(disease_name))
    
    # Check for specific crops
    crop_keywords = {
        'apple': ['apple scab', 'apple black rot', 'apple cedar apple rust'],
        'tomato': ['tomato bacterial spot', 'tomato early blight', 'tomato late blight', 
                   'tomato leaf mold', 'tomato septoria leaf spot', 'tomato spider mites',
                   'tomato target spot', 'tomato yellow leaf curl virus', 'tomato mosaic virus'],
        'potato': ['potato early blight', 'potato late blight'],
        'corn': ['corn cercospora leaf spot', 'corn common rust', 'corn northern leaf blight'],
        'grape': ['grape black rot'],
        'pepper': ['pepper bacterial spot'],
        'orange': ['orange citrus greening'],
        'squash': ['squash powdery mildew'],
        'strawberry': ['strawberry leaf scorch'],
        'peach': ['peach bacterial spot']
    }
    
    # Try to match by crop
    for crop, diseases in crop_keywords.items():
        if crop in normalized_input:
            # Try to find the best matching disease for this crop
            for disease in diseases:
                normalized_disease = normalize_disease_name(disease)
                if any(word in normalized_input for word in normalized_disease.split()):
                    if disease in DISEASE_REMEDIES:
                        return DISEASE_REMEDIES[disease]
    
    # Default fallback
    print(f"⚠️ Warning: Disease '{disease_name}' not found in database. Using fallback.")
    return _get_default_remedy(disease_name)


def _get_default_remedy(disease_name):
    """Return default remedy when disease is not found"""
    return {
        "description": f"Information not available in database for: {disease_name}",
        "symptoms": [
            "Unable to identify specific symptoms for this condition",
            "Consult with a plant pathologist or agricultural extension service for accurate diagnosis"
        ],
        "treatment": [
            "Document all symptoms with clear photographs",
            "Isolate affected plants if possible to prevent spread",
            "Contact your local agricultural extension office",
            "Consider sending plant samples to a diagnostic laboratory",
            "Keep detailed records of when symptoms first appeared"
        ],
        "prevention": [
            "Maintain overall plant health with proper watering and fertilization",
            "Ensure good air circulation around plants",
            "Practice crop rotation when possible",
            "Use disease-resistant varieties when available",
            "Monitor plants regularly for early detection"
        ],
        "organic_solutions": [
            "Focus on preventive cultural practices",
            "Maintain healthy soil with regular compost additions",
            "Monitor plants weekly for any changes",
            "Remove diseased material promptly and destroy (do not compost)",
            "Consult organic farming resources for specific recommendations"
        ]
    }



    
#     return text
def format_remedy_text(disease_name, remedy_info):
    """
    Format remedy information into clean, readable text (no markdown **)
    
    Args:
        disease_name: str
        remedy_info: dict
        
    Returns:
        str - Formatted remedy text
    """
    text = f"{disease_name}\n\n"
    text += f"Cause: {remedy_info.get('description', 'No description available.')}\n\n"

    # Add symptoms (optional, for detail)
    if remedy_info.get('symptoms'):
        text += "Key Symptoms:\n"
        for symptom in remedy_info['symptoms'][:3]:  # show top 3
            text += f"- {symptom}\n"
        text += "\n"

    # Add main remedy/treatment
    if remedy_info.get('treatment'):
        text += "Remedy:\n"
        for treatment in remedy_info['treatment'][:3]:
            text += f"- {treatment}\n"
        text += "\n"

    # Optionally show prevention
    if remedy_info.get('prevention'):
        text += "Prevention:\n"
        for prevention in remedy_info['prevention'][:2]:
            text += f"- {prevention}\n"
        text += "\n"

    # Optionally show organic solutions
    if remedy_info.get('organic_solutions'):
        text += "Organic Tips:\n"
        for solution in remedy_info['organic_solutions'][:2]:
            text += f"- {solution}\n"

    return text.strip()
