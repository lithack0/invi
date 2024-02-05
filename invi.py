import pyperclip
import argparse
parser = argparse.ArgumentParser(description="This is a tool for making invisible character.")
parser.add_argument('--encode',help='Enter the text which you want to be decoded',dest="encode",type=str)
parser.add_argument('--decode',help='Enter the decoded text to be converted back into the plain text',dest="decode",type=str)
args = parser.parse_args()


def convert_to_tag_chars(input_string):

    return ''.join(chr(0xE0000 + ord(ch)) for ch in input_string)


def convert_to_original_chars(tag_chars):
  original_chars = []
  for ch in tag_chars:
    # Get the numerical value of the tag character
    tag_value = ord(ch) - 0xE0000

    # Ensure the tag value is within the valid range
    if not 0 <= tag_value <= 0xFFFF:
      raise ValueError("Invalid tag character: {}".format(ch))

    # Convert the tag value back to its original character
    original_char = chr(tag_value)
    original_chars.append(original_char)

  return ''.join(original_chars)
if(args.encode):   
    tagged_output = convert_to_tag_chars(str(args.encode))
    print("Tagged output:", tagged_output)
elif(args.decode):
    decoded=convert_to_original_chars(str(args.decode))
    print(decoded)
else:
    print("No argument supplied...")

