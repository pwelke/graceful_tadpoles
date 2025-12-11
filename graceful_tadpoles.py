
def fig1(m, n):
    assert(m % 4 == 2)
    assert(n == 1 or n >= 3) # careful. n >= 3 requires additional tail nodes added in another step

    l = (m - 2) // 4 

    vertices = list()

    # point A1 will be at index 0, followed by m-1 cycle nodes, clockwise. 
    vertices.append(n + 2*l + 1)
    vertices.append(2*l + 1)

    for i in range(l+1):
        vertices.append(n + 4*l + 2 - i)
        vertices.append(i)
    
    for i in range(l+1,2*l):
        vertices.append(n + 4*l + 1 - i) # after l, we shift this by one. 
        vertices.append(i)

    edges = list(zip(vertices, vertices[1:] + [vertices[0]]))

    # Then 1 path node
    vertices.append(2*l)

    # and the edge connecting it to the cycle
    edges.append((vertices[0], vertices[m])) # edge connecting path and cycle

    return vertices, edges


def fig2(m, n):
    assert(m % 4 == 2)
    assert(n == 2)

    l = (m - 2) // 4 
    vertices = list()

    # point A1 will be at index 0, followed by m-1 cycle nodes, counterclockwise. 
    vertices.append(3*l+5)

    # we create increasing edge weights [2l+6, ..., m+n] by alternatingly increasing and decreasing the vertex label 
    # the last node constructed by this loop is the vertex with label 0
    startlength_counterclockwise = 2*l + 6 #3*l + 5 - (l - 1)
    decrease = True
    for w in range(startlength_counterclockwise, m+n+1):
        current = vertices[-1]
        if decrease:
            vertices.append(current - w)
            decrease = False
        else:
            vertices.append(current + w)
            decrease = True

    vertices.append(2*l + 4)

    # we create increasing edge weights [2, ..., 2l+2] by alternatingly increasing and decreasing the vertex label
    # the last node constructed by this loop is the vertex with label l+2
    decrease = True
    for w in range(2, 2*l+3):
        current = vertices[-1]
        if decrease:
            vertices.append(current - w)
            decrease = False
        else:
            vertices.append(current + w)
            decrease = True       

    # create cycle edges
    edges = list(zip(vertices, vertices[1:] + [vertices[0]]))

    # Then 2 path nodes
    vertices.append(l)
    vertices.append(l+1)

    # create tail edges
    edges.append((vertices[0], vertices[m])) # edge connecting path and cycle
    edges.append((vertices[m], vertices[m+1])) # path edge

    return vertices, edges

def case_3_1(m, n):
    assert(n % 6 == 3)

    head_vertices, head_edges = fig1(m, n)

    tail_vertices = list() 
    s = (n - 3) // 6
    a = n+2*l+1
    b = 2*l
    for i in range(s):
        tail_vertices.append(b+3*i)
        tail_vertices.append(a-2-3*i)
        tail_vertices.append(b+2+3*i)
        tail_vertices.append(a-1-3*i)
        tail_vertices.append(b+4+3*i)
        tail_vertices.append(a-3-3*i)
    tail_vertices.append(b+3*s)
    tail_vertices.append(2*l+2+3*s)
    tail_vertices.append(2*l+3+3*s)

    # construct tail edges
    tail_edges = [(u,v) for u,v in zip(tail_vertices, tail_vertices[1:])]

    # we are constructing edge labels for B_1, ... B_n, hence we drop B_1, 
    # as it is already part of the output of fig1
    return head_vertices + tail_vertices[1:], head_edges + tail_edges


def case_3_2(m, n):
    assert(n % 6 == 4)

    head_vertices, head_edges = fig1(m, n)

    tail_vertices = list() 
    s = (n - 3) // 6
    a = n+2*l+1
    b = 2*l
    for i in range(s):
        tail_vertices.append(b+3*i)
        tail_vertices.append(a-2-3*i)
        tail_vertices.append(b+2+3*i)
        tail_vertices.append(a-1-3*i)
        tail_vertices.append(b+4+3*i)
        tail_vertices.append(a-3-3*i)
    tail_vertices.append(b+3*s)
    tail_vertices.append(2*l+3+3*s)
    tail_vertices.append(2*l+2+3*s)
    tail_vertices.append(2*l+4+3*s)

    # construct tail edges
    tail_edges = [(u,v) for u,v in zip(tail_vertices, tail_vertices[1:])]

    # we are constructing edge labels for B_1, ... B_n, hence we drop B_1, 
    # as it is already part of the output of fig1
    return head_vertices + tail_vertices[1:], head_edges + tail_edges


def case_3_3(m, n):
    assert(n % 6 == 5)

    head_vertices, head_edges = fig1(m, n)

    tail_vertices = list() 
    s = (n - 3) // 6
    a = n+2*l+1
    b = 2*l
    for i in range(s):
        tail_vertices.append(b+3*i)
        tail_vertices.append(a-2-3*i)
        tail_vertices.append(b+2+3*i)
        tail_vertices.append(a-1-3*i)
        tail_vertices.append(b+4+3*i)
        tail_vertices.append(a-3-3*i)
    tail_vertices.append(b+3*s)
    tail_vertices.append(2*l+4+3*s)
    tail_vertices.append(2*l+3+3*s)
    tail_vertices.append(2*l+5+3*s)
    tail_vertices.append(2*l+2+3*s)

    # construct tail edges
    tail_edges = [(u,v) for u,v in zip(tail_vertices, tail_vertices[1:])]

    # we are constructing edge labels for B_1, ... B_n, hence we drop B_1, 
    # as it is already part of the output of fig1
    return head_vertices + tail_vertices[1:], head_edges + tail_edges

def case_3_4(m, n):
    assert(n % 6 == 0)

    head_vertices, head_edges = fig1(m, n)

    tail_vertices = list() 
    s = (n - 3) // 6
    a = n+2*l+1
    b = 2*l
    for i in range(s):
        tail_vertices.append(b+3*i)
        tail_vertices.append(a-2-3*i)
        tail_vertices.append(b+2+3*i)
        tail_vertices.append(a-1-3*i)
        tail_vertices.append(b+4+3*i)
        tail_vertices.append(a-3-3*i)
    tail_vertices.append(b+3*s)
    tail_vertices.append(2*l+5+3*s)
    tail_vertices.append(2*l+2+3*s)
    tail_vertices.append(2*l+6+3*s)
    tail_vertices.append(2*l+4+3*s)
    tail_vertices.append(2*l+3+3*s)


    # construct tail edges
    tail_edges = [(u,v) for u,v in zip(tail_vertices, tail_vertices[1:])]

    # we are constructing edge labels for B_1, ... B_n, hence we drop B_1, 
    # as it is already part of the output of fig1
    return head_vertices + tail_vertices[1:], head_edges + tail_edges


def case_3_5(m, n):
    assert(n % 6 == 1)

    head_vertices, head_edges = fig1(m, n)

    tail_vertices = list() 
    s = (n - 3) // 6
    a = n+2*l+1
    b = 2*l
    for i in range(s):
        tail_vertices.append(b+3*i)
        tail_vertices.append(a-2-3*i)
        tail_vertices.append(b+2+3*i)
        tail_vertices.append(a-1-3*i)
        tail_vertices.append(b+4+3*i)
        tail_vertices.append(a-3-3*i)
    tail_vertices.append(b+3*s)
    tail_vertices.append(2*l+6+3*s)
    tail_vertices.append(2*l+2+3*s)
    tail_vertices.append(2*l+7+3*s)
    tail_vertices.append(2*l+4+3*s)
    tail_vertices.append(2*l+5+3*s)
    tail_vertices.append(2*l+3+3*s)

    # construct tail edges
    tail_edges = [(u,v) for u,v in zip(tail_vertices, tail_vertices[1:])]

    # we are constructing edge labels for B_1, ... B_n, hence we drop B_1, 
    # as it is already part of the output of fig1
    return head_vertices + tail_vertices[1:], head_edges + tail_edges


def case_3_6(m, n):
    assert(n % 6 == 2)

    head_vertices, head_edges = fig1(m, n)

    tail_vertices = list() 
    s = (n - 3) // 6
    a = n+2*l+1
    b = 2*l
    for i in range(s):
        tail_vertices.append(b+3*i)
        tail_vertices.append(a-2-3*i)
        tail_vertices.append(b+2+3*i)
        tail_vertices.append(a-1-3*i)
        tail_vertices.append(b+4+3*i)
        tail_vertices.append(a-3-3*i)
    tail_vertices.append(b+3*s)
    tail_vertices.append(2*l+7+3*s)
    tail_vertices.append(2*l+2+3*s)
    tail_vertices.append(2*l+8+3*s)
    tail_vertices.append(2*l+4+3*s)
    tail_vertices.append(2*l+5+3*s)
    tail_vertices.append(2*l+3+3*s)
    tail_vertices.append(2*l+6+3*s)

    # construct tail edges
    tail_edges = [(u,v) for u,v in zip(tail_vertices, tail_vertices[1:])]

    # we are constructing edge labels for B_1, ... B_n, hence we drop B_1, 
    # as it is already part of the output of fig1
    return head_vertices + tail_vertices[1:], head_edges + tail_edges


def thm1(m, n):
    assert(m % 4 == 2)
    assert(n > 0)

    if n == 1:
        return fig1(m, n)
    if n == 2:
        return fig2(m, n)
    else:
        if n % 6 == 3:
            return case_3_1(m, n)
        if n % 6 == 4:
            return case_3_2(m, n)
        if n % 6 == 5:
            return case_3_3(m, n)
        if n % 6 == 0:
            return case_3_4(m, n)
        if n % 6 == 1:
            return case_3_5(m, n)
        if n % 6 == 2:
            return case_3_6(m, n)


def fig3(m, n):
    assert(m % 4 == 1)
    assert(n % 2 == 1)

    l = (m - 1) // 4
    k = (n - 1) // 2

    # assert (k > l - 2)

    vertices = [0]
    decrease = False
    offset = 0
    for w in range(n+m, 1, -1):
        current = vertices[-1]
        if w == 2*l:
            offset = -1
        if decrease:
            vertices.append(current - (w + offset))
            decrease = False
        else:
            vertices.append(current + w + offset)
            decrease = True

    # construct a long path
    edges = [(u,v) for u,v in zip(vertices, vertices[1:])]
    # add the edge connecting 0 with 2l that closes the head cycle
    edges.append((vertices[0], vertices[m-1]))

    return vertices, edges


def fig4(m, n):
    assert(m % 4 == 1)
    assert(n == 2)

    l = (m - 1) // 4

    vertices = [l+2, l+1]

    decrease = False
    for w in range(2*l+1, 4*l+4, 1):
        current = vertices[-1]
        if decrease:
            vertices.append(current - w)
            decrease = False
        else:
            vertices.append(current + w)
            decrease = True

    if 2*l+3 != 3*l+2:
        vertices.append(2*l+3)

    decrease = True
    for w in range(2, 2*l-1, 1):
        current = vertices[-1]
        if decrease:
            vertices.append(current - w)
            decrease = False
        else:
            vertices.append(current + w)
            decrease = True

    # construct a long path
    edges = [(u,v) for u,v in zip(vertices, vertices[1:])]
    # add the edge connecting 3l+2 with l+3 that closes the head cycle
    edges.append((vertices[-1], vertices[2]))

    return vertices, edges


def thm2(m, n):
    assert(m % 4 == 1)
    assert(n > 0)

    if n % 2 == 1:
        return fig3(m, n)
    if n % 2 == 0:
        if n == 2:
            return fig4(m, n)
        else:
            return [0,1], [(0,1)]


def is_graceful(vertices, edges):
    '''see if edge labels are unique. 
    this should suffice if node labels are injective'''

    # vertex labels in range 0...m (inclusive)?
    proper_range = min(vertices) >= 0 and max(vertices) <= len(edges)

    # vertex labels injective?
    injective_vertex_labels = len(set(vertices)) == len(vertices)

    # edge labels injective?
    labels = set()
    for e in edges:
        labels.add(abs(e[0] - e[1]))
    injective_edge_labels = len(labels) == len(edges)

    print(f'Proper vertex range? {proper_range}\nInjective vertex labels? {injective_vertex_labels}\nInjective edge labels? {injective_edge_labels}')
    return proper_range and injective_vertex_labels and injective_edge_labels


def edge_labels(edges):
    '''get edge label dict for nx drawing'''

    labels = dict()
    for e in edges:
        labels[e] = abs(e[0] - e[1])

    return labels


def draw_graph(e):
    import networkx as nx
    import matplotlib.pyplot as plt

    g = nx.from_edgelist(e)
    pos1 = nx.circular_layout(g)
    nx.draw(g, pos1, with_labels=True, node_color='skyblue')
    nx.draw_networkx_edge_labels(g, pos1, edge_labels=edge_labels(e))
    plt.show()


for l in range(1, 20):
    for n in range(1, 20):
        m = 4*l + 1
        v, e = thm2(m, n)

        print(f'V = {v}')
        print(f'E = {e}')
        if not is_graceful(v,e):
            print(f'nnodes = {len(v)} (should be {m+n})')
            print(f'nedges = {len(e)} (should be {m+n})')
            draw_graph(e)