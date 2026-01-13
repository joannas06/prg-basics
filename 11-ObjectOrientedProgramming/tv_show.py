from tv import TV

def main():
    # i. Create TV set
    my_tv = TV()

    # ii. Show TV status
    my_tv.show_status()

    # iii. Turn TV on
    my_tv.turn_on()
    my_tv.change_volume(5)

    # iv. Show TV status
    my_tv.show_status()
    
    #set channels
    list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    my_tv.set_channels(list)
    my_tv.show_channels()

    #change channel no
    my_tv.change_channel_no(3)
    my_tv.show_status()

    # v. Turn TV off
    my_tv.turn_off()

    # vi. Show TV status
    my_tv.show_status()

if __name__ == "__main__":
    main()