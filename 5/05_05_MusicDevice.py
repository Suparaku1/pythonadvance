class AudioPlayerMixin:
    def play(self) -> None:
        print("Audio: play")

    def pause(self) -> None:
        print("Audio: pause")


class RecorderMixin:
    def record(self) -> None:
        print("Recorder: record")

    def stop(self) -> None:
        print("Recorder: stop")


class Device:
    def __init__(self, name: str, model_number: str):
        self.name = name
        self.model_number = model_number


class MusicDevice(Device, AudioPlayerMixin, RecorderMixin):
    pass


if __name__ == "__main__":
    device = MusicDevice("Portable Music Device", "MD-100")

    print("Emri:", device.name)
    print("Modeli:", device.model_number)

    device.play()
    device.pause()
    device.record()
    device.stop()
