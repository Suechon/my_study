import re

text = 'aaa' 
pattern_default = r'a'
pattern_plus = r'a+'
pattern_question = r'a?'
pattern_asta = r'a*'
pattern_lazy_plus_question = r'a+?'
pattern_lazy_asta_question = r'a*?'

print(f"文字列: {text}")
count = re.findall(pattern_default, text)
print(f"{pattern_default}: {len(count)}個マッチ -- {count}")

count = re.findall(pattern_plus, text)
print(f"{pattern_plus}: {len(count)}個マッチ -- {count}")

count = re.findall(pattern_question, text)
print(f"{pattern_question}: {len(count)}個マッチ -- {count}")

count = re.findall(pattern_asta, text)
print(f"{pattern_asta}: {len(count)}個マッチ -- {count}")


count = re.findall(pattern_lazy_plus_question, text)
print(f"{pattern_lazy_plus_question}: {len(count)}個マッチ -- {count}")

count = re.findall(pattern_lazy_asta_question, text)
print(f"{pattern_lazy_asta_question}: {len(count)}個マッチ -- {count}")

