from tkinter import *


class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.entry_strings = []
        self.zone_paces = {}
        self.zone_times = {'zone 1': 0, 'zone 2': 0, 'zone 3': 0, 'zone 4': 0, 'zone 5': 0}
        self.total_time = 0

        self.title = Label(master, text='Interval Distance Calculator')
        self.zones_label = Label(master, text='Pace Zones (m:ss-m:ss)')
        self.z1_label = Label(master, text='Zone 1')
        self.z1_entry = Entry(master, textvariable=StringVar)
        self.z2_label = Label(master, text='Zone 2')
        self.z2_entry = Entry(master, textvariable=StringVar)
        self.z3_label = Label(master, text='Zone 3')
        self.z3_entry = Entry(master, textvariable=StringVar)
        self.z4_label = Label(master, text='Zone 4')
        self.z4_entry = Entry(master, textvariable=StringVar)
        self.z5_label = Label(master, text='Zone 5')
        self.z5_entry = Entry(master, textvariable=StringVar)
        self.interval_label = Label(master, text='Enter your interval workout (zone x, y min; etc)')
        self.interval_entry = Entry(master, width=100, textvariable=StringVar)
        self.distance_label = Label(master, text='') 
        self.title.grid(row=0, column=4, columnspan=2)
        self.zones_label.grid(row=1, column=4, columnspan=2)
        self.z1_label.grid(row=2, column=0)
        self.z1_entry.grid(row=2, column=1)
        self.z2_label.grid(row=2, column=2)
        self.z2_entry.grid(row=2, column=3)
        self.z3_label.grid(row=2, column=4)
        self.z3_entry.grid(row=2, column=5)
        self.z4_label.grid(row=2, column=6)
        self.z4_entry.grid(row=2, column=7)
        self.z5_label.grid(row=2, column=8)
        self.z5_entry.grid(row=2, column=9)
        self.interval_label.grid(row=3, column=4, columnspan=3)
        self.interval_entry.grid(row=4, column=3, columnspan=5)

        def get_zones(self):
            z1_entry = self.z1_entry.get()
            z2_entry = self.z2_entry.get()
            z3_entry = self.z3_entry.get()
            z4_entry = self.z4_entry.get()
            z5_entry = self.z5_entry.get()
            self.entry_strings = [z1_entry, z2_entry, z3_entry, z4_entry, z5_entry]
            print(f'The zone ranges are: {self.entry_strings}')
            return self.entry_strings
         
        def calculate_avgs(self):
            n = 1
            for i in self.entry_strings:
                slow_min = int(i[:1])  
                slow_sec = int(i[2:4])  
                fast_min = int(i[5:6])  
                fast_sec = int(i[7:9])  
                slow_pace = slow_min * 60 + slow_sec  
                fast_pace = fast_min * 60 + fast_sec  
                avg_pace = (slow_pace + fast_pace) / 2  
                self.zone_paces["zone {0}".format(n)] = avg_pace
                n += 1
            print(f'The average speeds are: {self.zone_paces}')
            
        def get_intervals(self):
            workout_string = self.interval_entry.get()
            workout_intervals = tuple(workout_string.split("; "))
            for i in workout_intervals:
                interval_entry = i.split(', ')
                interval_zone = interval_entry[0]
                interval_time = interval_entry[1]
                time_value = int(''.join([n for n in interval_time if n.isdigit()]))
                self.zone_times[interval_zone] = (
                            self.zone_times[interval_zone] + time_value * 60)
            print(f'the zone times are: {self.zone_times} seconds')

        def get_total_time(self):
            self.total_time = sum(self.zone_times.values())
            print(f'the workout total time is {self.total_time} seconds')
            return self.total_time         

        def calculate_distance(self):
            get_zones(self)
            calculate_avgs(self)
            get_intervals(self)
            get_total_time(self)
            avg_speed_components = {}
            for i in self.zone_times:
                time_fraction = self.zone_times[i] / self.total_time
                zone_speed_contribution = time_fraction * self.zone_paces[i]
                avg_speed_components[i] = zone_speed_contribution
            computed_avg = sum(avg_speed_components.values())
            distance = (self.total_time / computed_avg)
            self.distance_label = Label(master, text=f"Estimated distance: {distance:.1f} kilometers")
            self.distance_label.grid(row=5, column=4, columnspan=3)

        def reset_params():
            self.entry_strings = []
            self.zone_paces = {}
            self.zone_times = {'zone 1': 0, 'zone 2': 0, 'zone 3': 0, 'zone 4': 0, 'zone 5': 0}
            self.total_time = 0

        def button_click():
            print('button clicked')
            calculate_distance(self)
            reset_params()
            
        self.calculate_button = Button(master, text='calculate distance', command=button_click)
        self.calculate_button.grid(row=5, column=3, columnspan=2)


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()