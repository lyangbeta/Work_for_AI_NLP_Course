# code1-generate the sentence
import random
import networkx
grammar = """
sentence = adj noun verb adv noun2
adj = adj_single adj_single 的 | null
adj_single = 漂亮 | 蓝色 | 好看
adv = 安静地 | 静静地
verb = adv 看着 | adv 坐着
noun2 = 桌子 | 皮球
noun = 猫 | 女人 | 男人
"""

def build_grammar(grammar_str, split_str='='):
    grammar_pattern = {}
    for line in grammar_str.split('\n'):
        if len(line)==0:
            continue
        stat,expr=line.split(split_str)
        grammar_pattern[stat.strip()] = [e.strip() for e in expr.split('|')]
    return grammar_pattern

def generate_sentence(dict , target):
    if target not in dict:
        return target
    pattern = dict[target]
    expr1 = random.choice(pattern)
    list = expr1.split()
    tokens = [generate_sentence(dict, expr) for expr in list]
    return ''.join([t for t in tokens if t != 'null'])

# code2-BFS and DFS  the two ways for searching
graph = {
    'A' :'B B B C',
    'B' : 'A C',
    'C' : 'A B D E',
    'D' : 'C',
    'E' : 'C F',
    'F' : 'E'
}
def Searching(graph,start,ways='BFS'):
    need_visit_list = [node for node in graph[start].split(' ')]
    seen = set(start)
    serching_list = [start]
    while need_visit_list:
        node = need_visit_list.pop(0)
        serching_list += node
        if node in seen:
            continue
        seen.add(node)
        new = [node for node in graph[node].split(' ')]
        if ways=='BFS':
            need_visit_list = need_visit_list+[node for node in graph[node].split(' ')]
        elif ways=='DFS':
            need_visit_list = [node for node in graph[node].split(' ')]+need_visit_list
    print(serching_list)

#code3-searching path

BJ = 'Beijing'
SZ = 'Shenzhen'
GZ = 'Guangzhou'
WH = 'Wuhan'
HLG = 'Heilongjiang'
NY = 'New York City'
CM = 'Chiangmai'
SG = 'Singapore'

air_route = {
    BJ : {SZ, GZ, WH, HLG, NY},
    GZ : {WH, BJ, CM, SG},
    SZ : {BJ, SG},
    WH : {BJ, GZ},
    HLG : {BJ},
    CM : {GZ},
    NY : {BJ},
    SG : {CM}
}

def searching_path(air_route,start,destination):
    path_list = [[start]]
    seen = set()
    all_paths = []
    while path_list:
        path = path_list.pop(0)
        cur_node = path[-1]
        if cur_node in seen:
            continue
        for city in air_route[cur_node]:
            new_path = path+[city]
            if city == destination:
                all_paths.append(new_path)
            path_list = path_list + [new_path]
        seen.add(cur_node)
    print(all_paths)
    return all_paths


def search_destination(graph, start, destination):
    pathes = [[start]]
    seen = set()
    chosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]
        if frontier in seen: continue
        # get new lines
        for city in graph[frontier]:
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination:
                chosen_pathes.append(new_path)
        seen.add(frontier)
    print (chosen_pathes)
    return chosen_pathes

if __name__=="__main__":
    res_grammar=build_grammar(grammar)
    target = 'sentence'
    #print(generate_sentence(res_grammar,target))
    start = 'A'
    ways = 'DFS'
    #Searching(graph,start,ways)
    start_city = BJ
    destination = CM
    searching_path(air_route, start_city, destination)




