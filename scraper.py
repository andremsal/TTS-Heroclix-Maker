import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

# Ensure the script runs in its own directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# Get collection name from user input
collection_code = input("Qual o id da coleção (ex: wk25)? ")
collection_name = input("Qual o nome da coleção (ex: Wizkids 2025)? ")

search_url = f"https://hcunits.net/api/v1/units/?ext=json&set_id={collection_code}"
print(f"Buscando unidades da coleção {collection_code}...")

character_ids = []

# Fetch all units from the API with pagination
while search_url:
    response = requests.get(search_url)
    
    if response.status_code != 200:
        print(f"Erro ao acessar a API: Status {response.status_code}")
        exit()
    
    data = response.json()
    
    if isinstance(data, dict) and 'results' in data:
        character_ids.extend([u['id'] for u in data['results']])
        search_url = data.get('next')
    elif isinstance(data, list):
        character_ids.extend([u['id'] for u in data])
        search_url = None
    else:
        print("Formato de resposta inesperado ou nenhum resultado encontrado.")
        exit()

print(f"Total de personagens encontrados: {len(character_ids)}")

# Create folder if it doesn't exist
if not os.path.exists(collection_name):
    os.makedirs(collection_name)
    print(f"Pasta '{collection_name}' criada.")

# Initialize Selenium WebDriver
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

# Iterates Each Character
for id in character_ids:
    try:
        print(f"Processando personagem: {id}...")
        unit_url = f"https://hcunits.net/units/{id}"
        
        driver.get(unit_url)
        
        # Wait for the page to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.ID, "unitCard0"))
        )
        
        time.sleep(3)
        
        # Store screenshots temporarily
        cards = []
        card_paths = []
        
        # Find and screenshot unitCard0
        try:
            unitCard0 = driver.find_element(By.ID, "unitCard0")
            temp_path = os.path.join(collection_name, f"temp_{id}_0.png")
            unitCard0.screenshot(temp_path)
            cards.append(temp_path)
            card_paths.append(temp_path)
            print(f"Screenshot capturado: unitCard0")
        except Exception as e:
            print(f"Erro ao capturar unitCard0 para {id}: {e}")
        
        # Find and screenshot unitCard1 if it exists
        try:
            unitCard1 = driver.find_element(By.ID, "unitCard1")
            temp_path = os.path.join(collection_name, f"temp_{id}_1.png")
            unitCard1.screenshot(temp_path)
            cards.append(temp_path)
            card_paths.append(temp_path)
            print(f"Screenshot capturado: unitCard1")
        except Exception as e:
            print(f"unitCard1 não encontrado para {id}")
        
        # Find and screenshot unitCard2 if it exists
        try:
            unitCard2 = driver.find_element(By.ID, "unitCard2")
            temp_path = os.path.join(collection_name, f"temp_{id}_2.png")
            unitCard2.screenshot(temp_path)
            cards.append(temp_path)
            card_paths.append(temp_path)
            print(f"Screenshot capturado: unitCard2")
        except Exception as e:
            print(f"unitCard2 não encontrado para {id}")
        
        # Merge images if more than one card was captured
        if len(cards) > 1:
            try:
                images = [Image.open(card_path) for card_path in cards]
                
                # Calculate total width and max height
                total_width = sum(img.width for img in images)
                max_height = max(img.height for img in images)
                
                # Create new image with combined dimensions
                merged_image = Image.new('RGB', (total_width, max_height))
                
                # Paste images side by side
                x_offset = 0
                for img in images:
                    merged_image.paste(img, (x_offset, 0))
                    x_offset += img.width
                
                # Save merged image
                merged_path = os.path.join(collection_name, f"{id}_combined.png")
                merged_image.save(merged_path)
                print(f"Imagens mescladas salvas: {merged_path}")
                
                # Delete temporary files
                for temp_path in card_paths:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                
            except Exception as e:
                print(f"Erro ao mesclar imagens para {id}: {e}")
        elif len(cards) == 1:
            # If only one card, rename it to final name
            final_path = os.path.join(collection_name, f"{id}.png")
            os.rename(cards[0], final_path)
            print(f"Imagem salva: {final_path}")
    
    except Exception as e:
        print(f"Erro ao processar {id}: {e}")
        continue

# Close the browser
driver.quit()
print("Processamento concluído!")