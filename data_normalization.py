import pandas as pd
from tqdm import tqdm
from get_all_links import get_all_links
from get_all_data import get_all_data

"""
with open("total_data.txt", "r") as fp:
    total_data = json.load(fp)
"""

chromedriver_path = input("Escribe la ruta de tu chrome driver: ")

def data_normalization(chromedriver_path):
    
    ciudad = input("Escribe la ciudad de interés (sin tildes y en minúsculas): ")
    tipo_inmueble = input("Escribe el tipo de inmueble (oficina, local, bodega): ")
    
    all_good_links = get_all_links(chromedriver_path, ciudad, tipo_inmueble)
    total_data, bad_urls = get_all_data(all_good_links, chromedriver_path)
    
    df = pd.json_normalize(total_data[-1], sep='_')
    columns = list(df.columns)
    all_data = pd.DataFrame(columns=columns)

    for i in tqdm(total_data):
        all_data = pd.concat([all_data, pd.json_normalize(i, sep='_')], ignore_index=True)
        
    all_data.drop_duplicates(inplace = True, ignore_index = True,)

    all_data.to_excel('%s_%s.xlsx'%(ciudad, tipo_inmueble), index=False, columns=columns)
    print('Se guardó el archivo en esta misma carpeta con el nombre %s_%s.xlsx'%(ciudad, tipo_inmueble))

data_normalization(chromedriver_path)