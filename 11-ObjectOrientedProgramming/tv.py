class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    
    def change_volume(self,new_volume):
        if new_volume in range(0,10):
            self.volume = new_volume
        else:
            print("Out of range!")

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        # Displays the numbered list of channels
        print("Channel list:")
        for index, name in enumerate(self.channels, start=1):
            print(f"{index}. {name}")

    def change_channel_no(self, new_number):
        self.channel_no = new_number

    def show_status(self):
        if self.is_on:
            # Check if the channel number exists in our list
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({channel_name}), volume is {self.volume}")
            else:
                # If channel is out of range, show only the number
                print(f"TV is on, channel {self.channel_no}, the volume is: {self.volume}")
        else:
            print("TV is off")