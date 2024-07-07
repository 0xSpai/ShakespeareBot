# Shakespeare Twitter Bot

A Twitter bot for posting every word of Shakespeare at an interval of time.

## Features

1) Splits any body of text into words
2) Uses the Twitter API to make posts
3) Highly customizable

## Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/0xSpai/ShakespeareBot.git
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up API keys**:

Create a new file called `keys.py` and enter the following code:

```python
api_key = ''
api_key_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''
```

Visit `https://developer.x.com/` and sign up for a developer account. Fill the relevant fields with your API tokens.

> [!IMPORTANT]
> Ensure these keys are kept **private**. If leaked, they could be used to write/read on your account.

4. **Run the Project**:

```bash
python bot.py
```

## License

Distributed under the GNU General Public License. See `LICENSE.txt` for more information.