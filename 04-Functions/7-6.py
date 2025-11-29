def hide(card_number):
    return card_number[0:2] + '**********' + card_number[11:16]

if __name__ == "__main__":
    print(hide('123456789012345'))