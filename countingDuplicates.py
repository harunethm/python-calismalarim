def duplicate_count(text):
    count = 0
    text = text.lower()
    for i in text:
        if(text.count(i) > 1):
            count += 1
            text = text.replace(i, "")
    return count





print(duplicate_count("aabBcde"))