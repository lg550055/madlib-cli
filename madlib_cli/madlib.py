import re

def read_template(path):
  try:
    with open(path) as file:
      return file.read()
  except FileNotFoundError as err:
    raise err

def parse_template(text):
  p = re.findall(r'\{\w+\}', text)
  parts = [re.sub(r'[\{\}]','', e) for e in p]
  stp = re.sub(r'\{\w+\}','{}', text)
  return stp, tuple(parts)

def merge(stp, parts):
  return stp.format(*parts)


# @pytest.mark.skip("pending")
# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "missing.txt"
#         read_template(path)
