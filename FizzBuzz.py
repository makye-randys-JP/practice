#PyQで覚えたList内包表記を使ってみる。
count = [counter for counter in range(1,101)]

def FizzBazz(list_num):
    #3の倍数は’Fizz’、5の倍数は’Buzz’、
    #3かつ5の倍数は'FizzBuzz'に変換して表示。
    for num in list_num:
        if num % 3 == 0:
            print('Fizz', end ='')
        if num % 5 == 0:
            print('Buzz', end ='')
        elif num % 3 != 0 and num % 5 != 0:
            print(num, end ='')
        print('')

def main():
    FizzBazz(count)

if __name__ == '__main__':
    #importの際に実行されないようにする処理。
    main()