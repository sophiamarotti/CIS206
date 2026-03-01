"""
Session 7 - Run-Length Encoding (RLE) with Escape Sequences

Implements:
Activity 1: Encode alphabetic strings using compressed RLE format where single
            instances have no count (e.g., AAABCC -> A3BC2).
Activity 2: If input contains numbers, treat as already RLE and decode it;
            otherwise encode it. Uses separate decode function.
Activity 3: Adds escape handling using '#':
            - '#<digit>' means the digit is a literal character, not a count.
            - '##' means a literal '#'.
            - Encoded strings begin with '##00' to indicate it is already encoded.
              This makes decoding unambiguous even if the payload contains digits.

Author: Sophia Marotti
"""

from __future__ import annotations


ENCODED_PREFIX = "##00"


def _require_string(value, name: str) -> None:
    """Parameter validation: ensure a value is a string."""
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a str, got {type(value).__name__}.")


def _escape_literal_char(ch: str) -> str:
    """
    Escape a single character for the encoded payload.

    Rules:
    - '#' becomes '##'
    - digits '0'-'9' become '#<digit>'
    - all other characters pass through unchanged
    """
    if ch == "#":
        return "##"
    if ch.isdigit():
        return "#" + ch
    return ch


def encode_rle(raw: str) -> str:
    """
    Encode a raw string into RLE format with escape support.

    Output format:
    - Always starts with ENCODED_PREFIX ("##00") to indicate it's encoded.
    - Uses compressed counts: repeats of 2+ become <escaped_char><count>
      and single occurrences become just <escaped_char> (no count).

    Examples (payload shown without prefix):
    - "AAABCC" -> "A3BC2"   (full output: "##00A3BC2")
    - "A2" -> "A#23" would be ambiguous without escaping; we escape digits:
      "A2" -> "A#2" (full output: "##00A#2")
    """
    _require_string(raw, "raw")

    if raw == "":
        # Still mark as encoded; empty payload.
        return ENCODED_PREFIX

    out_parts: list[str] = [ENCODED_PREFIX]
    count = 1
    prev = raw[0]

    for i in range(1, len(raw)):
        cur = raw[i]
        if cur == prev:
            count += 1
        else:
            out_parts.append(_escape_literal_char(prev))
            if count > 1:
                out_parts.append(str(count))
            prev = cur
            count = 1

    # finalize last run
    out_parts.append(_escape_literal_char(prev))
    if count > 1:
        out_parts.append(str(count))

    return "".join(out_parts)


def _unescape_one(s: str, idx: int) -> tuple[str, int]:
    """
    Read ONE literal character from encoded payload at position idx, supporting escapes.

    Returns (literal_char, next_index).

    Encoded payload rules:
    - '##' represents literal '#'
    - '#<digit>' represents literal digit
    - Any other single non-digit char represents itself
    """
    if idx >= len(s):
        raise ValueError("Unexpected end of encoded data while reading a character.")

    ch = s[idx]
    if ch == "#":
        if idx + 1 >= len(s):
            raise ValueError("Dangling '#' at end of encoded data.")
        nxt = s[idx + 1]
        if nxt == "#":
            return "#", idx + 2
        if nxt.isdigit():
            return nxt, idx + 2
        raise ValueError(f"Invalid escape sequence '#{nxt}' in encoded data.")
    else:
        # In our encoding scheme, digits should never appear unescaped as characters.
        if ch.isdigit():
            raise ValueError(
                "Invalid encoded data: digit appeared where a character was expected "
                "(digits must be escaped with '#')."
            )
        return ch, idx + 1


def decode_rle(encoded: str) -> str:
    """
    Decode a string that is in the '##00' prefixed RLE format with escapes.

    Expected input:
    - Must start with ENCODED_PREFIX ("##00").
    - After prefix, data is a sequence of:
        <escaped_char> [<count>]
      where <count> is one or more digits and is optional (defaults to 1).

    Examples:
    - "##00A3BC2" -> "AAABCC"
    - "##00##2"   -> "##" repeated 2 times -> "##"
      (payload "##2" means literal '#' (escaped as '##') with count 2)
    """
    _require_string(encoded, "encoded")

    if not encoded.startswith(ENCODED_PREFIX):
        raise ValueError("Encoded string must start with '##00'.")

    payload = encoded[len(ENCODED_PREFIX) :]

    # Empty payload decodes to empty string
    if payload == "":
        return ""

    out_chars: list[str] = []
    i = 0

    while i < len(payload):
        literal, i = _unescape_one(payload, i)

        # Read optional count (one or more digits)
        j = i
        while j < len(payload) and payload[j].isdigit():
            j += 1

        if j == i:
            count = 1
        else:
            count_str = payload[i:j]
            count = int(count_str)
            if count <= 0:
                raise ValueError("Count must be a positive integer.")
            i = j

        out_chars.append(literal * count)

    return "".join(out_chars)


def is_probably_encoded(user_input: str) -> bool:
    """
    Decide whether to decode or encode based on the assignment rules.

    Activity 3 rule:
    - If it starts with '##00', it's already encoded -> decode.

    Activity 2 rule (fallback):
    - If it contains any digit and doesn't start with '##00', treat it as RLE -> decode.
      (This matches the wording, though it can be ambiguous without the prefix.)
    """
    _require_string(user_input, "user_input")

    if user_input.startswith(ENCODED_PREFIX):
        return True
    return any(ch.isdigit() for ch in user_input)


def validate_activity1_input_alpha(s: str) -> None:
    """
    Activity 1 validation: must be alphabetic characters only (A-Z/a-z) and non-empty.
    """
    _require_string(s, "s")
    if s == "":
        raise ValueError("Input cannot be empty for Activity 1.")
    if not s.isalpha():
        raise ValueError("Activity 1 requires alphabetic characters only (A-Z/a-z).")


def main() -> None:
    """
    Main program:
    - Prompts user for a string.
    - If it starts with ##00 -> decode (Activity 3).
    - Else if it contains digits -> attempt to decode (Activity 2).
    - Else encode (Activity 1/2/3 encoding format with prefix and escapes).
    """
    user_input = input("Enter a string: ").strip()

    try:
        if user_input.startswith(ENCODED_PREFIX):
            # Activity 3 decode path
            decoded = decode_rle(user_input)
            print("Detected encoded format (##00). Decoded:", decoded)
        elif any(ch.isdigit() for ch in user_input):
            # Activity 2 decode path (legacy/no prefix)
            # NOTE: This legacy decode expects classic RLE like A3BC2 (no prefix),
            # and digits represent counts. Characters are assumed non-digit.
            # If you want to strictly follow Activity 3, use the ##00 format.
            decoded = decode_legacy_rle(user_input)
            print("Detected digits (assumed RLE). Decoded:", decoded)
        else:
            # Encode path (Activity 1/3 format)
            # If you want to enforce Activity 1 alphabetic-only, uncomment next line:
            # validate_activity1_input_alpha(user_input)
            encoded = encode_rle(user_input)
            print("Encoded:", encoded)

    except Exception as exc:
        print("Error:", exc)


# --- Legacy decoder for Activity 2 (strings with numbers but without ##00 prefix) ---

def decode_legacy_rle(s: str) -> str:
    """
    Decode a legacy RLE string that does NOT use escapes or the ##00 prefix.
    Expected pattern like: A3BC2 -> AAABCC

    Rules:
    - A letter followed by digits means repeat that letter count times.
    - A letter with no digits after it means count 1.
    - Digits must follow a non-digit character.

    This is provided to satisfy Activity 2’s “if it has numbers, decode it” wording.
    Activity 3 supersedes this with the ##00 prefixed, escape-safe format.
    """
    _require_string(s, "s")
    if s == "":
        return ""

    out: list[str] = []
    i = 0

    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            raise ValueError("Invalid legacy RLE: count appears before a character.")
        i += 1

        # read optional count
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1

        if j == i:
            count = 1
        else:
            count = int(s[i:j])
            if count <= 0:
                raise ValueError("Count must be a positive integer.")
            i = j

        out.append(ch * count)

    return "".join(out)


if __name__ == "__main__":
    main()
