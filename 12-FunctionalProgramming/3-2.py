text = 'I completely agree with you'

result = list(map(lambda x: len(x.split(text)),text))

print(result)