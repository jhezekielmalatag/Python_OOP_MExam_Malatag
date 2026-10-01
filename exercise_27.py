class Device:
	room = "Lab 1"

	def __init__(self, asset_tag):
		self.asset_tag = asset_tag

if __name__ == "__main__":
	first = Device("D-01")
	second = Device("D-02")
	Device.room = "Lab 2"
	first.room = "Repair Bench"

	print(second.room)
	print(Device.room)