# blaze-take-home

## Task

1.  Scrape the Twitter followers of the some accounts.
1.  For all the users who have a .eth address in their name or bio, get the corresponding wallet address.

## Solution

- First scrape the Twitter followers of the accounts using the Twitter API. `scrape.py` does this.
- Then for each user, check if they have a .eth address in their name or bio. `parse.py` does this.
- If they do, get the corresponding wallet address using the ENS API. `wallet.py` does this.

### Limitations

- The Twitter API only allow 15 API request per 15 minutes window. This is managed by putting code to sleep at 429 error.
- (My setup) The ENS API is working on a remote provider which has cap of 1 Million API credits.

## How to run

1.  Clone the repo.
1.  Create a virtual environment. `python -m venv venv`
1.  Install the requirements. `pip install -r requirements.txt`
1.  Provide the Twitter API credentials and a remote eth node.
    ```sh
    # To set your environment variables in your terminal run the following lines:
    export BEARER_TOKEN='<your_bearer_token>'
    export PROVIDER_URL='<your_http_provider_url>'
    ```
1.  If you want to scrape the followers of a different account, change the `usernames` variable in `main.py`.
1.  Run `main.py`. Using command: `python main.py`
1.  The followers data of users will be stored in `out/<username>.json`.
1.  The wallet addresses will be stored in `out/wallet.csv`.

## Observation

- Occurences of `.eth` in entire [user model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) is either in name, description or as url in description or profile url and location. Per the instruction code only scrapes for name and bio but could easily be scaled to all aforementioned paramenters.
- eth addresses are only having alphanumeric characters and period(.) and hyphen(-) ending with .eth. If there are more allowed charecters, regex can be updated.

## Author

- [Harshit Raj](https://harshitraj.me)
