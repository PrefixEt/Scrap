# ScrabProject

Simple but strong web scraping with BS4 and requests modules what parse data from https://www.lueftner-cruises.com/en/river-cruises/cruise.html .
Program parsing four first pages, and save all valuable cruise information in result.txt as json.




**install and start**
>>clone this project

>>python3 -m venv venv

>>source ./venv/bin/activate

>>pip install --upgrade pip

>>pip install -r requirements.txt

>>python3 scraper.py

>>or just run setup.sh bash script for this in terminal


example data:
```
"name": "Classical Rhine Cruise",
        "itineary": [
            "Amsterdam",
            "Amsterdam>Hoorn",
            "Cologne",
            "Cochem",
            "Koblenz>Rüdesheim",
            "Mannheim>Speyer",
            "Strassbourg",
            "Basel"
        ],
        "days": [
            {
                "07-May-2019": {
                    "ship": "MS Amadeus Silver III",
                    "price": "1759,00"
                }
            },
      		{...},

            {
                "24-Oct-2019": {
                    "ship": "MS Amadeus Silver II",
                    "price": "1769,00"
                }
            }
        ]
    }
```
