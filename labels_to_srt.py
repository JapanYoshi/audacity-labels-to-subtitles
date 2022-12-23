import sys

def main(argv):
  if len(argv) < 3:
    print("Usage: " + argv[0] + " input_file_name.txt output_file_name.srt")
    return
  
  aud = []
  with open(argv[1], 'r', encoding='utf8') as file_in:
    aud = file_in.readlines()

  # SRT file conversion
  def to_timestamp(frac_sec: float):
    sec = frac_sec // 1
    frac_sec -= sec
    frac_sec = (frac_sec * 1000) // 1
    min = sec // 60
    sec -= min * 60
    hrs = min // 60
    min -= hrs * 60
    return f"{int(hrs):02d}:{int(min):02d}:{int(sec):02d},{int(frac_sec):03d}"

  with open(argv[2], 'w', encoding='utf8') as file_out:
    count: int = 0
    for line in aud:
      if len(line) == 0: continue
      tokens = line.split("\t")
      count += 1
      file_out.write(f"{count}\n{to_timestamp(float(tokens[0]))} --> {to_timestamp(float(tokens[1]))}\n{tokens[2]}\n\n")


if __name__ == "__main__":
  main(sys.argv)