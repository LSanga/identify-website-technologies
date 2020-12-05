# identify-website-technologies
Bulk scrape webiste and identify technologies using wappalyzer npm module. 

This script is optimized to work with SecApps output (https://secapps.com/). After launching a Scout, download either the URL or the Domain list and use that file (data.csv) as input.
It's slow to run. Output will be a txt file with the URL/Domain and the list of technologies.

With URL list:
```

python fixer.py -u data.csv

python wappalyzer-script.py -u
```

With Domain list:
```
python wappalyzer-script.py
```
