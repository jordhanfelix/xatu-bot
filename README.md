# XATU - WhatsApp Automation Bot for Football Match Organization

## Overview

XATU is a Python script designed to automate the process of sending football match attendance confirmation messages on WhatsApp. The script utilizes the pywhatkit library to send messages instantly to either individual contacts or group chats.

## Features

- Sends a customizable attendance confirmation message to a specified contact or group.
- Allows parameterization through a `.env` file for easy customization.
- Automatically calculates and selects the next Friday as the default event date.

## Prerequisites

- Python 3.x installed.
- Pip installed.
- Required Python packages installed. Install dependencies using:

    ```bash
    pip install python-dotenv pywhatkit pyautogui
    ```

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/seuusuario/seurepositorio.git
    ```

2. Navigate to the project directory:

    ```bash
    cd seurepositorio
    ```

3. Create a `.env` file in the root directory with the following parameters:

    ```
    MODE="Message sending mode (group or contact)"
    CONTACT_ID="WhatsApp contact number or group ID"
    ```

4. Run the script:

    ```bash
    python xatu.py
    ```

## Parameters

- **MODE**: Message sending mode, can be either "group" or "contact".
- **CONTACT_ID**: WhatsApp contact number or group ID.

## Usage

- The script will automatically calculate the next Friday's date for the football match.
- Customizable message includes details such as location, date, time, advance payment amount, PIX key, and responsible PIX owner.
- Supports sending messages to individual contacts or group chats based on the specified mode.

## Acknowledgments

- Inspired by the Pokémon "Xatu" for its timely predictions and automation.

## License

This project is licensed under the [MIT License](LICENSE).
