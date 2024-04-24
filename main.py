from Rifle import Rifle


def main():
    AK = Rifle(7.62, 206.5, 720)
    M4 = Rifle(7.62, 20.5, 720)
    print(AK == M4)

if __name__ == '__main__':
    main()
