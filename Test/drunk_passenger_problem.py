import random


def simulate_drunk_passenger(trials, n):
    last_seat_correct = 0  # 마지막 승객이 올바른 좌석에 앉은 경우의 수

    for _ in range(trials):
        seats = [i for i in range(n)]  # 좌석 번호 초기화
        random.shuffle(seats)  # 첫 번째 승객이 무작위로 좌석을 선택하도록 섞음

        # 첫 번째 승객이 무작위 좌석에 앉음
        first_passenger_seat = seats.pop(random.randint(0, n - 1))

        for passenger in range(1, n - 1):
            if passenger in seats:
                seats.remove(passenger)
            else:
                seats.pop(random.randint(0, len(seats) - 1))

        # 마지막 승객이 자신의 좌석에 앉는 경우 카운트
        if seats[0] == n - 1 or first_passenger_seat == n - 1:
            last_seat_correct += 1

    return last_seat_correct / trials


if __name__ == '__main__':
    for simulation_count in range(1, 21):
        print(f"{simulation_count}번째 시뮬레이션: {simulate_drunk_passenger(10000, 100)}")
