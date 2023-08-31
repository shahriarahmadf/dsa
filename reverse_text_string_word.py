text = 'Hello how are you?'
def reverse_text_string_word(text):
  end = -1
  reversed_text = ''
  for i in range(-1,-(len(text)+1),-1):
    if(text[i] == ' '):
      for j in range(i+1,end+1, 1):
        reversed_text += text[j]
      reversed_text += ' '
      end = i - 1
  if end != -1:
    for j in range(0,(len(text)+end)+1,1):
      print(text[j])
      reversed_text += text[j]
  return reversed_text

print(reverse_text_string_word(text))