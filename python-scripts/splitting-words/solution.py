def main(word, parts):
  result = []
  part = ""
  list_parts = parts.split(",")
  for l_ in word:
    part += l_
    if part.strip() in list_parts:
      result.append(part.strip())
      list_parts.remove(part.strip())
      part = ""
  if len(result) != 2:
    result = []
  return result



