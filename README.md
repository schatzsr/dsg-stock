# dsg-stock
_A product of late-night curiosity._

Small tool written in Python 3.7 to query Dick's Sporting Goods' API based on a product's SKU. 

Fitness equipment is scarce during the Covid pandemic. 
Products go out of stock quickly and DSG's store-search on their site isn't too great.
Users are limited to searching 100mi radius from a zip code, but apparently requesting the backend endpoints directly allows for 250mi and also provides stock quantities...

## TODO
- Deploy on GCP: [Free usage tiers](https://cloud.google.com/free/docs/gcp-free-tier)
    - Lightweight: Cloud Functions or Cloud Run
- Cron schedule to request endpoint using Cloud Scheduler
- Sendgrid emailing: Notify when products are in stock and close distance
- ???