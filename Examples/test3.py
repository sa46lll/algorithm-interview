
def solution(n, plans, clients):
    answer = [0] * len(clients)
    rate_plans = []
    for plan in plans:
        plan = list(map(int, plan.split()))
        rate_plans.append([plan[0], plan[1:]])  # [제공 데이터, [제공 부가 서비스]
    for c_idx, client in enumerate(clients):
        inf = list(map(int, client.split()))
        c_data, c_services = inf[0], inf[1:]  # [이용 데이터, [이용 부가 서비스]

        for idx, plan in enumerate(rate_plans):
            data, services = plan
            if data < c_data:  # 데이터가 적을 때
                for s in services:
                    try:
                        c_services.remove(s)
                        continue
                    except ValueError:
                        continue

            else:  # 데이터를 만족하면,
                for s in services:
                    try:
                        c_services.remove(s)
                        continue
                    except ValueError:
                        continue

                if len(c_services) == 0:  # 부가서비스를 모두 만족하면,
                    answer[c_idx] = idx + 1
                    break

    return answer


# Test
print(solution(5, ["100 1 3", "500 4", "2000 5"],
               ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))  # [3, 3, 1, 0]
print(solution(4, ["38 2 3", "394 1 4"],
               ["10 2 3", "300 1 2 3 4", "500 1"]))  # [1, 2, 0]
