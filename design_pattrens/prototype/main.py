from design_pattrens.prototype.Zombie import Zombie

if __name__ == '__main__':
    z = Zombie(100)

    arr = []
    for i in range(100):
        arr.append(z.clone())

    arr[0].health=99

    print(arr[1])
    print(arr)