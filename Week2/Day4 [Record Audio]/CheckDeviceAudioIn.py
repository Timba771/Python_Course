import sounddevice as sd
print(sd.query_devices())
print("Default devices:", sd.default.device)
