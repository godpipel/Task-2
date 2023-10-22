
from Math_function import add


def main():
    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+" or operator == "-" or operator == "%" :
        result = add(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
    else:
        print("Operator tidak valid. Gunakan operator '+,-,(%)' untuk penambahan,pengurangan dan modulus.")

if __name__ == "__main__":
    print("Hello Main !")
    main()
