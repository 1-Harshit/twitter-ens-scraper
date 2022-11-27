# blaze-take-home

## Task

1.  Scrape the Twitter followers of some accounts.
1.  Get the corresponding wallet address for all users with a `.eth` address in their name or bio.

## Solution

- First, scrape the Twitter followers of the accounts using the Twitter API. `scrape.py` does this.
- Then for each user, check if they have a .eth address in their name or bio. `parse.py` does this.
- If they do, get the corresponding wallet address using the ENS API. `wallet.py` does this.

### Limitations

- The Twitter API only allows 15 API requests per 15 minutes window. This is managed by putting code to sleep at 429 error.
- (My setup) The ENS API is working on a remote provider with a cap of 1 Million API credits.

## How to run

1.  Clone the repo.
1.  Create a virtual environment. `python -m venv venv`
1.  Install the requirements. `pip install -r requirements.txt`
1.  Provide the Twitter API credentials and a remote eth node.
    ```sh
    # To set your environment variables in your terminal, run the following lines:
    export BEARER_TOKEN='<your_bearer_token>'
    export PROVIDER_URL='<your_http_provider_url>'
    ```
1.  If you want to scrape the followers of a different account, change the `usernames` variable in `main.py`.
1.  Run `main.py`. Using the command: `python main.py`
1.  The followers' data of users will be stored in `out/<username>.json`.
1.  The wallet addresses will be stored in `out/wallet.csv`.

## Observation

- Occurrences of `.eth` in the entire [user model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) are either in name, description, or as URL in the description or profile URL and location. Per the instruction, the code only scrapes for name and bio but could easily be scaled to all aforementioned parameters.
- eth addresses are only having alphanumeric characters and period(.) and hyphen(-) ending with .eth. If there are more allowed characters, regex can be updated.

## Author

- [Harshit Raj](https://harshitraj.me)

## References

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- [ENS Domains](https://docs.ens.domains/)
- [Quicknode](https://www.quicknode.com/)

## Output

- For the given usernames, the output is stored in `out` folder. Available [here](https://iitk-my.sharepoint.com/:f:/g/personal/harshitr20_iitk_ac_in/EpwpR4fxW9xOkPUcSGoQBgABIz5CTX0jixo5uv0u4OAIVA?e=I84Sg2).
- All wallet addresses are also stored in [google sheets](https://docs.google.com/spreadsheets/d/1PcE9TajBa4ZnutE34xkDWNvwdIvTMZpfF6-zm6KGx74/edit?usp=sharing).
