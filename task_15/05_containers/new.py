
def sort_containers() -> str:
    quant_containers = int(input("Введите кол-во контейнеров: "))
    store = []
    while quant_containers != 0:
        weight_container = int(input("Введите вес контейнера: "))
        if weight_container > 200:
            print("Вес контейнера не должен превышать 200 кг")
        else:
            quant_containers -= 1
            store.append(weight_container)

    store.sort(reverse=True)
    new_weight = int(input("Введите вес нового контейнера: \t"))

    insert_index = 0
    for i, weight_cont in enumerate(store):
        if new_weight <= weight_cont:
            insert_index += 1
        else:
            break
    store.insert(insert_index, new_weight)

    return f"Номер, который получит новый контейнер: {insert_index + 1}"


if __name__ == "__main__":
    print(sort_containers())