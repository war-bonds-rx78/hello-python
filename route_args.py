def route(start, end, *args) :
    # 引数からルートを作る
#    route_list = [start]
#    route_list +=  list(args)
#    route_list += [end]
    route_list = list()
    route_list.append(start)
    route_list.extend(args)
    route_list.append(end)

    print(route_list)
    # リストの要素→で連絡した文字列にする
    route_str = "→".join(route_list)
    print(route_str)

start = "東京"
end = "宮崎"
route(start, end, "神戸", "長崎", "熊本")