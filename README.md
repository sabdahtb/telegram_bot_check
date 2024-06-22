# Telegram Dex Checker Bot

This Telegram bot allows users to check the status of tokens on Dexscreener using the CheckDex API.

## Features

- **Check Token Address:** Users can input a token address, and the bot will fetch its status from Dexscreener.
- **Interactive Replies:** Replies include detailed information about whether the token is paid for Dexscreener or not.
- **Error Handling:** Provides informative messages if there are any issues during the token check process.

## Usage

1. Start the bot by sending `/start` command.
2. Enter a token address to check its status.
3. The bot will respond with whether the token is paid for Dexscreener or not.

## Commands

- `/start`: Initializes the bot and provides instructions.
- _Entering a token address_: Initiates the check process for the provided token address.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## API Reference

The bot uses the CheckDex API to fetch token information. For more details, refer to the [CheckDex](https://checkdex.xyz/).
