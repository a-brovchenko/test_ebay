# test_ebay

## Running the Locally

 - Create a virtual environment
```bash
python -m venv .venv
```
- Activate virtual environment
``` bash
for Windows - .venv\Scripts\activate

for Linux/macOS - source .venv/bin/activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```

Before running the script, pass the eBay item number to the instance of the class 
```bash
product = EbayData(186522312139)
```

- Ranning main.py
```bash
python main.py
```
- expected output

```bash

{
  "product_name": "6-String DIME Dimebag Darrell Signature Model ML Profiled Electric Guitar",
  "product_price": "US $319.00",
  "product_url": "https://www.ebay.com/itm/186522312139",
  "saller_name": "SWguitar",
  "img_url": [
    "https://i.ebayimg.com/images/g/9HYAAOSw5NBmfnAo/s-l140.jpg",
    "https://i.ebayimg.com/images/g/UsMAAOSwfLVmfnAs/s-l140.jpg",
    "https://i.ebayimg.com/images/g/zSgAAOSwFfBmfnAy/s-l140.jpg",
    "https://i.ebayimg.com/images/g/qK0AAOSwsI5mfnA2/s-l140.jpg",
    "https://i.ebayimg.com/images/g/KNkAAOSwNf5mfnA9/s-l140.jpg",
    "https://i.ebayimg.com/images/g/WCMAAOSwEZVmfnBB/s-l140.jpg",
    "https://i.ebayimg.com/images/g/-jYAAOSwCFhmfnBG/s-l140.jpg",
    "https://i.ebayimg.com/images/g/wWwAAOSwqF1mfnBK/s-l140.jpg",
    "https://i.ebayimg.com/images/g/9GsAAOSwQlhmfnBP/s-l140.jpg",
    "https://i.ebayimg.com/images/g/Mp4AAOSwpXRmfnBV/s-l140.jpg",
    "https://i.ebayimg.com/images/g/ddcAAOSwsStmfnBa/s-l140.jpg"
  ]
}
```