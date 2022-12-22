def remove_parentheses(text):
    count_brackets = 0  
    memorise_erase_piece = ''  
    for letter in text:    
        if letter == '(':
            count_brackets += 1

        if count_brackets > 0:
            memorise_erase_piece += letter

        if letter == ')':
            count_brackets -= 1

            if count_brackets == 0:
                text = text.replace(memorise_erase_piece, '')
                memorise_erase_piece = ''
    return text
                


print(remove_parentheses("This is text(This is text)"))

    









