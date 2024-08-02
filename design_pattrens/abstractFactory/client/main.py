from design_pattrens.abstractFactory.Factory.AbstractAndroidFactory import AbstractAndroidFactory


def Deploy(val):
    if val == "ANDROID":
        Abs = AbstractAndroidFactory()
    if val == "IOS":
        Abs = AbstractIosFactory()
    Button = Abs.create_button().create()
    Button.click()
    Checkbox = Abs.create_checkbox().create()
    Checkbox.click()


if __name__ == '__main__':
    Deploy()
