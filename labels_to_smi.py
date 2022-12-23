import sys

def main(argv):
  if len(argv) < 3:
    print("Usage: " + argv[0] + " input_file_name.txt output_file_name.smi")
    return
  
  aud = []
  with open(argv[1], 'r', encoding='utf8') as file_in:
    aud = file_in.readlines()

  # SAMI file conversion
  smi = {
    0: ""
  }
  for line in aud:
    if len(line) == 0: continue
    tokens = line.split("\t")
    smi[int(1000 * float(tokens[0]))] = tokens[2].strip()
    smi[int(1000 * float(tokens[1]))] = ""

  with open(argv[2], 'w', encoding='utf8') as file_out:
    file_out.write("""<SAMI>
<HEAD>
<TITLE>Untitled</TITLE>
<SAMIParam>
  Metrics {{time:ms;}}
  Spec {{MSFT:1.0;}}
</SAMIParam>
<STYLE TYPE="text/css">
  <!-- no style -->
</STYLE>
</HEAD>
<BODY>
""")
    for key, value in smi.items():
      file_out.write('<SYNC Start="' + str(key) + '"><P Class="ENUSCC">' + value + '</P></SYNC>\n')
    file_out.write("""</BODY>
</SAMI>""")


if __name__ == "__main__":
  main(sys.argv)