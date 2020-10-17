import argparse
import requests


def find_stock(zip_code: int,
               target_sku: str,
               num_stores: int = 5,
               radius: int = 100):
    """
    Request the DSG API to find nearby stores with available inventory for a given product SKU
    """

    # Need referer and user-agent for successful requests to API
    referer_url = "https://www.dickssportinggoods.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "referer": referer_url}
    base_url = "https://availability.dickssportinggoods.com/ws/v2/omni/stores"

    query_params = f"?addr={zip_code}&radius={radius}&uom=imperial&lob=dsg&sku={target_sku}&res=locatorsearch"
    search_url = base_url + query_params

    resp = requests.get(search_url, headers=headers)
    resp_json = resp.json()

    stores = resp_json.get("data").get("results")
    num_found = 0

    print(f"Checked {len(stores)} stores within a {radius}mi radius from {zip_code}...\n")
    for s in stores:
        if num_found >= num_stores:
            break
        store = s.get("store")
        skus = s.get("skus")
        street1 = store.get("street1")
        street2 = store.get("street2")
        city = store.get("city")
        state = store.get("state")
        zip_ = store.get("zip")
        distance = s.get("distance")

        for sku in skus:
            qty = sku.get("qty")
            ats = qty.get("ats")
            isa = qty.get("isa")

            if "0" not in [ats, isa]:
                num_found += 1
                print(
                    f"{street1}\n{street2}\n{city}, {state} {zip_}\n{distance}mi from {zip_code}\nQty: ats:{ats} | isa:{isa}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--zip_code',
        required=True,
        type=int,
        help='Zipcode to search with 250mi radius'
    )
    parser.add_argument(
        '--num_stores',
        required=True,
        type=int,
        help='Number of stores to display'
    )
    parser.add_argument(
        '--skus',
        required=True,
        type=str,
        nargs="+",
        help='Item SKUs to search'
    )
    known_args, args = parser.parse_known_args()

    for sku in known_args.skus:
        print(f"~~ SKU: {sku} ~~")
        find_stock(zip_code=known_args.zip_code, target_sku=sku, num_stores=known_args.num_stores, radius=250)
