
import requests
import pandas as pd

endpoints = {
    "zakladni_prehled": "https://onemocneni-aktualne.mzcr.cz/api/v3/zakladni-prehled",
    "hospitalizace": "https://onemocneni-aktualne.mzcr.cz/api/v3/hospitalizace",
    "ockovani_hospitalizace": "https://onemocneni-aktualne.mzcr.cz/api/v3/ockovani-hospitalizace",
    "incidence_cr": "https://onemocneni-aktualne.mzcr.cz/api/v3/incidence-7-14-cr",
    "incidence_kraje": "https://onemocneni-aktualne.mzcr.cz/api/v3/incidence-7-14-kraje",
    "nakazeni_vyleceni_umrti_testy": "https://onemocneni-aktualne.mzcr.cz/api/v3/nakazeni-vyleceni-umrti-testy",
    "ockovani": "https://onemocneni-aktualne.mzcr.cz/api/v3/ockovani",
    "ockovani_demografie": "https://onemocneni-aktualne.mzcr.cz/api/v3/ockovani-demografie"
}

headers = {
    "Authorization": "Bearer token 31926f88785231e1e11a74f7557df78f"
    }

for name, url in endpoints.items():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data) if isinstance(data, list) else pd.json_normalize(data)
        df.to_csv(f'{name}.csv', index=False)
        print(f"Data pro {name} byla uložena do souboru {name}.csv.")
    else:
        print(f"Chyba při načítání dat pro {name}: {response.status_code}")

        