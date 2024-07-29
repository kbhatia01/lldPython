from abc import ABC, abstractmethod


class SwitchAble(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass



class Light(SwitchAble):
    def turn_on(self):
        print("light Turning on")

    def turn_off(self):
        print("light Turning off")


class fan(SwitchAble):
    def turn_on(self):
        print("fan Turning on")

    def turn_off(self):
        print("fan Turning off")


class microwave(SwitchAble):
    def turn_on(self):
        print("microwave Turning on")

    def turn_off(self):
        print("microwave Turning off")


class Switch:
    def __init__(self, appliance):
        self.appliance = appliance

    def toggle(self, state):
        if state == "on":
            self.appliance.turn_on()

        else:
            self.appliance.turn_off()


light = Light()
s = Switch(light)

s.toggle("on")
s.toggle("off")

f = fan()
s2 = Switch(f)
s2.toggle("on")
s2.toggle("off")

m = microwave()
s3 = Switch(m)
s3.toggle("on")
s3.toggle("off")

# class SwitchFan:
#     def __init__(self, light):
#         self.light = light
#
#     def toggle(self, state):
#         if state == "on":
#             self.light.turn_on_fan()
#
#         else:
#             self.light.turn_off_fan()



# class fan():
#     def turn_on_fan(self):
#         print("fan Turning on")
#
#     def turn_off_fan(self):
#         print("fan Turning off")






















# class StatusMapper(ABC):
#
#     @abstractmethod
#     def status_mapper(self, staus):
#         pass
# class databrick(StatusMapper):
#
#     def get_status(self):
#         return "SUCCESS"
#     def status_mapper(self,staus):
#
#         if staus == "SUCCESS":
#             return "DONE"
#
#         else:
#             raise Exception(staus)
# class SnowFlake(StatusMapper):
#     def get_status(self,staus):
#         return "SUCCESSFUL"
#     def status_mapper(self,staus):
#         if staus == "SUCCESSFUL":
#                 return "DONE"
#
#
# def mycode():
#     api = SnowFlake()
#     if api.status_mapper(api.get_status) == "DONE":
#         print("Databrick is on")