# https://www.codewars.com/kata/59e9f404fc3c49ab24000112/train/python
def nerdify(txt: str) -> str:
    new_text = txt
    new_text = new_text.replace('a', '4')
    new_text = new_text.replace('A', '4')
    new_text = new_text.replace('e', '3')
    new_text = new_text.replace('E', '3')
    new_text = new_text.replace('l', '1')
    return new_text

print(nerdify('Fundamentals'))