from collections import deque

stack = deque()  
def menu():
    print("\n=== PROGRAM STACK / DEQUE ===")
    print("a. append (tambah di kanan)")
    print("b. appendleft (tambah di kiri)")
    print("c. pop (ambil dari kanan)")
    print("d. popleft (ambil dari kiri)")
    print("e. clear (hapus semua)")
    print("f. keluar")
    return input("Pilih menu: ").lower()

while True:
    pilihan = menu()

    if pilihan == "a":
        data = input("Masukkan data: ")
        stack.append(data)
        print("Data berhasil di-append:", data)

    elif pilihan == "b":
        data = input("Masukkan data: ")
        stack.appendleft(data)
        print("Data berhasil di-appendleft:", data)

    elif pilihan == "c":
        if len(stack) == 0:
            print("Stack kosong!")
        else:
            print("Data yang di-pop:", stack.pop())

    elif pilihan == "d":
        if len(stack) == 0:
            print("Stack kosong!")
        else:
            print("Data yang di-popleft:", stack.popleft())

    elif pilihan == "e":
        stack.clear()
        print("Semua data telah dihapus.")

    elif pilihan == "f":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")

    print("Isi stack sekarang:", list(stack))
